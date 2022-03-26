"""
scripts/get_tables.py
~~~~~~~~~~~~~~~~~~~~~
script to download the data files from https://github.com/omniczech/vaarn-generators/tree/main/data
"""
import json

import requests
from tqdm import tqdm


def download_table(url: str, filepath: str):
    """makes a request to a url and downloads the text"""
    request = requests.get(url)
    with open(filepath, "w", encoding="utf-8") as outfile:
        outfile.write(request.text)


if __name__ == "__main__":

    with open("data/files.json", "r", encoding="utf-8") as infile:
        FILES = json.load(infile)

    for group, file_list in (pbar := tqdm(FILES.items())):
        pbar.set_description(f"Downloading {group}")
        for i in (sub_pbar := tqdm(file_list)):
            sub_pbar.set_description(f"Downloading {i['name']}")
            download_table(i["url"], i["filepath"])
