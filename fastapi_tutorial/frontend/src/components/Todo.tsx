import React, { useState, useEffect } from 'react';

interface Item {
  id: number;
  content: string;
  finished: boolean;
}

function MyComponent(): JSX.Element {
  const [data, setData] = useState<Item[]>([]);

  useEffect(() => {
    // Fetch data from the API
    fetch('http://127.0.0.1:8000')
      .then((response) => response.json())
      .then((apiData: Item[]) => {
        // Store the API response data in the state variable
        setData(apiData);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      {data.length > 0 ? (
        <ul>
          {data.map((item) => (
            <li key={item.id}>{item.content}</li>
          ))}
        </ul>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
}

export default MyComponent;