from httpx import Response, QueryParams
from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import GetOperationsQuerySchema, MakeFeeOperationRequestSchema, \
    MakeTopUpOperationRequestSchema, MakeCashbackOperationRequestSchema, MakeTransferOperationRequestSchema, \
    MakePurchaseOperationRequestSchema, MakeBillPaymentRequestSchema, MakeCashWithdrawalRequestSchema, \
    GetOperationResponseSchema, GetOperationsReceiptResponseSchema, GetOperationsSummaryResponseSchema, \
    MakeFeeOperationResponseSchema, MakeTopUpOperationResponseSchema, MakeCashbackOperationResponseSchema, \
    MakeTransferOperationResponseSchema, MakePurchaseOperationResponseSchema, MakeBillPaymentOperationResponseSchema, \
    MakeCashWithdrawalOperationResponseSchema, GetOperationsResponseSchema


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}",
                        extensions=HTTPClientExtensions(route="/api/v1/operations/{operation_id}"))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id

        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}",
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operation-receipt/{operation_id}"))

    def get_operations_api(self, account_id: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определенного счета.

        :account_id: Идентификатор аккаунта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**account_id.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations"))

    def get_operation_recemake_fee_operation_api(self, account_id: GetOperationsQuerySchema) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :account_id: Идентификатор аккаунта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary",
                        params=QueryParams(**account_id.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operations-summary"))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с данными операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка

        :param request: Словарь с данными операции кэшбека.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с данными операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создание операции покупки.

        :param request: Словарь с данными операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentRequestSchema) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с данными операции оплаты по счету.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalRequestSchema) -> Response:
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с данными операции снятия наличных денег.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationsReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationsReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operation_recemake_fee_operation_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, account_id: str, card_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(account_id=account_id, card_id=card_id)
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, account_id: str, card_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(account_id=account_id, card_id=card_id)
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, account_id: str, card_id: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(account_id=account_id,
                                                     card_id=card_id)
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, account_id: str, card_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(account_id=account_id,
                                                     card_id=card_id)
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, account_id: str, card_id: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(account_id=account_id,
                                                     card_id=card_id)
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, account_id: str, card_id: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentRequestSchema(account_id=account_id, card_id=card_id)
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, account_id: str,
                                       card_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalRequestSchema(account_id=account_id, card_id=card_id)
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
