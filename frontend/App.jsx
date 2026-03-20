import { useState } from "react";

const API = "https://intelligent-contract-five.vercel.app/api";

function App() {
  const [contract, setContract] = useState("");
  const [result, setResult] = useState("");
  const [history, setHistory] = useState([]);

  const callAPI = async (endpoint) => {
    try {
      const res = await fetch(`${API}/${endpoint}`, {
        method: endpoint === "history" ? "GET" : "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: endpoint === "history" ? null : JSON.stringify({ contract }),
      });

      const data = await res.json();

      if (endpoint === "history") {
        setHistory(data.history);
      } else {
        setResult(JSON.stringify(data, null, 2));
      }
    } catch (err) {
      setResult("❌ Error calling API");
    }
  };

  return (
    <div style={{ padding: 30, fontFamily: "Arial" }}>
      <h1>🚀 Intelligent Contract AI</h1>

      <textarea
        rows="6"
        style={{ width: "100%" }}
        placeholder="Paste your smart contract here..."
        value={contract}
        onChange={(e) => setContract(e.target.value)}
      />

      <br /><br />

      <button onClick={() => callAPI("submit")}>📤 Submit</button>
      <button onClick={() => callAPI("verify")} style={{ marginLeft: 10 }}>
        🔍 Verify
      </button>
      <button onClick={() => callAPI("history")} style={{ marginLeft: 10 }}>
        📜 History
      </button>

      <h3>📊 Result:</h3>
      <pre>{result}</pre>

      <h3>📚 History:</h3>
      <pre>{JSON.stringify(history, null, 2)}</pre>
    </div>
  );
}

export default App;