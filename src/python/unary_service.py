import grpc
from unary_pb2_grpc import UnaryServicer, add_UnaryServicer_to_server
from unary_pb2 import Message, Response
from concurrent import futures

class UnaryService(UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass  #do nothing for the time being

    def Respond(self, request: Message, context) -> Response:
        "This is the main service entry point"
        response = Response()
        response.message = "I did not understand the message"
        response.received = False
        if len(request.message) > 0:
            response.message = f"I have received the following: {request.message}"
            response.received = True
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
