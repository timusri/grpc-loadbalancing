import grpc
import api_pb2_grpc
import api_pb2
import time


def main():
    request = api_pb2.ApiRequest(
        name="timus",
        message="You are awesome")

    response = stub.ApiEndpoint(request)
    print(response)


if __name__ == '__main__':
    with open('cert/server.crt', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
    channel = grpc.secure_channel('www.timus.com:443', creds)
    stub = api_pb2_grpc.ApiStub(channel)
    while True:
        main()
        time.sleep(2)
