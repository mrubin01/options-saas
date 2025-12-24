import { NavLink } from "react-router-dom";

const linkStyle = {
  marginRight: "1rem",
  textDecoration: "none",
};


export default function Navigation() {
  return (
    <nav style={{ marginBottom: "1.5rem" }}>
      <NavLink
        to="/covered-calls"
        style={({ isActive }) => ({
          ...linkStyle,
          fontWeight: isActive ? "bold" : "normal",
        })}
      >
        Covered Calls
      </NavLink>

      <NavLink
        to="/put-options"
        style={({ isActive }) => ({
          ...linkStyle,
          fontWeight: isActive ? "bold" : "normal",
        })}
      >
        Put Options
      </NavLink>

      <NavLink
        to="/spread-options"
        style={({ isActive }) => ({
          ...linkStyle,
          fontWeight: isActive ? "bold" : "normal",
        })}
      >
        Spread Options
      </NavLink>

    </nav>
  );
}
