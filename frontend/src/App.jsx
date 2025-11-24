import { useState } from 'react'

export default function App() {
  const [file, setFile] = useState(null)
  const [status, setStatus] = useState('Idle')
  const [downloadUrl, setDownloadUrl] = useState('')

  const handleSubmit = async e => {
    e.preventDefault()
    if (!file) return
    setStatus('Uploading...')
    const formData = new FormData()
    formData.append('file', file)
    try {
      const res = await fetch('http://localhost:8000/convert/pdf-to-text', {
        method: 'POST',
        body: formData
      })
      if (!res.ok) throw new Error('Conversion failed')
      const blob = await res.blob()
      setDownloadUrl(URL.createObjectURL(blob))
      setStatus('Done')
    } catch (err) {
      setStatus(err.message)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded shadow w-full max-w-md space-y-4"
      >
        <h1 className="text-xl font-semibold">File Converter</h1>
        <input
          type="file"
          onChange={e => setFile(e.target.files?.[0] ?? null)}
          className="block w-full text-sm"
        />
        <button
          type="submit"
          className="px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
          disabled={!file}
        >
          Convert
        </button>
        <div className="text-sm text-gray-600">Status: {status}</div>
        {downloadUrl && (
          <a
            href={downloadUrl}
            download="converted.txt"
            className="text-blue-600 text-sm underline"
          >
            Download result
          </a>
        )}
      </form>
    </div>
  )
}