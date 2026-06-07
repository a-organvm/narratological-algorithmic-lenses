import { describe, expect, it, vi, beforeEach } from 'vitest'
import { renderToString } from 'react-dom/server'
import { StaticRouter } from 'react-router-dom/server'
import { ScriptDoctorWorkbench } from './ScriptDoctorWorkbench'

beforeEach(() => {
  vi.restoreAllMocks()
})

describe('ScriptDoctorWorkbench', () => {
  it('renders the workbench heading', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(
      new Response(JSON.stringify([]), { status: 200 }),
    )

    const html = renderToString(
      <StaticRouter location="/script-doctor">
        <ScriptDoctorWorkbench />
      </StaticRouter>,
    )
    expect(html).toContain('Script Doctor Workbench')
  })

  it('renders textarea for script input', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(
      new Response(JSON.stringify([]), { status: 200 }),
    )

    const html = renderToString(
      <StaticRouter location="/script-doctor">
        <ScriptDoctorWorkbench />
      </StaticRouter>,
    )
    expect(html).toContain('textarea')
    expect(html).toContain('Paste your Fountain')
  })

  it('renders consultation button', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(
      new Response(JSON.stringify([]), { status: 200 }),
    )

    const html = renderToString(
      <StaticRouter location="/script-doctor">
        <ScriptDoctorWorkbench />
      </StaticRouter>,
    )
    expect(html).toContain('Start Consultation')
  })
})
