import asyncio
import time

from decorator import Log
from exception import *

def division(x, y):
    if x == 0: raise CustomException("arg x must not be zero.")
    res = x // y
    return res

async def async_succeed_function():
    await asyncio.sleep(1)
    return {
        "result": division(2, 6)
    }

async def async_custom_exception_function():
    await asyncio.sleep(1)
    return {
        "result": division(0, 3)
    }

async def async_exception_function():
    await asyncio.sleep(1)
    return {
        "result": division(3, 0)
    }

async def succeed_function():
    time.sleep(1)
    return {
        "result": division(4, 2)
    }

async def custom_exception_function():
    time.sleep(1)
    return {
        "result": division(0, 5)
    }

async def exception_function():
    time.sleep(1)
    return {
        "result": division(2, 0)
    }

async def main():
    
    print("테스트 1: 요청 성공 시 로그 기록 (Async, Succeed)")
    try:
        await Log(
            log_data={
                "tag": "succeed"
            },
            func=async_succeed_function,
            args={}
        )
        print("테스트 1 성공")
    except CustomException:
        print("테스트 1 실패")
    except Exception:
        print("테스트 1 실패")

    print()
    print("테스트 2: 요청 실패 시 로그 기록 (Async, Custom Exception)")
    try:
        await Log(
            log_data={
                "tag": "custom_exception"
            },
            func=async_custom_exception_function,
            args={}
        )
        print("테스트 2 실패")
    except CustomException:
        print("테스트 2 성공")
    except Exception:
        print("테스트 2 실패")

    print()
    print("테스트 3: 요청 실패 시 로그 기록 (Async, Default Exception)")
    try:
        await Log(
            log_data={
                "tag": "exception"
            },
            func=async_exception_function,
            args={}
        )
        print("테스트 3 실패")
    except CustomException:
        print("테스트 3 실패")
    except Exception:
        print("테스트 3 성공")

    print()
    print("테스트 4: 요청 성공 시 로그 기록 (Sync, Succeed)")
    try:
        await Log(
            log_data={
                "tag": "succeed"
            },
            func=succeed_function,
            args={}
        )
        print("테스트 4 성공")
    except CustomException:
        print("테스트 4 실패")
    except Exception:
        print("테스트 4 실패")

    print()
    print("테스트 5: 요청 실패 시 로그 기록 (Sync, Custom Exception)")
    try:
        await Log(
            log_data={
                "tag": "custom_exception"
            },
            func=custom_exception_function,
            args={}
        )
        print("테스트 5 실패")
    except CustomException:
        print("테스트 5 성공")
    except Exception:
        print("테스트 5 실패")

    print()
    print("테스트 6: 요청 실패 시 로그 기록 (Sync, Default Exception)")
    try:
        await Log(
            log_data={
                "tag": "exception"
            },
            func=exception_function,
            args={}
        )
        print("테스트 6 실패")
    except CustomException:
        print("테스트 6 실패")
    except Exception:
        print("테스트 6 성공")

if __name__ == "__main__":
    asyncio.run(main())
