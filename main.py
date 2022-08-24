from login import google_login


def start_app():
    user_email = input('Name: ')
    user_psw = input('Password: ')
    google_login(user_email, user_psw)


if __name__ == '__main__':
    start_app()
