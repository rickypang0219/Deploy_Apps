import React, { useEffect, useState } from 'react';

interface Todo {
  id: number;
  content: string;
  finished: boolean;
}

function TodoCard({ todo }: { todo: Todo }): JSX.Element {
  return (
    <div>
      <h3>Todo ID: {todo.id}</h3>
      <p>Title: {todo.content}</p>
      <p>Completed: {todo.finished ? 'Yes' : 'No'}</p>
    </div>
  );
}

function DataFetcher(): JSX.Element {
  const [todos, setTodos] = useState<Todo[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://cors-anywhere.herokuapp.com/http://127.0.0.1:8000');
        const jsonTodos: Todo[] = await response.json();
        setTodos(jsonTodos);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {todos.length > 0 ? (
        todos.map((todo) => <TodoCard key={todo.id} todo={todo} />)
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
}

export default DataFetcher;