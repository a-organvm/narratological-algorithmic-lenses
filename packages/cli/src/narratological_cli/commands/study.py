"""CLI commands for exploring narratological studies."""

from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree

app = typer.Typer(help="Explore narratological studies")
console = Console()


@app.command("list")
def list_studies(
    category: Annotated[
        str | None,
        typer.Option("--category", "-c", help="Filter by category"),
    ] = None,
) -> None:
    """List all available studies."""
    from narratological.loader import load_compendium
    from narratological.models.study import Category

    compendium = load_compendium()

    if category:
        try:
            cat = Category(category)
            studies = compendium.get_studies_by_category(cat)
        except ValueError:
            console.print(f"[red]Invalid category: {category}[/red]")
            console.print(f"Valid categories: {', '.join(c.value for c in Category)}")
            raise typer.Exit(1) from None
    else:
        studies = list(compendium.studies.values())

    table = Table(title="Narratological Studies")
    table.add_column("ID", style="cyan")
    table.add_column("Creator", style="green")
    table.add_column("Category", style="yellow")
    table.add_column("Axioms", justify="right")
    table.add_column("Algorithms", justify="right")

    for study in studies:
        table.add_row(
            study.id,
            study.creator,
            study.category.value,
            str(len(study.axioms)),
            str(len(study.core_algorithms)),
        )

    console.print(table)


@app.command("show")
def show_study(
    study_id: Annotated[str, typer.Argument(help="Study ID to show")],
    section: Annotated[
        str | None,
        typer.Option(
            "--section",
            "-s",
            help="Section to show: axioms, algorithms, questions, hierarchy, quick",
        ),
    ] = None,
) -> None:
    """Show details of a specific study."""
    from narratological.loader import load_study

    try:
        study = load_study(study_id)
    except KeyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    # Header
    console.print(Panel(
        f"[bold]{study.creator}[/bold]\n{study.work}",
        title=f"Study: {study.id}",
        subtitle=f"Category: {study.category.value}",
    ))

    if section is None or section == "axioms":
        _show_axioms(study)

    if section is None or section == "algorithms":
        _show_algorithms(study)

    if section == "questions":
        _show_questions(study)

    if section == "hierarchy":
        _show_hierarchy(study)

    if section == "quick":
        _show_quick_reference(study)


def _show_axioms(study) -> None:
    """Display study axioms."""
    console.print("\n[bold]Axioms[/bold]")
    for axiom in study.axioms:
        console.print(f"\n[cyan]{axiom.id}[/cyan] - [bold]{axiom.name}[/bold]")
        console.print(f"  {axiom.statement[:200]}..." if len(axiom.statement) > 200 else f"  {axiom.statement}")


def _show_algorithms(study) -> None:
    """Display study algorithms."""
    console.print("\n[bold]Core Algorithms[/bold]")
    for algo in study.core_algorithms:
        console.print(f"\n[green]{algo.name}[/green]")
        console.print(f"  [dim]Purpose:[/dim] {algo.purpose[:150]}..." if len(algo.purpose) > 150 else f"  [dim]Purpose:[/dim] {algo.purpose}")


def _show_questions(study) -> None:
    """Display diagnostic questions."""
    console.print("\n[bold]Diagnostic Questions[/bold]")
    for q in study.diagnostic_questions:
        console.print(f"\n[yellow]{q.id}[/yellow]: {q.question}")
        console.print(f"  [dim]Valid if:[/dim] {q.valid_if}")


def _show_hierarchy(study) -> None:
    """Display structural hierarchy."""
    console.print("\n[bold]Structural Hierarchy[/bold]")
    tree = Tree(f"[bold]{study.id}[/bold]")
    for level in study.structural_hierarchy.levels:
        branch = tree.add(f"[cyan]Level {level.level}:[/cyan] {level.name}")
        branch.add(f"[dim]{level.description}[/dim]")
        for elem in level.elements[:5]:  # Show first 5 elements
            branch.add(f"- {elem}")
        if len(level.elements) > 5:
            branch.add(f"[dim]... and {len(level.elements) - 5} more[/dim]")
    console.print(tree)


def _show_quick_reference(study) -> None:
    """Display quick reference card."""
    console.print("\n[bold]Quick Reference[/bold]")
    console.print("\n[underline]Core Operations:[/underline]")
    for op in study.quick_reference.core_operations:
        console.print(f"  - {op}")
    console.print("\n[underline]Key Constraints:[/underline]")
    for constraint in study.quick_reference.key_constraints:
        console.print(f"  - {constraint}")


@app.command("axiom")
def show_axiom(
    study_id: Annotated[str, typer.Argument(help="Study ID")],
    axiom_id: Annotated[str, typer.Argument(help="Axiom ID (e.g., IB-A0)")],
) -> None:
    """Show a specific axiom in detail."""
    from narratological.loader import load_study

    try:
        study = load_study(study_id)
    except KeyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    axiom = study.get_axiom(axiom_id)
    if axiom is None:
        console.print(f"[red]Axiom {axiom_id} not found in study {study_id}[/red]")
        raise typer.Exit(1)

    console.print(Panel(
        f"[bold]{axiom.name}[/bold]\n\n{axiom.statement}",
        title=f"Axiom: {axiom.id}",
    ))

    if axiom.derivations:
        console.print("\n[bold]Derivations:[/bold]")
        for d in axiom.derivations:
            console.print(f"  - {d}")


@app.command("algorithm")
def show_algorithm(
    study_id: Annotated[str, typer.Argument(help="Study ID")],
    algo_name: Annotated[str, typer.Argument(help="Algorithm name")],
) -> None:
    """Show a specific algorithm in detail."""
    from narratological.loader import load_study

    try:
        study = load_study(study_id)
    except KeyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    algo = study.get_algorithm(algo_name)
    if algo is None:
        # Try partial match
        matches = [a for a in study.core_algorithms if algo_name.lower() in a.name.lower()]
        if len(matches) == 1:
            algo = matches[0]
        elif matches:
            console.print("[yellow]Multiple matches found:[/yellow]")
            for m in matches:
                console.print(f"  - {m.name}")
            raise typer.Exit(1)
        else:
            console.print(f"[red]Algorithm '{algo_name}' not found in study {study_id}[/red]")
            raise typer.Exit(1)

    console.print(Panel(
        f"[bold]Purpose:[/bold] {algo.purpose}",
        title=f"Algorithm: {algo.name}",
    ))

    console.print("\n[bold]Pseudocode:[/bold]")
    console.print(Panel(algo.pseudocode, border_style="dim"))

    if algo.inputs:
        console.print("\n[bold]Inputs:[/bold]")
        for inp in algo.inputs:
            console.print(f"  - {inp}")

    if algo.outputs:
        console.print("\n[bold]Outputs:[/bold]")
        for out in algo.outputs:
            console.print(f"  - {out}")


@app.command("search")
def search_studies(
    query: Annotated[str, typer.Argument(help="Search query")],
    search_type: Annotated[
        str,
        typer.Option(
            "--type",
            "-t",
            help="Search type: axioms, algorithms, all",
        ),
    ] = "all",
) -> None:
    """Search across all studies."""
    from narratological.loader import load_compendium

    compendium = load_compendium()

    if search_type in ("all", "axioms"):
        axiom_results = compendium.search_axioms(query)
        if axiom_results:
            console.print(f"\n[bold]Axiom matches ({len(axiom_results)}):[/bold]")
            for study_id, axiom in axiom_results[:10]:
                console.print(f"  [{study_id}] [cyan]{axiom.id}[/cyan]: {axiom.name}")

    if search_type in ("all", "algorithms"):
        algo_results = compendium.search_algorithms(query)
        if algo_results:
            console.print(f"\n[bold]Algorithm matches ({len(algo_results)}):[/bold]")
            for study_id, algo in algo_results[:10]:
                console.print(f"  [{study_id}] [green]{algo.name}[/green]")


@app.command("pairs")
def show_sequence_pairs() -> None:
    """Show thematic sequence pairs between studies."""
    from narratological.loader import load_compendium

    compendium = load_compendium()
    pairs = compendium.get_sequence_pairs()

    table = Table(title="Thematic Sequence Pairs")
    table.add_column("ID", style="cyan")
    table.add_column("Theme")
    table.add_column("Studies", style="green")
    table.add_column("Shared Principles")

    for pair in pairs:
        table.add_row(
            pair.id,
            pair.name,
            " <-> ".join(pair.studies),
            ", ".join(pair.shared_principles[:3]) + ("..." if len(pair.shared_principles) > 3 else ""),
        )

    console.print(table)
