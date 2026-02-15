"""CLI commands for validating narratological studies.

Ensures synchronization between Markdown sources and JSON structured data.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from narratological.loader import load_compendium, load_study, load_study_from_file
from narratological.models.study import Compendium, CompendiumMeta, Study
from narratological.validation import validate_study

app = typer.Typer(help="Validate data integrity and synchronization")
console = Console()


@app.command()
def sync(
    extracts_dir: Annotated[
        Path,
        typer.Option(
            "--extracts-dir",
            "-e",
            help="Directory containing JSON extracts",
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ] = Path("specs/03-structured-data/json-extracts"),
    output_file: Annotated[
        Path,
        typer.Option(
            "--output",
            "-o",
            help="Path to output unified JSON",
        ),
    ] = Path("specs/03-structured-data/narratological-algorithms-unified.json"),
    publish: bool = typer.Option(
        True, help="Also update the packaged resource in core package"
    ),
) -> None:
    """Rebuild the unified compendium from individual JSON extracts."""
    console.print(f"Scanning for extracts in [dim]{extracts_dir}[/dim]...")
    
    json_files = list(extracts_dir.glob("*.json"))
    if not json_files:
        console.print("[bold red]Error:[/bold red] No JSON files found in extracts directory.")
        raise typer.Exit(1)

    studies = {}
    categories = set()

    for json_file in json_files:
        try:
            study = load_study_from_file(json_file)
            studies[study.id] = study
            categories.add(study.category.value)
            console.print(f"  [green]✓[/green] Loaded [cyan]{study.id}[/cyan]")
        except Exception as e:
            console.print(f"  [red]✗[/red] Failed to load [bold]{json_file.name}[/bold]: {e}")

    # Build metadata
    meta = CompendiumMeta(
        title="Narratological Algorithmic Lenses Compendium",
        version="0.1.0",
        generated=datetime.now().isoformat(),
        study_count=len(studies),
        categories=sorted(list(categories)),
    )

    # Note: Sequence pairs and other cross-references should be preserved
    # For now, we'll try to load existing cross-references if the output file exists
    cross_references = {}
    if output_file.exists():
        try:
            old_data = json.loads(output_file.read_text())
            cross_references = old_data.get("cross_references", {})
            console.print("[dim]Preserving existing cross-references.[/dim]")
        except Exception:
            pass

    compendium = Compendium(
        meta=meta,
        studies=studies,
        cross_references=cross_references,
    )

    # Write to specs
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        compendium.model_dump_json(indent=2), encoding="utf-8"
    )
    console.print(f"\n[bold green]Unified compendium written to:[/bold green] {output_file}")

    # Optionally publish to core package
    if publish:
        package_resource = Path("packages/core/src/narratological/data/narratological-algorithms-unified.json")
        if package_resource.parent.exists():
            package_resource.write_text(
                compendium.model_dump_json(indent=2), encoding="utf-8"
            )
            console.print(f"[bold green]Published to package resource:[/bold green] {package_resource}")
        else:
            console.print(f"[yellow]Warning: Package resource directory not found at {package_resource.parent}[/yellow]")


def _resolve_markdown_path(study_id: str, search_dir: Path) -> Path | None:
    """Find the markdown file for a study ID using common patterns."""
    # Handle cases like 'warren-ellis' -> 'ellis'
    last_name = study_id.split("-")[-1] if "-" in study_id else study_id

    patterns = [
        f"{study_id}-narratological-algorithms.md",
        f"{study_id}_narratological_study.md",
        f"{study_id}.md",
        f"{study_id.replace('-', '_')}_narratological_study.md",
        f"{study_id.replace('_', '-')}-narratological-algorithms.md",
        f"{last_name}-narratological-algorithms.md",
        f"{last_name}_narratological_study.md",
    ]

    for pattern in patterns:
        path = search_dir / pattern
        if path.exists():
            return path

    return None


@app.command()
def compendium(
    specs_dir: Annotated[
        Path,
        typer.Option(
            "--specs-dir",
            "-d",
            help="Directory containing markdown studies",
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ] = Path("specs/02-completed-studies"),
    verbose: bool = False,
) -> None:
    """Validate all studies in the compendium against their markdown sources."""
    try:
        compendium_data = load_compendium()
    except Exception as e:
        console.print(f"[bold red]Error loading compendium:[/bold red] {e}")
        raise typer.Exit(1)

    total_errors = 0
    total_warnings = 0
    studies_with_issues = 0

    table = Table(title="Compendium Validation Summary")
    table.add_column("Study ID", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Errors", justify="right", style="red")
    table.add_column("Warnings", justify="right", style="yellow")
    table.add_column("Markdown Source")

    for study_id, study in compendium_data.studies.items():
        md_path = _resolve_markdown_path(study_id, specs_dir)

        if md_path is None:
            table.add_row(
                study_id,
                "[bold red]MISSING[/bold red]",
                "1",
                "0",
                "[dim]Not found[/dim]",
            )
            total_errors += 1
            studies_with_issues += 1
            continue

        report = validate_study(study, md_path)

        if report.is_valid and not report.warnings:
            status = "[bold green]PASS[/bold green]"
        elif report.is_valid:
            status = "[bold yellow]WARN[/bold yellow]"
        else:
            status = "[bold red]FAIL[/bold red]"

        table.add_row(
            study_id,
            status,
            str(len(report.errors)),
            str(len(report.warnings)),
            md_path.name,
        )

        total_errors += len(report.errors)
        total_warnings += len(report.warnings)
        if report.errors or report.warnings:
            studies_with_issues += 1

        if verbose and (report.errors or report.warnings):
            console.print(f"\n[bold underline]Detail: {study_id}[/bold underline]")
            for issue in report.issues:
                color = "red" if issue.severity == "error" else "yellow"
                console.print(f"  [{color}]• {issue.field}: {issue.message}[/{color}]")

    console.print(table)

    summary_color = "green" if total_errors == 0 else "red"
    console.print(
        Panel(
            f"[{summary_color}]Validation Complete[/{summary_color}]\n"
            f"Studies Checked: {len(compendium_data.studies)}\n"
            f"Issues Found: {studies_with_issues} studies ({total_errors} errors, {total_warnings} warnings)",
            title="Results",
        )
    )

    if total_errors > 0:
        raise typer.Exit(1)


@app.command()
def study(
    study_id: str,
    specs_dir: Annotated[
        Path,
        typer.Option(
            "--specs-dir",
            "-d",
            help="Directory containing markdown studies",
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ] = Path("specs/02-completed-studies"),
) -> None:
    """Validate a specific study against its markdown source."""
    try:
        study_data = load_study(study_id)
    except KeyError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(1)

    md_path = _resolve_markdown_path(study_id, specs_dir)

    if md_path is None:
        console.print(f"[bold red]Error:[/bold red] Could not find markdown source for '{study_id}' in {specs_dir}")
        raise typer.Exit(1)

    console.print(f"Validating [bold cyan]{study_id}[/bold cyan] against [dim]{md_path}[/dim]...")
    report = validate_study(study_data, md_path)

    if report.is_valid and not report.warnings:
        console.print("[bold green]✓ Validation passed![/bold green]")
    else:
        if report.errors:
            console.print(f"[bold red]✗ Found {len(report.errors)} errors:[/bold red]")
            for err in report.errors:
                console.print(f"  [red]• {err.field}: {err.message}[/red]")

        if report.warnings:
            console.print(f"[bold yellow]! Found {len(report.warnings)} warnings:[/bold yellow]")
            for warn in report.warnings:
                console.print(f"  [yellow]• {warn.field}: {warn.message}[/yellow]")

    if not report.is_valid:
        raise typer.Exit(1)
