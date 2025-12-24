import { apiGet } from "./client";
import type { SpreadOption } from "../types/spreadOption";

export interface SpreadOptionsQuery {
  ticker?: string;
  expiry_date?: string;
  contract?: string;
  exchange?: number;
  limit?: number;
  offset?: number;
}

export function fetchSpreadOptions(
  params: SpreadOptionsQuery = {}
): Promise<SpreadOption[]> {
  const query = new URLSearchParams();

  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== "") {
      query.append(key, String(value));
    }
  });

  const qs = query.toString();
  return apiGet<SpreadOption[]>(
    qs ? `/spread-options?${qs}` : "/spread-options"
  );
}
