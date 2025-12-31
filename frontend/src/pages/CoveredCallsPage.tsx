import { useEffect, useState } from "react";
import OptionsFilters from "../components/OptionsFilters";
import OptionsTable from "../components/OptionsTable";
import { fetchCoveredCalls } from "../api/coveredCalls";
import type { OptionsFilters as Filters } from "../types/filters";
import type { CoveredCall } from "../types/coveredCall";
import { EXCHANGES } from "../constants/exchanges";
import { getLastUpdated } from "../utils/lastUpdated";

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

  const lastUpdated = getLastUpdated(data);

  // RENDER: JSX returned to the browser
  return (
    <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
      <h2 className="text-xl font-semibold mb-4">
        Best Covered Calls
      </h2>

      {lastUpdated && (
        <div className="text-sm text-gray-500 mb-2">
          Last updated: {lastUpdated}
        </div>
      )}

      <OptionsFilters
        filters={filters}
        onChange={setFilters}
        exchanges={EXCHANGES}
      />

      {loading && <p>Loading...</p>}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {!loading && data.length === 0 && (
        <div className="text-sm text-gray-500 py-6">
          No results found.
        </div>
      )}

      {!loading && !error && data.length > 0 && (
        <OptionsTable data={data} exchangeMap={exchangeMap} />
      )}

      {loading && (
        <div className="text-sm text-gray-500 py-6">
          Loading results…
        </div>
      )}
    </div>
  );
}
