{
    'name': 'Open Telemetry Monitoring Module',
    'version': '1.0',
    'summary': 'Integrates Custom Open Telemetry Configuration for Odoo.',
    'description': """
                    Integrates custom Open Telemetry configuration for Odoo.
                    This module uses Grafana Loki (logs), Prometheus (metrics) and Grafana (Visualization).
                    You can access metrics by going into Developer Mode and go to Settings -> Technical -> Metrics. It should be listed under Resources.
                    Meaning you can add more metrics in case you need more informations regarding the system.
                   """,
    'author': 'None',
    'depends': ['base', 'resource', 'bus'],
    'installable': True,
    'application': False,
    'category': 'OpenTelemetry Collector/',
    'data': [
        'views/ir_metric.xml',
        'security/ir.model.access.csv',
        'data/config_parameters.xml',
        'data/ir_metric.xml',
    ],
    'external_dependencies':{
      'python': [
        'opentelemetry-exporter-otlp',
        'opentelemetry-instrumentation-logging',
        'prometheus_client',
      ],
    },
    'license': 'AGPL-3',
}
