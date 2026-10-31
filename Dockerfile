FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY copilot_sommelier_caviste/ ./copilot_sommelier_caviste/
RUN pip install --no-cache-dir .
EXPOSE 8000
CMD ["uvicorn", "copilot_sommelier_caviste.entrypoints.fastapi_router:app", "--host", "0.0.0.0", "--port", "8000"]
