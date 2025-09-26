from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum

from tools.fakers import fake


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура данных для создания операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str = Field(default_factory=fake.category)


class MakeBillPaymentRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass


class MakeCashWithdrawalRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    pass


class OperationSchema(BaseModel):
    """
    Структура данных для операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Структура данных для чека по операции.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Структура данных для описания опирации.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    """
    Структура данных для получения ответа по операции.
    """
    operations: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Структура данных для получения ответа по списку операций.
    """
    operations: list[OperationSchema]


class GetOperationsReceiptResponseSchema(BaseModel):
    """
    Структура данных для получения ответа по чеку.
    """
    receipt: OperationReceiptSchema


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура данных для получения ответа по описанию.
    """
    summary: OperationsSummarySchema


class BaseFeeOperationResponseSchema(BaseModel):
    """
    Структура данных для ответа при создании операции.
    """
    operation: OperationSchema


class MakeFeeOperationResponseSchema(BaseFeeOperationResponseSchema):
    """
    Структура данных для ответа при создании операции комиссии.
    """
    pass


class MakeTopUpOperationResponseSchema(BaseFeeOperationResponseSchema):
    """
    Структура данных для ответа при создании операции пополнения.
    """
    pass


class MakeCashWithdrawalOperationResponseSchema(BaseFeeOperationResponseSchema):
    """
    Структура данных для ответа при создании операции снятия наличных денег.
    """
    pass


class MakeTransferOperationResponseSchema(BaseFeeOperationResponseSchema):
    """
    Структура данных для ответа при создании операции перевода.
    """
    pass


class MakePurchaseOperationResponseSchema(BaseFeeOperationResponseSchema):
    """
    Структура данных для ответа при создании операции покупки.
    """
    pass


class MakeBillPaymentOperationResponseSchema(BaseFeeOperationResponseSchema):
    """
    Структура данных для ответа при создании оплаты по счету.
    """
    pass


class MakeCashbackOperationResponseSchema(BaseFeeOperationResponseSchema):
    """
    Структура данных для ответа при создании операции кэшбэка.
    """
    pass
