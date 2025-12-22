import { apiGet } from "./client";
import type { CoveredCall } from "../types/coveredCall";

export interface CoveredCallsQuery {
  ticker?: string;
  contract?: string;
  limit?: number;
  offset?: number;
}

export function fetchCoveredCalls(
  params: CoveredCallsQuery = {}
): Promise<CoveredCall[]> {
  const query = new URLSearchParams();

  if (params.ticker) query.append("ticker", params.ticker);
  if (params.contract) query.append("contract", params.contract);
  if (params.limit !== undefined) query.append("limit", params.limit.toString());
  if (params.offset !== undefined) query.append("offset", params.offset.toString());

  const qs = query.toString();
  const endpoint = qs ? `/covered-calls?${qs}` : "/covered-calls";

  return apiGet<CoveredCall[]>(endpoint);
}
