FROM python:3.9-slim-buster
COPY . .
WORKDIR /
RUN pip install -r requirements.txt --disable-pip-version-check
RUN python3 scripts/get_tables.py
CMD [ "python3", "-m", "mnemosym.bot" ]
