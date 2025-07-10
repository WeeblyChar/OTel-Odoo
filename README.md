# OpenTelemetry Collector Module for Odoo

## Module Location
The module is located in the folder:  
`inDevModules/OpenTelemetry_Collector`

## What It Does
This module integrates OpenTelemetry with Odoo to enable tracing, metrics, and logging collection.  
It helps monitor Odoo operations by exporting telemetry data to your observability stack (e.g., Prometheus, Loki, Grafana).

## How to Install the Module

1. Copy or clone the module folder `OpenTelemetry_Collector` into your Odoo addons directory, e.g.,  
   `addons/inDevModules/OpenTelemetry_Collector`

2. Update your Odoo configuration (`odoo.conf`) to include the custom addons path if not already done:  

3. Restart your Odoo server to detect the new module.

4. In Odoo, go to **Apps**, click on the **Update Apps List** menu to refresh the module list.

5. Search for **OpenTelemetry Collector** and click **Install**.

## Docker Setup

All Docker-related files and configurations required to run Odoo with OpenTelemetry and observability tools are located inside the `docker` folder. This includes:

- `docker-compose.yml` to orchestrate Odoo, PostgreSQL, OpenTelemetry Collector, Prometheus, Loki, Grafana, and optionally Tempo.
- Dockerfiles for building custom Odoo images with OpenTelemetry instrumentation.
- Configuration files for OpenTelemetry Collector, Prometheus, Loki, Grafana dashboards, etc.

Before running, review and adjust the configurations (e.g., ports, volume mounts, environment variables) inside this folder to fit your environment.

Start the stack by running:

```bash
docker compose up -d
```

This will launch all services and make Odoo accessible on http://localhost:8069 by default.

Ensure your observability tools (Prometheus, Loki, Grafana, Tempo) are properly configured to receive and display telemetry data from Odoo via the OpenTelemetry Collector.

## Important Notes / Things to Pay Attention To

- Ensure your OpenTelemetry Collector and related observability tools (e.g., Prometheus, Loki) are properly configured and running, so the telemetry data can be received and visualized.

- The module requires compatible Odoo version (tested on Odoo 17). Using it on other versions may cause issues.

- Configuration for OpenTelemetry endpoints and exporters may require additional setup in your Odoo config or environment variables.

- When upgrading Odoo or this module, verify compatibility and test in a staging environment first.

- Monitor the performance impact of telemetry collection, especially on production systems.

---

If you encounter any issues or have questions, please contact the module maintainer.
