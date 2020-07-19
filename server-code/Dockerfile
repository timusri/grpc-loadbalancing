FROM python:3.6
RUN pip install update pip
RUN pip install grpcio
RUN pip install grpcio-tools
COPY api_pb2_grpc.py .
COPY api_pb2.py .
COPY server.py .
COPY insecure-server.py .
COPY cert ./cert/
ENTRYPOINT ping localhost
