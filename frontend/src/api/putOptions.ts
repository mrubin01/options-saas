import { apiGet } from "./client";
import type { PutOption } from "../types/putOption";

export interface PutOptionsQuery {
  ticker?: string;
  expiry_date?: string;
  contract?: string;
  exchange?: number;
  limit?: number;
  offset?: number;
}

export function fetchPutOptions(
  params: PutOptionsQuery = {}
): Promise<PutOption[]> {
  const query = new URLSearchParams();

  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== "") {
      query.append(key, String(value));
    }
  });

  const qs = query.toString();
  return apiGet<PutOption[]>(
    qs ? `/put-options?${qs}` : "/put-options"
  );
}
