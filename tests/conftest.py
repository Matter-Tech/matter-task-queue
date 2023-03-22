import os
import pytest
from dotenv import load_dotenv

from tests.utils import SqsMock


if not load_dotenv("test.env"):
    load_dotenv("tests/test.env")


@pytest.fixture(scope="session", autouse=True)
def aws_container():
    localstack = SqsMock()
    localstack.start()
    yield localstack
    localstack.stop()

@pytest.fixture(scope="session")
def sqs_mock(aws_container):
    yield aws_container

@pytest.fixture(scope="session")
def mock_celery_broker(sqs_mock):
    aws_endpoint = sqs_mock.get_aws_endpoint()
    celery_broker_url = f"sqs://{aws_endpoint}"
    os.environ["CELERY_BROKER_URL"] = celery_broker_url
    os.environ["AWS_ENDPOINT_URL"] = f"http://{aws_endpoint}"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_ACCESS_KEY_ID"] = "test"

    from matter_task_queue.config import Config
    Config.load_variables()


@pytest.fixture(scope='session')
def celery_config(mock_celery_broker):
    from matter_task_queue.celery_config import build_celery_config
    celery_config = build_celery_config(create_dead_letter_queue=True)

    return celery_config

