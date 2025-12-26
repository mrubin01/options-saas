import { useEffect, useState } from "react";
import OptionsFilters from "../components/OptionsFilters";
import { fetchSpreadOptions } from "../api/spreadOptions";
import type { SpreadOption } from "../types/spreadOption";
import type { OptionsFilters as Filters } from "../types/filters";
import OptionsTable from "../components/OptionsTable";
import { EXCHANGES } from "../constants/exchanges";

const exchangeMap: Record<number, string> = Object.fromEntries(
  EXCHANGES.map((e) => [e.id, e.name])
);

export default function SpreadOptionsPage() {
  const [filters, setFilters] = useState<Filters>({});
  const [data, setData] = useState<SpreadOption[]>([]);

  useEffect(() => {
    fetchSpreadOptions(filters).then(setData);
  }, [filters]);

  return (
    <>
      <h2>Spread Options</h2>

      <OptionsFilters
        filters={filters}
        onChange={setFilters}
        exchanges={EXCHANGES}
      />

      <OptionsTable data={data} exchangeMap={exchangeMap} />
    </>
  );
}
