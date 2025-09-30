from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя.
    Создаём 300 пользователей, каждому из которых открываются кредитный счет, пять операций покупок,
    1 операцию пополнения и 1 операцию снятия наличных.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания загрузки списка операций по своему кредитному счёту и
        просмотра статистики по этим операциям.
        Мы создаём 300 пользователей, каждый получит кредитный счет, пять операций покупок,
        1 операцию пополнения и 1 операцию снятия наличных
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                ),
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
