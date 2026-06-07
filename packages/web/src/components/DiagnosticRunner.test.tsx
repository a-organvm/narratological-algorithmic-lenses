import { describe, expect, it, vi, beforeEach } from 'vitest'
import { renderToString } from 'react-dom/server'
import { StaticRouter } from 'react-router-dom/server'
import DiagnosticRunner from './DiagnosticRunner'

beforeEach(() => {
  vi.restoreAllMocks()
})

describe('DiagnosticRunner', () => {
  it('renders without crashing', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(new Response(JSON.stringify([]), { status: 200 }))

    const html = renderToString(
      <StaticRouter location="/diagnostics">
        <DiagnosticRunner />
      </StaticRouter>,
    )
    expect(html).toBeDefined()
    expect(html.length).toBeGreaterThan(0)
  })

  it('shows loading state during SSR', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(new Response(JSON.stringify([]), { status: 200 }))

    const html = renderToString(
      <StaticRouter location="/diagnostics">
        <DiagnosticRunner />
      </StaticRouter>,
    )
    // loading=true is the initial state; useEffect hasn't fired
    expect(html).toContain('Loading...')
  })

  it('renders without crashing when fetch rejects', () => {
    vi.spyOn(globalThis, 'fetch').mockRejectedValue(new Error('API down'))

    const html = renderToString(
      <StaticRouter location="/diagnostics">
        <DiagnosticRunner />
      </StaticRouter>,
    )
    expect(html).toBeDefined()
    expect(html.length).toBeGreaterThan(0)
  })
})
