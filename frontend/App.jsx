import { useState } from "react";

function App() {
  const [contract, setContract] = useState("");
  const [result, setResult] = useState("");

  const submit = async () => {
    try {
      const res = await fetch("https://intelligent-contract-five.vercel.app/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ contract }),
      });

      const data = await res.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (err) {
      setResult("Error calling API");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🚀 Intelligent Contract UI</h1>

      <textarea
        rows="6"
        cols="60"
        placeholder="Paste contract here..."
        value={contract}
        onChange={(e) => setContract(e.target.value)}
      />

      <br /><br />

      <button onClick={submit}>Analyze</button>

      <pre>{result}</pre>
    </div>
  );
}

export default App;