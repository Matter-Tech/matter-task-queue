import pytest

from matter_task_queue import async_to_sync, run_task, run_task_async


def test_basic_task(celery_app, celery_worker):
    @celery_app.task
    def mul(x, y):
        return x * y

    assert mul.delay(4, 4).get(timeout=10) == 16


def test_async_to_sync(celery_app, celery_worker):
    async def foo_async(x, y):
        return x * y

    @celery_app.task
    def foo(x, y):
        return async_to_sync(foo_async, x, y)

    assert foo.delay(4, 4).get(timeout=10) == 16


def test_run_task(celery_app, celery_worker):
    class V:
        x = 4
        y = 4

    @celery_app.task
    def foo():
        V.x = 10
        V.y = 10

    run_task(foo)
    assert V.x == 10
    assert V.y == 10


@pytest.mark.asyncio
async def test_run_task_async(celery_app, celery_worker):
    class V:
        x = 4
        y = 4

    @celery_app.task
    def foo():
        V.x = 10
        V.y = 10

    await run_task_async(foo)
    assert V.x == 10
    assert V.y == 10
