import requests
from requests.adapters import HTTPAdapter
from testcontainers.localstack import LocalStackContainer
from urllib3 import Retry


class SqsMock(LocalStackContainer):
    def __init__(self):
        super(SqsMock, self).__init__("localstack/localstack:latest-amd64")
        self.get_container_host_ip = lambda: f"localhost"

        # Include any AWS services we wish to test within this integration test component.
        self.with_services("sqs")

    def get_container_host_ip(self):
        return "localhost"

    def start(self, timeout=60):
        super().start(timeout=timeout)

        with requests.Session() as session:
            retries = Retry(total=10, backoff_factor=0.1)
            session.mount("http://", HTTPAdapter(max_retries=retries))
            session.get(self.get_url())

        return self

    def get_aws_endpoint(self):
        host = self.get_container_host_ip()
        port = self.get_exposed_port(LocalStackContainer.EDGE_PORT)

        return f"{host}:{port}"