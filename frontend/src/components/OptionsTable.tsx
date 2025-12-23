import type { CoveredCall } from "../types/coveredCall";

interface OptionsTableProps {
  data: CoveredCall[];
  exchangeMap: Record<number, string>;
}

export default function OptionsTable({
  data,
  exchangeMap,
}: OptionsTableProps) {
  if (data.length === 0) {
    return <p>No results found.</p>;
  }

  return (
    <table border={1} cellPadding={6} cellSpacing={0}>
      <thead>
        <tr>
          <th>Contract</th>
          <th>Ticker</th>
          <th>Exchange</th>
          <th>Expiry</th>
          <th>Current</th>
          <th>Strike</th>
        </tr>
      </thead>
      <tbody>
        {data.map((row) => (
          <tr key={row.contract}>
            <td>{row.contract}</td>
            <td>{row.ticker}</td>
            <td>{exchangeMap[row.exchange] ?? row.exchange}</td>
            <td>{row.expiry_date}</td>
            <td>{row.current_price}</td>
            <td>{row.strike_price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
