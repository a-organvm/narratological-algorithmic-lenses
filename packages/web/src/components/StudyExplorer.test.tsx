import { describe, expect, it, vi, beforeEach } from 'vitest'
import { renderToString } from 'react-dom/server'
import { StaticRouter } from 'react-router-dom/server'
import StudyExplorer from './StudyExplorer'

beforeEach(() => {
  vi.restoreAllMocks()
})

describe('StudyExplorer', () => {
  it('renders without crashing', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(new Response(JSON.stringify([]), { status: 200 }))

    const html = renderToString(
      <StaticRouter location="/">
        <StudyExplorer />
      </StaticRouter>,
    )
    expect(html).toBeDefined()
    expect(html.length).toBeGreaterThan(0)
  })

  it('shows loading state during SSR', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(new Response(JSON.stringify([]), { status: 200 }))

    const html = renderToString(
      <StaticRouter location="/">
        <StudyExplorer />
      </StaticRouter>,
    )
    // loading=true is the initial state; useEffect hasn't fired
    expect(html).toContain('Loading...')
  })
})
