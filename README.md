# OpenTelemetry Collector Module for Odoo

## 📦 What This Module Does

This module enables **metrics and logging export** from Odoo to OpenTelemetry-compatible observability stacks (such as **Prometheus**, **Loki**, and **Grafana**).

It provides:

- System & Odoo-specific **metrics** exposed at `/metrics`
- Structured **logs** forwarded via OpenTelemetry
- Built-in integration points for custom instrumentation

Useful for developers, devops, and observability engineers looking to monitor, debug, or analyze Odoo instances.

---

## ✅ How to Install the Module

1. Copy or clone the module folder `OpenTelemetry_Collector` into your Odoo **addons path**, e.g.:

2. Ensure the `addons_path` in your `odoo.conf` includes the path to `inDevModules`.

3. Restart your Odoo server.

4. In the Odoo UI:
- Go to **Apps**
- Click **Update Apps List**
- Search for `OpenTelemetry Collector`
- Click **Install**

> 💡 That’s it! No CLI install or extra setup needed inside Odoo.

---

## ⚙️ Developer Notes & Configuration

Before using or extending this module:

- **Check the `example.env` file** in this repo. It contains all key environment variables (e.g., OpenTelemetry endpoints, ports, exporters).
- **You should copy and rename it to `.env`**, and adjust the values to match your setup (especially OTEL collector addresses).
- **Avoid hardcoding** values inside the Python code – this module respects `.env` and `os.getenv()` settings.

### ⚠️ Developers Should Pay Attention To:

- `OTEL_COLLECTOR_ENDPOINT`, `OTEL_COLLECTOR_GRPC_PORT`, `OTEL_COLLECTOR_HTTP_PORT` — must align with your actual OpenTelemetry Collector.
- Logging and metrics will silently fail if the collector is unreachable or misconfigured.
- You **can extend** this module to add tracing, custom metrics, or hook into specific business logic.

---

## 🐳 Docker Support (Optional)

If you're deploying your observability stack via Docker, see the provided `docker/` folder:

- Includes `docker-compose.yml`, OpenTelemetry Collector config, Prometheus, Loki, Grafana setup.
- To start:
```bash
docker compose up -d
