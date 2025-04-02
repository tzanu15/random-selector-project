import { useEffect, useState } from "react";
import { getHelloMessage } from "../services/api";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
  getHelloMessage()
    .then(setMessage)
    .catch(() => setMessage("Eroare la fetch!"));
}, []);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white shadow-xl rounded-xl p-8 text-center">
        <h1 className="text-2xl font-bold text-blue-600 mb-4">Hello from Django 👋</h1>
        <p className="text-lg text-gray-700">{message}</p>
      </div>
    </div>
  );
}

export default App;
