import { apiGet } from "./client";
import type { CoveredCall } from "../types/coveredCall";

export interface CoveredCallsQuery {
  ticker?: string;
  expiry_date?: string;
  contract?: string;
  exchange?: number;
  limit?: number;
  offset?: number;
}

export function fetchCoveredCalls(
  params: CoveredCallsQuery = {}
): Promise<CoveredCall[]> {
  const query = new URLSearchParams();

  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== "") {
      query.append(key, String(value));
    }
  });

  const qs = query.toString();
  return apiGet<CoveredCall[]>(
    qs ? `/covered-calls?${qs}` : "/covered-calls"
  );
}
