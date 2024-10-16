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

api_url = 'http://192.168.25.189/webapi/v1/settings/instreams/active/1'
request_body = {
}
number_req = 1
urls = [api_url] * number_req

loop = asyncio.get_event_loop()

request_number = 10  # Initialize request number
success_counter = Counter()  # Initialize a success counter one time

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
