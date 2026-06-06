import { useState, useEffect } from 'react'
import { fetchStudies, type StudySummary } from '../api/client'

export default function DiagnosticRunner() {
  const [studies, setStudies] = useState<StudySummary[]>([])
  const [selectedStudy, setSelectedStudy] = useState<string>('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchStudies()
      .then(setStudies)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return <div className="loading">Loading...</div>
  }

  if (error) {
    return <div className="error">{error}</div>
  }

  return (
    <div className="diagnostic-runner">
      <h2>Diagnostic Runner</h2>
      <p>
        Run diagnostic tests against your narrative using frameworks from our 14 studies.
        Each framework provides specific questions to evaluate structural integrity.
      </p>

      <div className="diagnostic-form">
        <h3>Select Framework</h3>
        <select
          value={selectedStudy}
          onChange={(e) => setSelectedStudy(e.target.value)}
        >
          <option value="">Choose a framework...</option>
          {studies.map((study) => (
            <option key={study.id} value={study.id}>
              {study.creator} ({study.question_count} questions)
            </option>
          ))}
        </select>

        {selectedStudy && (
          <div className="framework-info">
            <p>
              Selected: <strong>{studies.find((s) => s.id === selectedStudy)?.creator}</strong>
            </p>
            <p>
              This framework has{' '}
              {studies.find((s) => s.id === selectedStudy)?.question_count} diagnostic questions.
            </p>
          </div>
        )}
      </div>

      <div className="diagnostic-info">
        <h3>How Diagnostics Work</h3>
        <p>
          Each study provides diagnostic questions designed to evaluate whether a narrative
          meets the principles established by that creator's work. Common diagnostics include:
        </p>
        <ul>
          <li>
            <strong>Causal Binding</strong> - Tests whether scenes connect through
            BUT/THEREFORE (strong) or AND THEN (weak)
          </li>
          <li>
            <strong>Reorderability</strong> - Tests whether scenes could be reordered
            without breaking the narrative
          </li>
          <li>
            <strong>Necessity</strong> - Tests whether every scene is essential
          </li>
          <li>
            <strong>Information Economy</strong> - Tests efficient information delivery
          </li>
        </ul>

        <h3>Available Framework Diagnostics</h3>
        <div className="framework-list">
          {studies.slice(0, 5).map((study) => (
            <div key={study.id} className="framework-item">
              <strong>{study.creator}</strong>
              <span className="category">{study.category}</span>
              <span className="count">{study.question_count} questions</span>
            </div>
          ))}
          {studies.length > 5 && (
            <p className="more">And {studies.length - 5} more frameworks...</p>
          )}
        </div>
      </div>

      <div className="diagnostic-note">
        <h3>Note</h3>
        <p>
          Full diagnostic analysis requires a completed script analysis. Upload your script
          to the analyzer first, then run diagnostics against the analysis results.
        </p>
        <p>
          For now, explore the diagnostic questions available in each framework to understand
          what criteria your narrative should meet.
        </p>
      </div>
    </div>
  )
}
