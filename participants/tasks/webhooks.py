from __future__ import absolute_import

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
