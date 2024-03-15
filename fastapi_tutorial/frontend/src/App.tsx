import { useState } from 'react'
import './App.css'
import './components/TodoCard'
import Todo from './components/Todo'
import TodoCard from './components/TodoCard'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1> Hello World!</h1>
      <Todo />
      <TodoCard />
    </>
  )
}

export default App
