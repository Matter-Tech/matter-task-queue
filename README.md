# matter-task-queue

The Task Queue Library is a Python library that provides functionality for managing queues and integrates Celery into FastAPI apps. It enables a seamless integration that unlocks all of Celery's capabilities and allows for easy queue management and task execution.

Celery is an open-source, distributed task queue that is widely used in Python-based applications for processing and executing background tasks or long-running processes asynchronously. It was created in 2009 and has since grown into a mature and powerful library that provides a robust and scalable solution for managing task queues.

The core idea behind Celery is to divide an application into small, independent tasks that can be executed asynchronously in a distributed environment. Tasks are added to a queue, where they wait to be picked up by a worker process. Once a worker picks up a task, it executes it and updates the status of the task. This allows tasks to be executed independently and in parallel, without blocking the main application thread.

Celery provides a number of features that make it a popular choice for managing task queues. It supports a wide range of brokers, including RabbitMQ, Redis, and Amazon SQS, which allows it to work with many different messaging systems. It also provides support for scheduling tasks, task retries, and task prioritization, which makes it easy to build complex workflows.

Another key feature of Celery is its ability to distribute tasks across multiple worker nodes. This allows tasks to be processed in parallel, which can improve overall performance and scalability. Celery provides several different strategies for distributing tasks, including round-robin, direct, and fanout.

**Table of Contents**

- [Installation](#installation)
- [License](./LICENSE)

## Installation

```console
pip install matter-task-queue
```

Make sure that you have set the following ENV values:
```console
ENV=test-or-local-or-development-or-production
DEBUG=false
INSTANCE_NAME=your-webapp-name
CELERY_BROKER_URL=your-broker-url
CELERY_LOG_LEVEL=info
CELERY_LOG_FILE_PATH=/tmp/celery.txt
AWS_REGION=eu-central-1
SENTRY_DSN=your-sentry-dsn
```

## Usage

To use the Task Queue Library in your FastAPI app, you can import the TaskQueue class and create an instance of it:

```python
# Create api
app = FastAPI(
    title="My FastAPI Web Service",
    root_path=env.PATH_PREFIX,
)

from matter_task_queue import create_celery
app.celery = create_celery(
    task_module_paths=["your.task.model.paths", "", ...]
)
```

The constructor takes two more optional arguments:

celery_beat_schedule: The schedule for periodic cron-jobs
create_dead_letter_queue: defaults to True


## Contributing

Make sure you have all supported python versions installed in your machine:

* 3.10
* 3.11

### Install hatch in your system

```https://hatch.pypa.io/latest/install/```

### Create the environment

```console
hatch env create
```

Do your changes...

### Run the tests

```console
hatch run test
```

The command above will run the tests against all supported python versions
installed in your machine. For testing in other operating system you may use the
configured CI in github. 

### Bump a new version

In general, you just need to execute:

```console
hatch version
```

This command will update the minor version. i.e.:
No breaking changes and new feature has been added

We are using [semantic version](https://semver.org/), if you are doing a bug fix:

```console
hatch version fix
```
