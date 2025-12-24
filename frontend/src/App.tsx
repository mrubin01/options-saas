import { Routes, Route, Navigate } from "react-router-dom";
import CoveredCallsPage from "./pages/CoveredCallsPage";
import PutOptionsPage from "./pages/PutOptionsPage";
import Navigation from "./components/Navigation";

function App() {
  return (
    <>
      <Navigation />

      <Routes>
        <Route path="/" element={<Navigate to="/covered-calls" />} />
        <Route path="/covered-calls" element={<CoveredCallsPage />} />
        <Route path="/put-options" element={<PutOptionsPage />} />
      </Routes>
    </>
  );
}

export default App;
