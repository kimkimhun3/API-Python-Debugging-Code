import asyncio
import aiohttp

async def send_put_request(url, request_body, request_number, success_counter):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=request_body) as response:
                response_body = await response.json()
                print(f'Request {request_number} to {url} - Status Code: {response.status}')
                if response.status == 200:
                    success_counter.increment()  # Increment the success counter
                return response_body
    except Exception as e:
        print(f'Error for Request {request_number} to {url}: {str(e)}')
        return None

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

api_url = 'http://192.168.25.189/webapi/v1/settings/outstreams'
request_body = {
    "id": 1,
    "view": 0,
    "ip_multi": False,
    "recv_ip": "",
    "recv_port": 5004,
    "v_codec": "hevc",
    "a_codec": "none",
    "two_way_audio": False,
    "two_way_ip": "",
    "two_way_port": "",
    "a_bitrate": "320",
    "a_bitrate_custom": "",
    "sync": 2,
    "jitter": 300,
    "function": 2,
    "encoder_ip": "192.168.25.90",
    "encoder_port": 50008,
    "encryption": False,
    "ttl": 1,
}
number_req = 50
urls = [api_url] * number_req

loop = asyncio.get_event_loop()

request_number = 1  # Initialize request number
success_counter = Counter()  # Initialize a success counter

results = loop.run_until_complete(asyncio.gather(
    *[send_put_request(url, request_body, request_number + i, success_counter) for i, url in enumerate(urls)]
))

for i, response_body in enumerate(results):
    if response_body is not None:
        print(f'Response {request_number + i}: {response_body}')
    else:
        print(f'Response {request_number + i} had an error.')

# Print the total number of successful requests
print(f'Total successful requests: {success_counter.value}/{number_req}')
