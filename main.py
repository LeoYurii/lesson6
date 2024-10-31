import urwid


def has_digit(password):
    return any(char.isdigit() for char in password)


def is_very_long(password):
    return len(password) > 12


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def update_password_info(edit, new_edit_text):
    password = new_edit_text
    score = sum([
        2 if has_digit(password) else 0,
        2 if is_very_long(password) else 0,
        2 if has_letters(password) else 0,
        2 if has_upper_letters(password) else 0,
        2 if has_lower_letters(password) else 0,
        2 if has_symbols(password) else 0
    ])
    score_text.set_text(f'Рейтинг пароля: {score}')


ask = urwid.Edit('Введите пароль: ', mask='*')
score_text = urwid.Text('')
menu = urwid.Pile([ask, score_text])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', update_password_info)
urwid.MainLoop(menu).run()
