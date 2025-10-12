from locust import User, between

from config import settings


class LocustBaseUser(User):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения документов.
    """
    host = "localhost"
    wait_time = between(
        min_wait=settings.locust_user.wait_time_min,
        max_wait=settings.locust_user.wait_time_max
    )
    abstract = True
