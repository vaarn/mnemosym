"""
mnemosym.table_manager
~~~~~~~~~~~~~~~~~~~~~~
This module holds both the table and table manager classes.

Table managers are responsible for loading the data and initalizing specific tables to
a self.tables dictionary (organized further by equipment and ancestry dictionaries).

Tables are resonsible for initalizing the table dictionary and rolling on it, as well as
providing non-rolled charactersitics.
"""
import json
from collections import defaultdict
from pathlib import Path
from random import choice
from typing import List

# useful dict that defaults to values being empty dictionaries
dictdict = defaultdict(dict)


class Table:
    """
    A table represents a set of rolls and characteristics derived from the dictionary
    supplied.
    """

    def __init__(self, table_dict) -> None:
        self.rolls = table_dict.pop("rolls")  # pop to get remaining characteristics
        self.characterisitcs = table_dict  # popped dict only containing characteristics

    def specified_roll(self, table_name):
        """
        rolls a specific named subtable.
        N.b. this will not work if rolls have duplicate name values.
        """
        table_options = list(filter(lambda x: x["name"] == table_name, self.rolls))[0]
        return choice(table_options)  # nosec

    def roll_table(self) -> dict:
        """rolls all the subtables and returns results dict"""
        return {
            sub_table["name"]: choice(sub_table["options"]) for sub_table in self.rolls
        }  # nosec


class EquipmentTable(Table):
    """modified table that builds weapons and armour in addition to rolling gear"""

    def joined_roll(self, sub_tables: List[str]):
        """returns a string of the rolled subtables joined with spaces"""
        return " ".join([self.specified_roll(i) for i in sub_tables])

    def cybernetics_roll(self):
        """edge case handling for the cybernetics formatting"""
        return " ".join(choice(self.rolls[0]))


class TableManager:  # pylint: disable=too-few-public-methods
    """loads and manages the creation of the tables"""

    def __init__(
        self,
        path_to_data_dir: Path,
    ) -> None:
        self.index: dict = self.load_json(path_to_data_dir / "files.json")
        self.tables: dict = self._load_data()

    @staticmethod
    def load_json(filename: str) -> dict:
        """utility method for loading json dict from filename"""
        with open(filename, "r", encoding="utf-8") as infile:
            output = json.load(infile)
        return output

    def _load_data(self):
        """loads the data and sets the properties"""
        tables = dictdict
        for group, file_list in self.index.items():
            for file in file_list:
                target_dict = self.load_json(file["filepath"])
                if group == "ancestries":
                    target_table = Table(target_dict)
                if group == "equipment":
                    target_table = EquipmentTable(target_dict)

                tables[group][file["name"]] = target_table
        return tables
