import grpc
from concurrent import futures
import time
import api_pb2
import api_pb2_grpc
import os


class ChatBox(api_pb2_grpc.ApiServicer):

    def ApiEndpoint(self, request, context):
        response = api_pb2.ApiResponse()
        response.reply = "Hi {}, myself {} , Thanks for this message : {}".format(
            request.name, os.getenv("POD_NAME"), request.message)
        return response


if __name__ == '__main__':
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    with open('cert/server.key', 'rb') as f:
        private_key = f.read()
    with open('cert/server.crt', 'rb') as f:
        certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain), ))

    # add the servier created above tp the server
    api_pb2_grpc.add_ApiServicer_to_server(ChatBox(), server)

    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_secure_port('[::]:50051', server_credentials)
    server.start()
    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
