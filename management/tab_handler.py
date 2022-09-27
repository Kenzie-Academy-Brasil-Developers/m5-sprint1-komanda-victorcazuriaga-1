import utils
from datetime import date, time, datetime, timedelta, timezone


def calculate_tab(itens_list):
    menu = utils.menu_to_dict()
    total = 0
    for item in itens_list:
        price = menu[item["id"]]["price"]
        total += price * item["amount"]
    return {"subtotal": total, "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
