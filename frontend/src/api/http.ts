const API_URL = "http://127.0.0.1:8000";

export function authHeaders() {
  const token = localStorage.getItem("access_token");
  return token
    ? { Authorization: `Bearer ${token}` }
    : {};
}

export async function apiFetch<T>(
  path: string,
  options: RequestInit = {}
): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...authHeaders(),
      ...options.headers,
    },
  });

  if (!res.ok) {
    throw new Error(await res.text());
  }

  return res.json();
}
