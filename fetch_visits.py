s = "['В корзину - https://www.hse.ru/edu/dpo/764596397?yclid=2696005785434456063','✓ В корзине - https://www.hse.ru/edu/dpo/764596397?yclid=2696005785434456063']"

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

print(get_goals_program_ids(s))