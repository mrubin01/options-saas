import { useEffect, useState } from "react";
import OptionsFilters from "../components/OptionsFilters";
import { fetchSpreadOptions } from "../api/spreadOptions";
import type { SpreadOption } from "../types/spreadOption";
import type { OptionsFilters as Filters } from "../types/filters";
import OptionsTable from "../components/OptionsTable";
import { EXCHANGES } from "../constants/exchanges";
import { getLastUpdated } from "../utils/lastUpdated";

const exchangeMap: Record<number, string> = Object.fromEntries(
  EXCHANGES.map((e) => [e.id, e.name])
);

export default function SpreadOptionsPage() {
  const [filters, setFilters] = useState<Filters>({});
  const [data, setData] = useState<SpreadOption[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
  setLoading(true);
  setError(null);

  fetchSpreadOptions(filters)
    .then(setData)
    .catch(() => setError("Failed to load spread options"))
    .finally(() => setLoading(false));
}, [filters]);

  const lastUpdated = getLastUpdated(data);

  // RENDER: JSX returned to the browser
  return (
    <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
      <h2 className="text-xl font-semibold mb-4">
        Best Spread Options
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
