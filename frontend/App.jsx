import { useState } from "react";

function App() {
  const [contract, setContract] = useState("");
  const [result, setResult] = useState("");

  const submit = async () => {
    const res = await fetch("https://intelligent-contract-five.vercel.app/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ contract }),
    });

    const data = await res.json();
    setResult(JSON.stringify(data));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🚀 Intelligent Contract UI</h1>

      <textarea
        rows="5"
        cols="50"
        onChange={(e) => setContract(e.target.value)}
      />

      <br />
      <button onClick={submit}>Submit</button>

      <pre>{result}</pre>
    </div>
  );
}

export default App;