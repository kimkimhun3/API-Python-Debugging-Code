import asyncio
import aiohttp

async def send_put_request(url, request_body):  # Pass request_body as an argument
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=request_body) as response:
                response_body = await response.json()
                print(f'Request to {url} - Status Code: {response.status}')
                return response_body
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return None

api_url = 'http://192.168.25.189/webapi/v1/settings/instreams/active/2'
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
    "jitter": 100,
    "function": 2,
    "encoder_ip": "192.168.25.90",
    "encoder_port": 50008,
    "encryption": False,
    "ttl": 1,
}

urls = [api_url] * 20

loop = asyncio.get_event_loop()

# Send and process requests one by one
for i, url in enumerate(urls):
    response_body = loop.run_until_complete(send_put_request(url, request_body))
    if response_body is not None:
        print(f'Response {i + 1}: {response_body}')
    else:
        print(f'Response {i + 1} had an error.')











# Response Time
# import asyncio
# import aiohttp
# import time

# async def send_put_request(url, request_body):
#     try:
#         start_time = time.time()  # Record the start time
#         async with aiohttp.ClientSession() as session:
#             async with session.put(url, json=request_body) as response:
#                 response_body = await response.json()
#                 end_time = time.time()  # Record the end time
#                 response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
#                 print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
#                 return response_body
#     except Exception as e:
#         print(f'Error for {url}: {str(e)}')
#         return None

# api_url = 'http://192.168.25.189/webapi/v1/settings/instreams/active/2'
# request_body = {}

# urls = [api_url] * 20

# loop = asyncio.get_event_loop()

# for i, url in enumerate(urls):
#     response_body = loop.run_until_complete(send_put_request(url, request_body))
#     if response_body is not None:
#         print(f'Response {i + 1}: {response_body}')
#     else:
#         print(f'Response {i + 1} had an error.')
