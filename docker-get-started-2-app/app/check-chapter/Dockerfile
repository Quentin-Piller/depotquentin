FROM python:3.9-slim

WORKDIR /app

COPY script/check-chapter.py /app

RUN pip install requests

CMD ["python", "check-chapter.py"]