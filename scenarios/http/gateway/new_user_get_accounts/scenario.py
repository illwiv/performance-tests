from locust import task, TaskSet

from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.users.client import build_users_gateway_locust_http_client, UsersGatewayHTTPClient
from clients.http.gateway.accounts.client import build_accounts_gateway_locust_http_client, AccountsGatewayHTTPClient
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(TaskSet):
    """
    Нагрузочный сценарий, который:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счёт.
    3. Получает счета.

    Использует базовый GatewayHTTPSequentialTaskSet и уже созданных в нём API клиентов.
    """
    create_user_response: CreateUserResponseSchema | None = None
    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient

    def on_start(self):
        self.users_gateway_client = build_users_gateway_locust_http_client(environment=self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(environment=self.user.environment)

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что предыдущий шаг был успешным.
        """
        if not self.create_user_response:
            return

        self.accounts_gateway_client.open_deposit_account(
            user_id=self.create_user_response.user.id
        )

    @task(6)
    def get_accounts(self):
        """
        Получаем счета.
        """
        if not self.create_user_response:
            return

        self.accounts_gateway_client.get_accounts(user_id=self.create_user_response.user.id)


class GetAccountsScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий последовательный сценарий.
    """
    tasks = [GetAccountsTaskSet]
