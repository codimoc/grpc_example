import grpc
from unary_pb2_grpc import UnaryStub
from unary_pb2 import Message


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")

        # bind the client and the server
        self.stub = UnaryStub(self.channel)

    def call_service(self, message: str):
        """
        Client function to call the rpc for Respond service
        """
        message = Message(message=message)
        return self.stub.Respond(message)


if __name__ == '__main__':
    client = UnaryClient()
    result = client.call_service(message="Hello Server, are you there?")
    print(f'{result}')