export function getLastUpdated<T extends { updated_at: string }>(
  data: T[]
): string | null {
  if (!data.length) return null;

  const latest = data.reduce((max, item) =>
    new Date(item.updated_at) > new Date(max.updated_at) ? item : max
  );

  return new Date(latest.updated_at).toLocaleString();
}
