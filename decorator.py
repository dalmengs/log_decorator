from time import time
import traceback
import inspect
import json

from util import generate_id
from exception import *

"""
log_data -> dict
- user_id (str, optional)
- tag (str, required)

args -> dict
- function의 인자를 순서대로 dictionary 형태로 
"""

# Log Decorator
async def Log(log_data, func, args): 
    # Parameters
    data = {
        "log_id": generate_id(),
        "user_id": log_data["user_id"] if "user_id" in log_data else None,
        "status_code": 200,
        "tag": log_data["tag"],
        "execution_time": None,
        "request_data": json.dumps(args),
        "response_data": None
    }

    # Function Arguments
    args_list = [v for _, v in args.items()]

    try:
        # Function Execution
        if inspect.iscoroutinefunction(func): # async function
            t = time()
            result = await func(*args_list)
            data["execution_time"] = int((time() - t) * 1000)
        else: # default function
            t = time()
            result = func(*args_list)
            data["execution_time"] = int((time() - t) * 1000)
        data["response_data"] = json.dumps(result)
        return result
    except CustomException as e:
        data["status_code"] = e.status_code
        data["response_data"] = e.msg
        raise
    except Exception as e:
        data["status_code"] = 500
        data["response_data"] = traceback.format_exc()
        raise
    finally: # Insert log data
        f = open("./log/{}.json".format(data["log_id"]), "w")
        f.write(json.dumps(data, indent=4))
        f.close()

