FROM continuumio/miniconda3
WORKDIR /
COPY . .
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "mnemosym", "/bin/bash", "-c"]
RUN python scripts/get_tables.py
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "mnemosym", "python", "-m", "mnemosym.bot"]
