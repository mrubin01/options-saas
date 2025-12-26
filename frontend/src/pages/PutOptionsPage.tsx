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

  useEffect(() => {
    fetchPutOptions(filters).then(setData);
  }, [filters]);

  return (
    <>
      <h2>Put Options</h2>

      <OptionsFilters
        filters={filters}
        onChange={setFilters}
        exchanges={EXCHANGES}
      />

      <OptionsTable data={data} exchangeMap={exchangeMap} />
    </>
  );
}
