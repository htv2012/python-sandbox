import contextlib
import json
from typing import TypedDict


class CurlRequest(TypedDict):
    method: str
    path: str
    http_version: str
    headers: dict


class CurlResponse(TypedDict):
    http_version: str
    http_status: int
    reason: str
    headers: dict
    text: str
    json_data: dict


def parse_request(line: str, request: CurlRequest):
    if "HTTP/" in line:
        # Parse: '> GET /get?abc=1 HTTP/1.1'
        _, method, path, http_version = line.split()
        request["method"] = method
        request["path"] = path
        request["http_version"] = http_version
    elif ":" in line:
        # Parse: '> User-Agent: curl/8.1.2'
        key, value = [token.strip() for token in line.replace("> ", "").split(": ")]
        request["headers"][key] = value


def parse_response(line: str, response: CurlResponse):
    if "HTTP/" in line:
        # _, http_version, status, reason = line.split(" ", 3)
        tokens = line.split(None, 3)
        response["http_version"] = tokens[1]
        response["http_status"] = int(tokens[2])
        with contextlib.suppress(IndexError):
            response["reason"] = tokens[3]
    elif ":" in line:
        _, keyvalue = line.split(" ", 1)
        key, value = [token.strip() for token in keyvalue.split(": ")]
        response["headers"][key] = value


def parse_curl_output(text):
    request = CurlRequest(method=None, path=None, http_version=None, headers={})
    response = CurlResponse(
        http_version=None,
        http_status=None,
        reason=None,
        headers={},
        text=None,
        json_data=None,
    )
    for line in text.splitlines():
        if line.startswith("> "):
            parse_request(line, request)
        elif line.startswith("< "):
            parse_response(line, response)

    return {
        "request": request,
        "response": response,
    }


#
# Test
#
output = """*   Trying 54.205.233.15:80...
* Connected to httpbin.org (54.205.233.15) port 80 (#0)
> GET /get?abc=1 HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/8.1.2
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Thu, 28 Sep 2023 16:28:40 GMT
< Content-Type: application/json
< Content-Length: 277
< Connection: keep-alive
< Server: gunicorn/19.9.0
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Credentials: true
<
{
  "args": {
    "abc": "1"
  },
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "curl/8.1.2",
    "X-Amzn-Trace-Id": "Root=1-6515a9b8-2913f57d4293a3ac0519f194"
  },
  "origin": "50.204.110.16",
  "url": "http://httpbin.org/get?abc=1"
}
* Connection #0 to host httpbin.org left intact
"""

out = parse_curl_output(output)
print(json.dumps(out, indent=4))
