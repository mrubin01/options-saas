import { useEffect, useState } from "react";
import { fetchCoveredCalls } from "../api/coveredCalls";
import type { CoveredCall } from "../types/coveredCall";

export default function CoveredCallsPage() {
  const [data, setData] = useState<CoveredCall[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchCoveredCalls({ limit: 20 })
      .then(setData)
      .catch((err) => {
        console.error(err);
        setError("Failed to load covered calls");
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading covered calls...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>Best Covered Calls</h1>

      <table border={1} cellPadding={6} cellSpacing={0}>
        <thead>
          <tr>
            <th>Contract</th>
            <th>Ticker</th>
            <th>Exchange</th>
            <th>Expiry</th>
            <th>Current Price</th>
            <th>Strike Price</th>
          </tr>
        </thead>
        <tbody>
          {data.map((cc) => (
            <tr key={cc.contract}>
              <td>{cc.contract}</td>
              <td>{cc.ticker}</td>
              <td>{cc.exchange}</td>
              <td>{cc.expiry_date}</td>
              <td>{cc.current_price}</td>
              <td>{cc.strike_price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
