FROM python:3.10-slim

RUN apt-get update && apt-get install curl -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR /bot/

ADD poetry.lock pyproject.toml ./

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/bot/"

RUN poetry install --no-root

COPY . .


ARG BOT_TOKEN
ENV TG_BOT_TOKEN=$BOT_TOKEN

CMD ["poetry", "run", "python3", "bot.py"]