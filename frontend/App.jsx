import { useState, useEffect } from "react";

function App() {
  const [owner, setOwner] = useState("");
  const [tokens, setTokens] = useState([]);

  const API_URL = "https://intelligent-contract.onrender.com"; // backend local

  const fetchTokens = async () => {
    try {
      const res = await fetch(`${API_URL}/tokens`);
      const data = await res.json();
      setTokens(data);
    } catch (err) {
      console.error("Failed to fetch tokens:", err);
    }
  };

  const mintToken = async () => {
    if (!owner) return;
    try {
      await fetch(`${API_URL}/mint`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ owner }),
      });
      setOwner("");
      fetchTokens();
    } catch (err) {
      console.error("Mint failed:", err);
    }
  };

  useEffect(() => {
    fetchTokens();
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Intelligent Contract Demo</h1>
      <input
        type="text"
        placeholder="Owner name"
        value={owner}
        onChange={(e) => setOwner(e.target.value)}
      />
      <button onClick={mintToken} style={{ marginLeft: 10 }}>
        Mint Token
      </button>

      <h2>Tokens List</h2>
      <ul>
        {tokens.map((t) => (
          <li key={t.token_id}>
            ID: {t.token_id}, Owner: {t.owner}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;