from __future__ import absolute_import

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'webhook_launcher.settings'

from webhook_launcher.app.utils import handle_payload
from webhook_launcher.app.utils import relay_payload
from participants.celery import app

process_def = """<?xml version="1.0"?>
<process>
    <action participant="participant2" />
</process>
"""

@app.task
def participant1(workitem):
    """Test participant1 function."""

    if "counter" not in workitem["fields"]:
        workitem["fields"]["counter"] = 0
    else:
        workitem["fields"]["counter"] += 1
    workitem["fields"]["some_process"] = process_def

    return workitem

@app.task
def participant2(workitem):
    """Test participant2 function."""
    return workitem

@app.task
def handle_webhook(workitem):
    """Handle POST request to a webhook."""

    payload = workitem["fields"]["payload"]
    handle_payload(payload)

    return workitem

@app.task
def relay_webhook(workitem):
    """Relay webhook POST request to task queue."""

    payload = workitem["fields"]["payload"]
    relay_payload(payload)

    return workitem
