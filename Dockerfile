FROM python:3.13.5-slim-bookworm
RUN useradd -m dockeruser
USER dockeruser
WORKDIR /home/dockeruser/bot
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip; pip install --no-cache-dir -r ./requirements.txt
COPY ./data ./data
COPY ./src ./src
CMD ["python", "-m", "src"]
