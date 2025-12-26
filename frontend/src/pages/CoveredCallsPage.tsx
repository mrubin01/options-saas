import { useEffect, useState } from "react";
import OptionsFilters from "../components/OptionsFilters";
import OptionsTable from "../components/OptionsTable";
import { fetchCoveredCalls } from "../api/coveredCalls";
import type { OptionsFilters as Filters } from "../types/filters";
import type { CoveredCall } from "../types/coveredCall";
import { EXCHANGES } from "../constants/exchanges";

const exchangeMap: Record<number, string> = Object.fromEntries(
  EXCHANGES.map((e) => [e.id, e.name])
);

export default function CoveredCallsPage() {
  const [filters, setFilters] = useState<Filters>({});
  const [data, setData] = useState<CoveredCall[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
  setLoading(true);
  setError(null);

  fetchCoveredCalls(filters)
    .then(setData)
    .catch(() => setError("Failed to load covered calls"))
    .finally(() => setLoading(false));
}, [filters]);

  // RENDER: JSX returned to the browser
  return (
    <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
      <h2>Covered Calls</h2>

      <OptionsFilters
        filters={filters}
        onChange={setFilters}
        exchanges={EXCHANGES}
      />

      {loading && <p>Loading...</p>}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {!loading && !error && data.length === 0 && (
        <p>No results found</p>
      )}

      {!loading && !error && data.length > 0 && (
        <OptionsTable data={data} exchangeMap={exchangeMap} />
      )}
    </div>
  );
}
