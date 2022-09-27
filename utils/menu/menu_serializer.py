import utils
from utils import menu


def menu_to_dict():
    menu_list = utils.read_json("menu.json")
    return {menu["id"]: menu for menu in menu_list}
