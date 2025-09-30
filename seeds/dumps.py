import os
from pathlib import Path
from seeds.schema.result import SeedsResult

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DUMPS_PATH = PROJECT_ROOT / "dumps"

def save_seeds_result(result: SeedsResult, scenario: str):
    """
    Сохраняет результат сидинга (SeedsResult) в JSON-файл.

    :param result: Результат сидинга, сгенерированный билдером.
    :param scenario: Название сценария нагрузки, для которого создаются данные.
                     Используется для генерации имени файла (например, "credit_card_test").
    """
    # Убедимся, что папка dumps существует
    if not os.path.exists(DUMPS_PATH):
        os.mkdir(DUMPS_PATH)

    # Сохраняем результат сидинга в файл с именем {scenario}_seeds.json
    filename = os.path.join(DUMPS_PATH, f"{scenario}_seeds.json")
    with open(filename, "w+", encoding="utf-8") as file:
        file.write(result.model_dump_json())


def load_seeds_result(scenario: str) -> SeedsResult:
    """
    Загружает результат сидинга из JSON-файла.

    :param scenario: Название сценария нагрузки.
    :return: Объект SeedsResult.
    """
    filename = os.path.join(DUMPS_PATH, f"{scenario}_seeds.json")
    with open(filename, "r", encoding="utf-8") as file:
        return SeedsResult.model_validate_json(file.read())
