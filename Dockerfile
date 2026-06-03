FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY sample_requirement.txt .
COPY tests/ tests/
COPY generator.py .

RUN useradd --create-home appuser
USER appuser

CMD ["python", "generator.py"]
