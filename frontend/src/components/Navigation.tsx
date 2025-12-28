import { useAuth } from "../auth/AuthContext";
import { Link } from "react-router-dom";


export default function Navigation() {
  const { token, logout } = useAuth();

  if (!token) return null;

  return (
    <nav>
      <Link to="/covered-calls">Covered Calls</Link>
      <Link to="/put-options">Put Options</Link>
      <Link to="/spread-options">Spreads</Link>

      <button onClick={logout}>Logout</button>
    </nav>
  );
}
