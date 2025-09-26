from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest, \
    IssuePhysicalCardResponse
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardRequest, \
    IssueVirtualCardResponse
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub


class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с CardsGatewayServiceStub.
    Предоставляет высокоуровневые методы для получения и создания пользователей.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к UsersGatewayService.
        """
        super().__init__(channel)

        self.stub = CardsGatewayServiceStub(channel)

    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> IssueVirtualCardResponse:
        """
        Низкоуровневый вызов метода IssueVirtualCard через gRPC.

        :param request: gRPC-запрос с данными нового пользователя.
        :return: Ответ от сервиса с данными созданного пользователя.
        """
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """
        Низкоуровневый вызов метода IssuePhysicalCard через gRPC.

        :param request: gRPC-запрос с данными нового пользователя.
        :return: Ответ от сервиса с данными созданного пользователя.
        """
        return self.stub.IssuePhysicalCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponse:
        request = IssueVirtualCardRequest(user_id=user_id, account_id=account_id)
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        request = IssuePhysicalCardRequest(user_id=user_id, account_id=account_id)
        return self.stub.IssuePhysicalCard(request)


def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра CardsGatewayGRPCClient.

    :return: Инициализированный клиент для CardsGatewayGRPCClient.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_grpc_client())
