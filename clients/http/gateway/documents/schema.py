from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: HttpUrl
    document: str


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры тарифа.
    """
    contract: DocumentSchema


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры контракта.
    """
    tariff: DocumentSchema
