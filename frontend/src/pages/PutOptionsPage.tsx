import { useEffect, useState } from "react";
import { fetchPutOptions } from "../api/putOptions";
import type { PutOption } from "../types/putOption";
import OptionsTable from "../components/OptionsTable";

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

export default function PutOptionsPage() {
  const [data, setData] = useState<PutOption[]>([]);
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

    fetchPutOptions({
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
      <h1>Best Put Options</h1>

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
        <OptionsTable data={data} exchangeMap={EXCHANGE_MAP} />
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
