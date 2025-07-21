# Use the official Odoo image as the base (can change depending on the Odoo version).
FROM odoo:17.0

# Set as root to install dependencies.
USER root

# Install OpenTelemetry dependencies in a clean environment
RUN pip config set global.break-system-packages true && \
    pip install --no-cache-dir \
    prometheus-client \
    opentelemetry-instrumentation-logging \
    opentelemetry-exporter-otlp && \
    rm ~/.config/pip/pip.conf
    
# Entrypoint
COPY entrypoint.py /usr/bin/odoo-entrypoint.py
RUN chmod +x /usr/bin/odoo-entrypoint.py

RUN ln -sf /usr/bin/python3.10 /usr/bin/python3
RUN ln -sf /usr/bin/python3.10 /bin/python3

RUN apt update && apt install -y curl \
    && curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.8.7/grpcurl_1.8.7_linux_x86_64.tar.gz | tar -xz \
    && mv grpcurl /usr/local/bin/ \
    && chmod +x /usr/local/bin/grpcurl

# Switch back to user
USER odoo

# ENTRYPOINT ["opentelemetry-instrument", "--traces_exporter", "otlp", "--metrics_exporter", "none", "--logs_exporter", "otlp", "--", "python3", "/usr/bin/odoo-entrypoint.py"]
ENTRYPOINT ["python3", "/usr/bin/odoo-entrypoint.py"]