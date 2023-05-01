import random

import pandas as pd


# def check_user(chat_id):
#     # code
#     return req_str


def get_themes():
    try:
        df = pd.read_excel('file.xlsx', sheet_name='Математика', usecols='B:B')
    except ValueError:
        print(f"Column B not found in file 'file.xlsx'")
        return {}
    req_result = {}
    items = []
    names = df['Тема'].dropna().tolist()
    for item in names:
        if not pd.isna(item):
            items.append(item)
    keys = list(range(len(names)))
    for i in keys:
        req_result[str(i)] = str(names[i])
    return req_result


def get_task(theme_id):
    try:
        df = pd.read_excel('file.xlsx', sheet_name='Математика', usecols=[0, 1, 4, 5, 6, 7])
    except ValueError:
        print(f"Columns not found in file 'file.xlsx'")
        return {}
    req_result = {}
    items = []
    themes = df['Тема2'].dropna().tolist()
    tasks = df['Задача'].dropna().tolist()
    inc = list(range(len(tasks)))
    theme_name = get_theme_by_id(theme_id)
    for item in inc:
        if not pd.isna(item):
            if themes[item] == theme_name:
                items.append(item)
                req_result[str(item)] = str(tasks[item])
    data_answer = {}
    data_solution = {}
    for row in df.itertuples():
        theme, task, solution, answer = row[3], row[4], row[5], row[6]
        data_answer[str(task)] = {"answer": str(answer)}
        data_solution[str(task)] = {"solution": str(solution)}

    task_text = random.choice(list(req_result.values()))

    solution_text = data_solution.get(task_text, {"solution": "Решение не найдено"})
    answer_text = data_answer.get(task_text, {"answer": "Ответ не найден"})

    random_value = task_text + "\n Решение: <tg-spoiler>" + solution_text[
        "solution"] + "</tg-spoiler>." + "\n Ответ: <tg-spoiler>" + answer_text["answer"] + "</tg-spoiler>."
    return random_value


def get_theme_by_id(theme_id):
    try:
        df = pd.read_excel('file.xlsx', sheet_name='Математика', usecols=[0, 1])
    except ValueError:
        print(f"Columns not found in file 'file.xlsx'")
        return ""
    theme_dict = dict(zip(map(int, df['Идентификатор'].dropna().tolist()), df['Тема']))
    return theme_dict.get(int(theme_id))
