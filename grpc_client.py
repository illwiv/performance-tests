import grpc

import greeting_pb2_grpc
import greeting_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')

    stub = greeting_pb2_grpc.GreeterStub(channel)

    request = greeting_pb2.HelloRequest(name='world')
    response = stub.SayHello(request)
    print("Server response: {}".format(response.message))


if __name__ == '__main__':
    run()