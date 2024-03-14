import re
from urllib.parse import urlparse, parse_qs

def get_goals_names(params):
    lst = params[1:-1].split(',')
    res = []
    for goal in lst:
        res.append(goal.split(" - ")[0][1:])
    return res


def get_goals_program_ids(params):
    lst = params[1:-1].split(',')
    res = []
    for goal in lst:
        if len(goal.split(" - ")) <= 1:
            res.append(None)
            continue
        url = goal.split(" - ")[1][:-1]
        if not url:
            res.append(None)
            continue
        if url.find("hse.ru/edu/dpo/") == -1:
            res.append(None)
        params_str = url[url.find("hse.ru/edu/dpo/") + len("hse.ru/edu/dpo/"):]
        if params_str.find("?") == -1:
            res.append(params_str)
        else:
            res.append(params_str[:params_str.find("?")])
    return res    


def parse_goal(goal_rus):
    if goal_rus.find("Подать заявку") != -1:
        return "send_application"
    if goal_rus.find("В корзину") != -1:
        return "add_to_cart"
    if goal_rus.find("вопрос") != -1:
        return "ask_question"
    if goal_rus.find("Избранное") != -1:
        return "feature"
    if goal_rus.find("бесплатный модуль") != -1:
        return "trial"
    if goal_rus.find("тест-драйв") != -1:
        return "trial"

    return "other"
    