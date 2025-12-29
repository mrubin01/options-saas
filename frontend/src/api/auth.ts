const API_URL = "http://127.0.0.1:8000";
import { apiGet } from "./client";

export async function login(email: string, password: string) {
  const body = new URLSearchParams();
  body.append("username", email);
  body.append("password", password);

  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body,
  });

  if (!res.ok) {
    throw new Error("Invalid credentials");
  }

  return res.json(); // { access_token, token_type }
}

export type MeResponse = {
  id: number;
  email: string;
};

export function fetchMe(): Promise<MeResponse> {
  return apiGet<MeResponse>("/auth/me");
}

