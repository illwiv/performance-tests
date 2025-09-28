from locust import User, between, task, TaskSet

from clients.grpc.gateway.users.client import build_users_gateway_locust_grpc_client, UsersGatewayGRPCClient
from clients.grpc.gateway.accounts.client import build_accounts_gateway_locust_grpc_client, AccountsGatewayGRPCClient
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetAccountsTaskSet(TaskSet):
    """
    Нагрузочный сценарий, который:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счёт.
    3. Получает счета.

    Использует базовый GatewayHTTPSequentialTaskSet и уже созданных в нём API клиентов.
    """
    create_user_response: CreateUserResponse | None = None
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient

    def on_start(self):
        self.users_gateway_client = build_users_gateway_locust_grpc_client(environment=self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(environment=self.user.environment)

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


class GetAccountsScenarioUser(User):
    """
    Пользователь Locust, исполняющий последовательный сценарий.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)
