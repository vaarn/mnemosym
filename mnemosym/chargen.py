"""
mnemosym.chargen
"""
import json
from random import choice, choices, randint
from typing import List

PLAYER_STATS = [
    "STR",
    "DEX",
    "CON",
    "INT",
    "PSY",
    "EGO",
]

ANCESTRIES = [
    "True-Kin",
    # "Cacogen",
    # "Synth",
    # "Newbeast",
]


def load_table(table_name: str) -> dict:
    """load dict of random options from json"""
    with open(f"./tables/{table_name}.json", "r", encoding="utf8") as file:
        return json.load(file)


def choice_from_weighted_table(table: dict) -> str:
    """
    takes a dict where keys represent a choice and values represent their weights
    returns a random choice by weight
    """
    return choices(list(table.keys()), list(table.values()), k=1)[
        0
    ]  # nosec - we don't use choices for any cryptography


def generate_stat() -> int:
    "3d6 keep lowest"
    return min([randint(1, 6) for i in range(3)])  # nosec - same as above


def generate_stat_block(player_stats: List[str]) -> dict:
    """generates stat bonuses and hp"""
    stats = {s: generate_stat() for s in player_stats}
    return stats


def generate_ancestry_features(ancestry_table_dict: dict) -> dict:
    """generates a dict of random and static ancestry features from a table dict"""
    ancestry_details = {
        name: choice_from_weighted_table(table)
        for name, table in ancestry_table_dict["tables"].items()
    }
    ancestry_details["ANCESTRY"] = ancestry_table_dict["table_name"]
    ancestry_details["SPECIAL"] = ancestry_table_dict["specials"]
    return ancestry_details


def generate_starting_equipment(equipment_table_dict: dict) -> List[str]:
    """builds weapon, armour and rolls on both gear tables"""
    weaponry = equipment_table_dict["tables"]["Weaponry"]
    armour = equipment_table_dict["tables"]["Armour"]
    gear_1 = equipment_table_dict["tables"]["Gear Table I"]
    gear_2 = equipment_table_dict["tables"]["Gear Table II"]
    exotica = equipment_table_dict["tables"]["Exotica"]
    return [
        (
            f"{choice_from_weighted_table(weaponry['ASPECT'])} "
            f"{choice_from_weighted_table(weaponry['FORM'])} "
            f"{choice_from_weighted_table(weaponry['DAMAGE & WEIGHT'])}"
        ),
        (
            f"{choice_from_weighted_table(armour['Quality'])} "
            f"{choice_from_weighted_table(armour['Type'])}"
        ),
        choice_from_weighted_table(gear_1),
        choice_from_weighted_table(gear_2),
        choice_from_weighted_table(exotica),
    ]


def generate_gift(gift_table):
    """generate a gift"""
    source = gift_table["tables"]["SOURCE OF POWER"]
    gift = gift_table["tables"]["YOUR GIFT"]

    return (
        f"Gift: {choice_from_weighted_table(gift)}"
        f"\nSource: {choice_from_weighted_table(source)}\n"
    )


def generate_character():
    """generate and format character"""
    stat_block = generate_stat_block(PLAYER_STATS)

    ancestry = choice(ANCESTRIES)
    ancestry_table = load_table(ancestry)
    ancestry_details = generate_ancestry_features(ancestry_table)

    equipment = load_table("equipment")
    item_slots = generate_starting_equipment(equipment)

    gifts = load_table("gifts")
    gift = generate_gift(gifts)

    return (
        "```\n"
        # + f"Name: {ancestry_details['NAME']}\n"
        + "\n".join([f"{k}: {v}" for k, v in ancestry_details.items()])
        + f"\nLevel: 1 | HP: {randint(1, 8)}\n"
        + "\n".join(
            [f"{10+bonus} {stat} +{bonus}" for stat, bonus in stat_block.items()]
        )
        + f"\n{gift}"
        + "Items:\n  - "
        + "\n  - ".join(item_slots)
        + "\n```"
    )
