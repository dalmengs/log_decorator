# 로그 수집을 위한 로그 데코레이터

Metabase 같은 데이터베이스 통계 시각화 플랫폼이나 쿼리 기반 분석 플랫폼으로 로그 데이터를 분석하기 위해서는 로그 수집을 간편하게, 그리고 통일된 구조로 할 필요가 있다. </br></br>

이 데코레이터를 이용하면 함수 호출과 예외 처리에는 영향을 주지 않고, 수행하고자 하는 함수의 결과를 수집할 수 있다. </br></br>

# 프로젝트 실행하기

```
python main.py
```

# 프로젝트에 활용 시 주의 할 점 

1. `decorator.py`에 정의되어 있는 `Log` 메소드에서, 로그 삽입 로직 구현하기

`decorator.py`의 54번째 줄, `finally` 절 내부에 로그 데이터를 삽입하는 로직을 상황에 맞게 구현하면 된다.</br>
현재는 `log` 디렉토리에 `json` 형식으로 저장하도록 구현해두었으나, 실제 서비스에는 `requests`나 `aiohttp`같은 HTTP 요청 라이브러리로 대체되어야 할 것이다.

2. `Log` 함수 사용법 이해하기

``` python
result = await Log(
    log_data={
        "user_id": "..."
        "tag": "inference"
    },
    func=async_exception_function,
    args={}
)
```

- `result` 변수에는 호출하고자 하는 함수(`func`)의 결과값이 들어가게 된다.
- `log_data`는 추가로 저장할 필드이다.
  - `user_id`는 필수는 아니나, 사용자 별로 분석해야 하는 데이터인 경우에는 넣을 수 있다.
  - `tag는 필수이고, 상황 별로 데이터를 분석하기 위해 필요하다.
- `func`는 호출할 함수이고, 동기, 비동기에 관계없이 정상적으로 동작한다.
- `args`는 호출할 함수에 전달할 인자이다.
  - 함수 인자 순서대로 <strong>딕셔너리</strong>에 키와 값 형식으로 넣어 전달한다.

3. 로깅 결과 이해하기 

```python
{
    "log_id": "EESFKGPR914oI7CtVb6uiPU9iB69iJ",
    "user_id": null,
    "status_code": 200,
    "tag": "succeed",
    "execution_time": 1005,
    "request_data": "{}",
    "response_data": "{\"result\": 2}"
}
```

- `log_id`는 로그 데이터에 부여되는 고유 아이디이다.
- `status_code`는 요청 성공 여부이다.
  - 2xx는 성공, 4xx, 5xx는 실패를 나타낸다.
-  `execution_time`은 함수의 실제 실행 시간(ms)을 나타낸다.
  - 성능 분석을 위해 필요하다.
- `request_data`는 함수 요청 데이터이다.
- `response_data`는 함수 결과 데이터이다.