import React, { useEffect, useState } from 'react';

function MyComponent(): JSX.Element {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/welcome'); // Replace with your API endpoint

        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }

        const json = await response.json();
        setData(json);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <p>Loading data...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div>
      <h3>Data:</h3>
      <p>ID: {data.id}</p>
      <p>Content: {data.content}</p>
      <p>Finished: {data.finished ? 'Yes' : 'No'}</p>
    </div>
  );
}

export default MyComponent;