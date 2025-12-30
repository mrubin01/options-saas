import { useEffect, useState } from "react";
import OptionsFilters from "../components/OptionsFilters";
import { fetchPutOptions } from "../api/putOptions";
import type { PutOption } from "../types/putOption";
import type { OptionsFilters as Filters } from "../types/filters";
import OptionsTable from "../components/OptionsTable";
import { EXCHANGES } from "../constants/exchanges";

const exchangeMap: Record<number, string> = Object.fromEntries(
  EXCHANGES.map((e) => [e.id, e.name])
);

export default function PutOptionsPage() {
  const [filters, setFilters] = useState<Filters>({});
  const [data, setData] = useState<PutOption[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
  setLoading(true);
  setError(null);

  fetchPutOptions(filters)
    .then(setData)
    .catch(() => setError("Failed to load put options"))
    .finally(() => setLoading(false));
}, [filters]);

  // RENDER: JSX returned to the browser
  return (
    <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
      <h2 className="text-xl font-semibold mb-4">
        Best Put Options
      </h2>

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

