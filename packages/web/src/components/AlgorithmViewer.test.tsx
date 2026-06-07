import { describe, expect, it, vi, beforeEach } from 'vitest'
import { renderToString } from 'react-dom/server'
import { StaticRouter } from 'react-router-dom/server'
import AlgorithmViewer from './AlgorithmViewer'

beforeEach(() => {
  vi.restoreAllMocks()
})

describe('AlgorithmViewer', () => {
  it('renders algorithm browser heading on SSR without studyId', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(new Response('{}', { status: 200 }))

    const html = renderToString(
      <StaticRouter location="/algorithms">
        <AlgorithmViewer />
      </StaticRouter>,
    )
    // Without studyId and loading=false initially, SSR shows default browser view
    expect(html).toContain('Algorithm Browser')
  })

  it('renders without crashing when studyId is provided', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(
      new Response(
        JSON.stringify({
          id: 'aristotle',
          creator: 'Aristotle',
          work: 'Poetics',
          category: 'Classical',
          axioms: [],
          core_algorithms: [],
          diagnostic_questions: [],
          structural_hierarchy: { levels: [] },
          theoretical_correspondences: { maps_to: [], sequence_pairs: [] },
          quick_reference: { core_operations: [], key_constraints: [] },
        }),
        { status: 200 },
      ),
    )

    const html = renderToString(
      <StaticRouter location="/algorithms/aristotle/test-algo">
        <AlgorithmViewer />
      </StaticRouter>,
    )
    expect(html).toBeDefined()
    expect(html.length).toBeGreaterThan(0)
  })

  it('renders without crashing on error path', () => {
    vi.spyOn(globalThis, 'fetch').mockRejectedValue(new Error('Failed to load'))

    const html = renderToString(
      <StaticRouter location="/algorithms/aristotle/test">
        <AlgorithmViewer />
      </StaticRouter>,
    )
    expect(html).toBeDefined()
    expect(html.length).toBeGreaterThan(0)
  })
})
