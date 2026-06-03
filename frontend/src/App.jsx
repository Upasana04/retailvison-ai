import { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function App() {
  const [metrics, setMetrics] = useState({});
  const [heatmap, setHeatmap] = useState([]);
  const [funnel, setFunnel] = useState({});
  const [anomalies, setAnomalies] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/metrics")
      .then(res => setMetrics(res.data));

    axios.get("http://127.0.0.1:8000/heatmap")
      .then(res => {
        const data = res.data.zone_activity.map(
          item => ({
            zone: item[0],
            count: item[1]
          })
        );
        setHeatmap(data);
      });

    axios.get("http://127.0.0.1:8000/funnel")
      .then(res => setFunnel(res.data));

    axios.get("http://127.0.0.1:8000/anomalies")
      .then(res => setAnomalies(res.data.suspicious_visitors));

    axios.get("http://127.0.0.1:8000/events")
      .then(res => setEvents(res.data.events));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>RetailVision AI Dashboard</h1>

      <hr />

      <h2>Metrics</h2>

      <p>Total Visitors: {metrics.total_visitors}</p>
      <p>Entries: {metrics.entries}</p>
      <p>Zone Transitions: {metrics.zone_transitions}</p>

      <hr />

      <h2>Heatmap</h2>

      <BarChart
        width={700}
        height={300}
        data={heatmap}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="zone" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" />
      </BarChart>

      <hr />

      <h2>Conversion Funnel</h2>

      <p>Entries: {funnel.entries}</p>

      <p>
        Cash Counter Visitors:
        {funnel.cash_counter_visitors}
      </p>

      <p>
        Conversion Rate:
        {funnel.conversion_rate}%
      </p>

      <hr />

      <h2>Anomaly Detection</h2>

      {anomalies.map((a, index) => (
        <div key={index}>
          Visitor {a[0]} → {a[1]} events
        </div>
      ))}

      <hr />

      <h2>Recent Events</h2>

      {events.slice(0, 20).map((e, index) => (
        <div key={index}>
          {e[0]} | {e[1]} | {e[2]}
        </div>
      ))}
    </div>
  );
}

export default App;