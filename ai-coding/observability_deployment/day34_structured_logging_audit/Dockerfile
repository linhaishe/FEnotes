FROM python:3.12-slim

WORKDIR /app

COPY observability_deployment/day34_structured_logging_audit/requirements-container.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY observability_deployment/day32_security_guardrails_hitl/demo.py /app/observability_deployment/day32_security_guardrails_hitl/demo.py
COPY observability_deployment/day34_structured_logging_audit/demo.py /app/observability_deployment/day34_structured_logging_audit/demo.py
COPY observability_deployment/day34_structured_logging_audit/audit_demo.py /app/observability_deployment/day34_structured_logging_audit/audit_demo.py

RUN useradd --uid 10001 --create-home appuser \
    && mkdir /data \
    && chown appuser:appuser /data
USER appuser

CMD ["uvicorn", "observability_deployment.day34_structured_logging_audit.demo:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
