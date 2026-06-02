import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [metrics, setMetrics] = useState({});
  const [funnel, setFunnel] = useState({});
  const [events, setEvents] = useState([]);
  const [heatmap, setHeatmap] = useState([]);
  const [anomalies, setAnomalies] = useState([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const metricsRes = await axios.get("http://127.0.0.1:8000/metrics");
      const funnelRes = await axios.get("http://127.0.0.1:8000/funnel");
      const eventsRes = await axios.get("http://127.0.0.1:8000/events");
      const heatmapRes = await axios.get("http://127.0.0.1:8000/heatmap");
      const anomalyRes = await axios.get("http://127.0.0.1:8000/anomalies");

      setMetrics(metricsRes.data);
      setFunnel(funnelRes.data);
      setEvents(eventsRes.data.events || []);
      setHeatmap(heatmapRes.data.zone_activity || []);
      setAnomalies(anomalyRes.data.suspicious_visitors || []);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>RetailVision AI Dashboard</h1>

      <div style={{ display: "flex", gap: "20px" }}>
        <div style={{ border: "1px solid gray", padding: "10px" }}>
          <h3>Total Visitors</h3>
          <p>{metrics.total_visitors}</p>
        </div>

        <div style={{ border: "1px solid gray", padding: "10px" }}>
          <h3>Entries</h3>
          <p>{funnel.entries}</p>
        </div>

        <div style={{ border: "1px solid gray", padding: "10px" }}>
          <h3>Conversion Rate</h3>
          <p>{funnel.conversion_rate}%</p>
        </div>
      </div>

      <hr />

      <h2>Zone Activity</h2>

      {heatmap.map((item, index) => (
        <p key={index}>
          {item[0]} : {item[1]}
        </p>
      ))}

      <hr />

      <h2>Recent Events</h2>

      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Visitor</th>
            <th>Event</th>
            <th>Zone</th>
            <th>Timestamp</th>
          </tr>
        </thead>

        <tbody>
          {events.slice(0, 20).map((event, index) => (
            <tr key={index}>
              <td>{event[0]}</td>
              <td>{event[1]}</td>
              <td>{event[2]}</td>
              <td>{event[3]}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <hr />

      <h2>Anomaly Detection</h2>

      {anomalies.length === 0 ? (
        <p>No suspicious visitors found.</p>
      ) : (
        anomalies.map((visitor, index) => (
          <p key={index}>
            Visitor {visitor[0]} → {visitor[1]} events
          </p>
        ))
      )}
    </div>
  );
}

export default App;