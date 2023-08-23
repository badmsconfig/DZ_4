def get_valid_input(prompt, correct_answer):
    """
    Функция получает ввод от пользователя и проверяет его на соответствие правильному ответу.
    Возвращает True, если ввод правильный, и False в противном случае.
    :param prompt: строка с вопросом
    :param correct_answer: правильный ответ
    :return: True, если ввод правильный, и False в противном случае
    """
    user_input = input(prompt)
    return user_input == correct_answer

def main():
    year_prompt = 'Введите год рождения А.С.Пушкина: '
    day_prompt = 'В какой день июня родился Пушкин? '

    year_correct = '1799'
    day_correct = '6'

    while not get_valid_input(year_prompt, year_correct):
        print('Не верно')

    while not get_valid_input(day_prompt, day_correct):
        print('Не верно')

    print('Верно')

if __name__ == "__main__":
    main()
