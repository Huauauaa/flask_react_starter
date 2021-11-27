import { useState, useEffect } from 'react';
import logo from './logo.svg';

function App() {
  const [count, setCount] = useState(0);
  const [users, setUsers] = useState([]);
  useEffect(() => {
    (async () => {
      const response = await fetch('/api/users');
      const data = await response.json();
      setUsers(data);
    })();
  }, []);

  return (
    <div className="text-center">
      <header className="App-header bg-gray-800 min-h-screen flex flex-col items-center justify-center text-xl text-white">
        <img
          src={logo}
          className="text-center w-1/4 pointer-events-none animate-logo-spin"
          alt="logo"
        />
        <p>Hello Vite + React!</p>
        <p>
          <button
            type="button"
            onClick={() => setCount((count) => count + 1)}
            className="bg-white text-black  py-1 px-1 rounded"
          >
            count is: {count}
          </button>
        </p>
        <p>
          Edit <code>App.jsx</code> and save to test HMR updates.
        </p>
        <p>
          <a
            className="text-blue-500"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          {' | '}
          <a
            className="App-link"
            href="https://vitejs.dev/guide/features.html"
            target="_blank"
            rel="noopener noreferrer"
          >
            Vite Docs
          </a>
        </p>
      </header>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
