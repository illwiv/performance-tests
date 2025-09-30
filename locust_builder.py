from seeds.builder import build_grpc_seeds_builder

from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan


builder = build_grpc_seeds_builder()

result = builder.build(
    SeedsPlan(
        users=SeedUsersPlan(
            count=500,
            credit_card_accounts=SeedAccountsPlan(
                count=1,
                physical_cards=SeedCardsPlan(count=1)
            )
        ),
    )
)

# Шаг 3. Сохраняем результат сидинга в файл, привязанный к сценарию "test-scenario"
save_seeds_result(result=result, scenario="test-scenario")

# Шаг 4. Загружаем данные из файла и выводим в консоль
print(load_seeds_result(scenario="test-scenario"))

