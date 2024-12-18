"""
schedules an alarm using the android alarm manager

The actual scheduling is done inside the TaskScheduler java class in the
java_src/ folder which contains java files to be included in the app build


The implementation was done in java instead of python using jnius because of an
error that occurred when using the getClass() method of a reflected java class.
This error is likely related to the kivy version being used at the time of writing and may not be 
an issue with later versions hence should be easily implemented in python alone.
"""
# import json
# from datetime import datetime

from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
TaskExecutor = autoclass('org.test.myapp.TaskExecutor')


def schedule_task():
    """
    Schedules a task by calling the schedule task method of the TaskExecutor class
    The task itself is to run a service defined in the buildozer.spec file

    The current activity is passed when initializing the class because it is a
    requirement when using getSystemService() which is required to get the
    alarm manager.
    """
    # task_details = {'title': title, 'message': message}
    python_activity = PythonActivity.mActivity


    task_executor = TaskExecutor(python_activity)
    task_executor.triggerTask() # (json.dumps(task_details))

def cancel_task():
    """
    Cancel a scheduled task
    """
    # task_details = {'title': title, 'message': message}
    python_activity = PythonActivity.mActivity


    task_executor = TaskExecutor(python_activity)
    task_executor.cancelTask() # (json.dumps(task_details))
