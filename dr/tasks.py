from celery import shared_task
from django.shortcuts import HttpResponse
from time import sleep
# from django.core.mail import send_mail
# for running the ssh script
import subprocess
import os
from django.conf import settings

@shared_task
def sleepy(duration):
    sleep(duration)
    return "Task Completed"

@shared_task
def execute_script():
    print("Inside script")
    # Path of shell script
    script_name = 'sample.ssh'  # Replace with the name of your script
    script_path = os.path.join(settings.STATIC_ROOT, script_name)
    print(script_path)
    # Call the shell script using subprocess.run()
    result = subprocess.run(["bash","D:\Work\Ekovolt\static_files\sample.sh"])

    # Check if the script executed successfully
    print("before running script")
    if result.returncode == 0:
        output = result.stdout
        print("this is output-->",output)
        return HttpResponse(f'Script executed successfully. Output: {output}')
    else:
        error_message = result.stderr
        print("this is output with error -->",error_message)
        return HttpResponse(f'Script execution failed. Error: {error_message}')

    # print("Inside script")
    #
    # # Path of shell script
    # script_name = 'sample.ssh'  # Replace with the name of your script
    # script_path = os.path.join(settings.STATIC_ROOT, script_name)
    # print("Script Path:", script_path)
    #
    # # Check if the script exists
    # if not os.path.exists(script_path):
    #     return HttpResponse(f'Script {script_name} not found.')
    #
    # # Call the shell script using subprocess.run()
    # try:
    #     result = subprocess.run(['bash', script_path], capture_output=True, text=True,
    #                             timeout=60)  # Set a timeout if needed
    #     print("before running script")
    #     print("Return Code:", result.returncode)
    #     print("output",result.stdout)
    #     print("error",result.stderr)
    #     if result.returncode == 0:
    #         output = result.stdout
    #         print("Output:", output)
    #         return HttpResponse(f'Script executed successfully. Output: {output}')
    #     else:
    #         error_message = result.stderr
    #         print("Error:", error_message)
    #         return HttpResponse(f'Script execution failed. Error: {error_message}')
    # except subprocess.TimeoutExpired:
    #     return HttpResponse('Script execution timed out.')
    # except Exception as e:
    #     return HttpResponse(f'Script execution failed. Exception: {str(e)}')
