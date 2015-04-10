from __future__ import absolute_import

from celery import Celery

app = Celery('bureaucrat',
             broker='amqp://localhost',
             include=['participants.tasks.webhooks'])

app.conf.update(
    CELERY_IGNORE_RESULT=True,
)

if __name__ == '__main__':
    app.start()
