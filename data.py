DRIVER_NAME = None

class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    URL_HOME = f"{BASE_URL}/"  # Домашняя страница (Конструктор)
    URL_ENTRANCE_PERSONAL_ACCOUNT = f"{BASE_URL}/login"  # Форма авторизации
    URL_RECOVERY_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"  # Страница восстановления пароля
    URL_RECOVERY_PASSWORD_FORM = f"{BASE_URL}/reset-password"  # Форма восстановления пароля
    URL_ACCOUNT_PROFILE = f"{BASE_URL}/account/profile"  # Личный кабинет (Профиль)
    URL_ORDER_HISTORY = f"{BASE_URL}/account/order-history"  # История заказов
    URL_ORDER_FEED = f"{BASE_URL}/feed"  # Лента заказов

class UserData:
    email = 'testgureva@ya.ru'
    password = '123456'