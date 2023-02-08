FROM python:3.10-slim-bullseye
COPY . .
WORKDIR /
RUN pip install -r requirements.txt --disable-pip-version-check
RUN python3 scripts/get_tables.py
CMD [ "python3", "-m", "mnemosym.bot" ]
