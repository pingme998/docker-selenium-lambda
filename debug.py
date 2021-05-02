import os
import subprocess
from test import handler
import json
import shutil
import threading

text = []


def func(event, context):
    try:
        text.append(handler(event, context))
    except Exception as e:
        text.append(str(e))


def debug(event=None, context=None):
    text.clear()
    for filename in os.listdir('/tmp'):
        file_path = os.path.join('/tmp', filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            pass
    event = event if event is not None else {}
    thread = threading.Thread(target=func, args=([event, context]))
    thread.daemon = True
    thread.start()
    thread.join(timeout=15)
    text.extend([
        *subprocess.run(
            ['find', '/tmp', '-print'], capture_output=True, text=True).stdout.split("\n"),
        event,
        subprocess.run(
            ['cat', '/tmp/user-data-dir/chrome_debug.log'], capture_output=True, text=True).stdout.split("\n"),
    ])
    return text


if __name__ == '__main__':
    from pprint import pprint
    with open('args.json') as json_file:
        pprint(debug(event=json.load(json_file)))
