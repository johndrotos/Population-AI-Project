import React, {useState, useEffect} from 'react'

function App() {
  const [data, setData] = useState({})
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    console.log('useEffect is running')
    fetch('/home')
      .then(res => {
        console.log('Got response:', res)
        console.log('Response status:', res.status)
        console.log('Response ok?:', res.ok)
        return res.json()
      })
      .then(data => {
        console.log('Parsed data:', data)
        setData(data)
        setLoading(false)
      })
      .catch(error => {
        console.error('Error occurred:', error)
        setLoading(false)
      })
  }, [])

  if (loading) return <div>Loading...</div>

  return (
    <div>
      <h1>{data.title}</h1>
    </div>
  )
}

export default App