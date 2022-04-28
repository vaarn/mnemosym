"""
mnemosym.generators
~~~~~~~~~~~~~~~~~~~
contains functions for rolling on tables provided by the table manager.

TODO: there is a lot of duplicated code here that could be refactored into one or two
different functions that take specific table and subtables.
"""
from random import choice, randint

from mnemosym.config import DATA_DIR
from mnemosym.table_manger import TableManager

tm = TableManager(DATA_DIR)


def generate_stat() -> int:
    "3d6 keep lowest"
    return min([randint(1, 6) for i in range(3)])  # nosec - same as above


def generate_stat_block() -> str:
    """generates stat bonuses and hp"""
    character_stats = [
        "STR",
        "DEX",
        "CON",
        "INT",
        "PSY",
        "EGO",
    ]
    stats = {s: generate_stat() for s in character_stats}
    return (
        "\n".join([f"{10+bonus} {stat} +{bonus}" for stat, bonus in stats.items()])
        + "\n"
        + "You may swap the scores of two abilities."
    )


def generate_hp(fudge=False) -> str:
    """generates hp, can be fudged"""
    if fudge is False:
        hitpoints = randint(1, 8)
    if fudge is True:
        hitpoints = randint(5, 8)
    return f"**HP:** {hitpoints}"


def list_ancestry() -> str:
    """lists available ancestries."""
    return "Available ancestries:\n" + "\n".join(list(tm.tables["ancestries"].keys()))


def generate_ancestry_features(ancestry=None) -> dict:
    """generates a dict of random and static ancestry features from a table dict"""
    if ancestry is None:
        target_ancestry = choice(list(tm.tables["ancestries"].keys()))
    else:
        target_ancestry = ancestry
    target_table = tm.tables["ancestries"][target_ancestry]
    ancestry_rolls = target_table.roll_table()
    ancestry_characteristics = target_table.characteristics

    return (
        f"**Ancestry:** {target_ancestry}\n"
        + f"> {ancestry_characteristics['description']}\n\n"
        + "**Special(s):**\n"
        + "    \n".join(ancestry_characteristics["special"])
        + "\n\n"
        + "\n".join(f"**{k}:** {v}" for k, v in ancestry_rolls.items())
    )


def generate_weapon():
    """generates a weapon"""
    weapon_table = tm.tables["equipment"]["Weapons"]
    return f"**Weapon:** {weapon_table.joined_roll(['aspect', 'Form', 'damage'])}"


def generate_armour():
    """generates armour"""
    armour_table = tm.tables["equipment"]["Armour"]
    return f"**Armour:** {armour_table.joined_roll(['quality', 'type'])}"


def generate_gear():
    """generates starting gear without weapon or armour"""
    gear_table = tm.tables["equipment"]["Gear"]
    return (
        "**Starting Gear:** 3 Days Rations, "
        + f"{gear_table.joined_roll(['Gear 1', 'Gear 2'], ' & ')}."
    )


def generate_gift():
    """generates a gift"""
    gift_table = tm.tables["equipment"]["Mystic Gifts"]
    return (
        f"**Source of Power:** {gift_table.specified_roll('Source of Power')}"
        + "\n**Your Gift:** {gift_table.specified_roll('Your Gift')}"
    )


def generate_cybernetic():
    """generates a cybernetic"""
    cybernetic_table = tm.tables["equipment"]["Cybernetics"]
    result_list = cybernetic_table.specified_roll("cyber")
    return f"**{result_list[0]} ({result_list[1]})** {' '.join(result_list[2:])}"
