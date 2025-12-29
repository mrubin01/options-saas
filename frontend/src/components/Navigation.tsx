import { Link } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export default function Navigation() {
  const { user, logout } = useAuth();

  if (!user) return null;

  return (
    <nav>
      <span>{user.email}</span>

      <Link to="/covered-calls">Covered Calls</Link>
      <Link to="/put-options">Put Options</Link>
      <Link to="/spread-options">Spread Options</Link>

      <button onClick={logout}>Logout</button>
    </nav>
  );
}
