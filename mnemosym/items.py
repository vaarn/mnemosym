"""
mnemosym.items
~~~~~~~~~~~~~~
"""
import os
import dice
import yaml
from jinja2 import Environment, FileSystemLoader
from mnemosym.config import DATA_DIR

# Configure jinja2
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


# this is temporary and will be expanded or replaced.
def d20() -> int:
    """rolls a d20 dice and returns the result"""
    result = dice.roll('d20')
    return result[0]


def data_load(ext_data) -> dict:
    """returns a python dict from a yaml file that is passed in when called"""
    file_path = os.path.join(DATA_DIR,ext_data)
    with open(file_path, mode='r', encoding='utf8') as stream:
        try:
            # Converts yaml document to python object
            exdata_dict = yaml.safe_load(stream)
        except yaml.YAMLError as error:
            print(error)
    return exdata_dict


# This will be a common pattern, so documenting just this first one.
def generate_book():
    """generates a book of Vaarn"""
    # load books dict from srd tables
    books = data_load('items-books.yaml')
    # create book dict using rolls against books dict
    book = {
        'cover': books['cover'][d20()],
        'author': books['author'][d20()],
        'style': books['style'][d20()],
        'subject': books['subject'][d20()],
        'feature': books['feature'][d20()]
    }
    # load jinja template
    template = env.get_template('book.j2')
    # render the template with the book dict and return to caller.
    return template.render(book)


def generate_drug():
    """generates vaarn drug"""
    drugs = data_load('items-drugs.yaml')
    drug = {
        'colour': drugs['colour'][d20()],
        'form': drugs['form'][d20()],
        'ingested': drugs['ingested_by'][d20()],
        'effect1': drugs['effect'][d20()],
        'effect2': drugs['effect'][d20()]
    }
    template = env.get_template('drug.j2')
    return template.render(drug)

