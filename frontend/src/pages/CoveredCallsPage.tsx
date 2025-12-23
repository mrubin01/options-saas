import { useEffect, useState } from "react";
import { fetchCoveredCalls } from "../api/coveredCalls";
import type { CoveredCall } from "../types/coveredCall";

const PAGE_SIZE = 10;

const EXCHANGES = [
  { id: 0, name: "NYSE" },
  { id: 1, name: "NASDAQ" },
  { id: 2, name: "ARCA" },
];

const EXCHANGE_MAP: Record<number, string> = {
  0: "NYSE",
  1: "NASDAQ",
  2: "ARCA",
};

export default function CoveredCallsPage() {
  const [data, setData] = useState<CoveredCall[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Filters
  const [ticker, setTicker] = useState("");
  const [contract, setContract] = useState("");
  const [expiryDate, setExpiryDate] = useState("");
  const [exchange, setExchange] = useState("");

  // Pagination
  const [offset, setOffset] = useState(0);

  useEffect(() => {
    setLoading(true);
    setError(null);

    fetchCoveredCalls({
      ticker,
      contract,
      expiry_date: expiryDate,
      exchange: exchange ? Number(exchange) : undefined,
      limit: PAGE_SIZE,
      offset,
    })
      .then(setData)
      .catch(() => setError("Failed to load data"))
      .finally(() => setLoading(false));
  }, [ticker, contract, expiryDate, exchange, offset]);

  return (
    <div>
      <h1>Best Covered Calls</h1>

      {/* Filters */}
      <div style={{ marginBottom: "1rem" }}>
        <input
          placeholder="Ticker"
          value={ticker}
          onChange={(e) => {
            setOffset(0);
            setTicker(e.target.value.toUpperCase());
          }}
        />

        <input
          placeholder="Contract"
          value={contract}
          onChange={(e) => {
            setOffset(0);
            setContract(e.target.value.toUpperCase());
          }}
        />

        <input
          type="date"
          value={expiryDate}
          onChange={(e) => {
            setOffset(0);
            setExpiryDate(e.target.value);
          }}
        />

        <select
          value={exchange}
          onChange={(e) => {
            setOffset(0);
            setExchange(e.target.value);
          }}
        >
          <option value="">All Exchanges</option>
          {EXCHANGES.map((ex) => (
            <option key={ex.id} value={ex.id}>
              {ex.name}
            </option>
          ))}
        </select>

      </div>

      {/* Table */}
      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}

      {!loading && !error && (
        <table border={1} cellPadding={6}>
          <thead>
            <tr>
              <th>Ticker</th>
              <th>Contract</th>
              <th>Exchange</th>
              <th>Expiry</th>
              <th>Current</th>
              <th>Strike</th>
            </tr>
          </thead>
          <tbody>
            {data.map((cc) => (
              <tr key={cc.contract}>
                <td>{cc.ticker}</td>
                <td>{cc.contract}</td>
                <td>{EXCHANGE_MAP[cc.exchange] ?? cc.exchange}</td>
                <td>{cc.expiry_date}</td>
                <td>{cc.current_price}</td>
                <td>{cc.strike_price}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* Pagination */}
      <div style={{ marginTop: "1rem" }}>
        <button
          onClick={() => setOffset(Math.max(0, offset - PAGE_SIZE))}
          disabled={offset === 0}
        >
          Previous
        </button>

        <button
          onClick={() => setOffset(offset + PAGE_SIZE)}
          disabled={data.length < PAGE_SIZE}
        >
          Next
        </button>
      </div>
    </div>
  );
}
