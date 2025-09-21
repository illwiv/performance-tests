from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура данных для создания операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakeBillPaymentRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass


class MakeCashWithdrawalRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    pass


class OperationDict(TypedDict):
    """
    Структура данных для операции.
    """
    id: str
    type: str
    statu: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Структура данных для чека по операции.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Структура данных для описания опирации.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationResponseDict(TypedDict):
    """
    Структура данных для получения ответа по операции.
    """
    operations: OperationDict


class GetOperationsResponseDict(TypedDict):
    """
    Структура данных для получения ответа по списку операций.
    """
    operations: list[OperationDict]


class GetOperationsReceiptResponseDict(TypedDict):
    """
    Структура данных для получения ответа по чеку.
    """
    receipt: OperationReceiptDict


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура данных для получения ответа по описанию.
    """
    summary: OperationsSummaryDict


class BaseFeeOperationResponseDict(TypedDict):
    """
    Структура данных для ответа при создании операции.
    """
    operation: OperationDict


class MakeFeeOperationResponseDict(BaseFeeOperationResponseDict):
    """
    Структура данных для ответа при создании операции комиссии.
    """
    pass


class MakeTopUpOperationResponseDict(BaseFeeOperationResponseDict):
    """
    Структура данных для ответа при создании операции пополнения.
    """
    pass


class MakeCashWithdrawalOperationResponseDict(BaseFeeOperationResponseDict):
    """
    Структура данных для ответа при создании операции снятия наличных денег.
    """
    pass


class MakeTransferOperationResponseDict(BaseFeeOperationResponseDict):
    """
    Структура данных для ответа при создании операции перевода.
    """
    pass


class MakePurchaseOperationResponseDict(BaseFeeOperationResponseDict):
    """
    Структура данных для ответа при создании операции покупки.
    """
    pass


class MakeBillPaymentOperationResponseDict(BaseFeeOperationResponseDict):
    """
    Структура данных для ответа при создании оплаты по счету.
    """
    pass


class MakeCashbackOperationResponseDict(BaseFeeOperationResponseDict):
    """
    Структура данных для ответа при создании операции кэшбэка.
    """
    pass


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id

        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}.")

    def get_operations_api(self, account_id: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        :account_id: Идентификатор аккаунта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**account_id))

    def get_operation_recemake_fee_operation_api(self, account_id: GetOperationsQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :account_id: Идентификатор аккаунта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**account_id))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с данными операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка

        :param request: Словарь с данными операции кэшбека.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с данными операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        :param request: Словарь с данными операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с данными операции оплаты по счету.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с данными операции снятия наличных денег.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationsReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operation_recemake_fee_operation_api(query)
        return response.json()

    def make_fee_operation(self, account_id: str, card_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(status="COMPLETED", amount=55.77, accountId=account_id, cardId=card_id)
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, account_id: str, card_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(status="COMPLETED", amount=55.77, accountId=account_id, cardId=card_id)
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, account_id: str, card_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(status="COMPLETED", amount=55.77, accountId=account_id,
                                                   cardId=card_id)
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, account_id: str, card_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(status="COMPLETED", amount=55.77, accountId=account_id,
                                                   cardId=card_id)
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, account_id: str, card_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(status="COMPLETED", amount=55.77, accountId=account_id,
                                                   cardId=card_id, category='taxi')
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, account_id: str, card_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentRequestDict(status="COMPLETED", amount=55.77, accountId=account_id, cardId=card_id)
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, account_id: str, card_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalRequestDict(status="COMPLETED", amount=55.77, accountId=account_id, cardId=card_id)
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
