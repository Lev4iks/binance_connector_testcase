from telegram_bot import notify_all_subs
from settings import CONFIG


def check_pair(pair) -> None:
    pair_name = str(*pair)
    recent_pair_price = float(*pair.values())
    trigger = CONFIG[pair_name]['trigger']
    price_trigger = float(CONFIG[pair_name]['price'])

    if trigger == "more" and recent_pair_price > price_trigger:
        notify_all_subs(f"MORE TRIGGER, {pair_name, trigger, price_trigger}\n"
                        f"Current price : {recent_pair_price}")
    elif trigger == "less" and recent_pair_price < price_trigger:
        notify_all_subs(f"LESS TRIGGER, {pair_name, trigger, price_trigger}\n"
                        f"Current price : {recent_pair_price}")
    elif trigger == "more_eq" and recent_pair_price >= price_trigger:
        notify_all_subs(f"MORE OR EQUAL TRIGGER, {pair_name, trigger, price_trigger}\n"
                        f"Current price : {recent_pair_price}")
    elif trigger == "less_eq" and recent_pair_price <= price_trigger:
        notify_all_subs(f"LESS OR EQUAL TRIGGER, {pair_name, trigger, price_trigger}\n"
                        f"Current price : {recent_pair_price}")