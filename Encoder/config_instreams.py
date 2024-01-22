# import requests
# from concurrent.futures import ThreadPoolExecutor

# # Define your API endpoint and request body
# api_url = 'http://192.168.25.189/webapi/v1/settings/instreams'
# request_body = {
#     "id": 1,
#     "view": 0,
#     "ip_multi": False,
#     "recv_ip": "",
#     "recv_port": 5004,
#     "v_codec": "hevc",
#     "a_codec": "none",
#     "two_way_audio": False,
#     "two_way_ip": "",
#     "two_way_port": "",
#     "a_bitrate": "320",
#     "a_bitrate_custom": "",
#     "sync": 2,
#     "jitter": 300,
#     "function": 2,
#     "encoder_ip": "192.168.25.90",
#     "encoder_port": 50008,
#     "encryption": False,
#     "ttl": 1,
# }

# # Function to send a single POST request and return the response body
# def send_put_request(url):
#     try:
#         response = requests.put(url, json=request_body)
#         response_body = response.json()  # Assuming the response is in JSON format
#         print(f'Request to {url} - Status Code: {response.status_code}')
#         return response_body
#     except Exception as e:
#         print(f'Error for {url}: {str(e)}')
#         return None

# # Create a list of 100 identical URLs (the same endpoint)
# urls = [api_url] * 1

# # Use ThreadPoolExecutor to send requests concurrently and collect response bodies
# with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
#     response_bodies = list(executor.map(send_put_request, urls))

# # Now you have a list of response bodies from the POST requests
# for i, response_body in enumerate(response_bodies):
#     if response_body is not None:
#         print(f'Response {i + 1}: {response_body}')
#     else:
#         print(f'Response {i + 1} had an error.')



import asyncio
import aiohttp

async def send_put_request(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=request_body) as response:
                response_body = await response.json()
                print(f'Request to {url} - Status Code: {response.status}')
                return response_body
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return None

api_url = 'http://192.168.25.189/webapi/v1/settings/instreams'
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

urls = [api_url] * 20

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*[send_put_request(url) for url in urls]))

for i, response_body in enumerate(results):
    if response_body is not None:
        print(f'Response {i + 1}: {response_body}')
    else:
        print(f'Response {i + 1} had an error.')

# import asyncio
# import aiohttp

# async def send_put_request(url, request_body, request_number):
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.put(url, json=request_body) as response:
#                 response_body = await response.json()
#                 print(f'Request {request_number} to {url} - Status Code: {response.status}')
#                 return response_body
#     except Exception as e:
#         print(f'Error for Request {request_number} to {url}: {str(e)}')
#         return None

# api_url = 'http://192.168.25.189/webapi/v1/settings/instreams'
# request_body = {
#     "id": 1,
#     "view": 0,
#     "ip_multi": False,
#     "recv_ip": "",
#     "recv_port": 5004,
#     "v_codec": "hevc",
#     "a_codec": "none",
#     "two_way_audio": False,
#     "two_way_ip": "",
#     "two_way_port": "",
#     "a_bitrate": "320",
#     "a_bitrate_custom": "",
#     "sync": 2,
#     "jitter": 300,
#     "function": 2,
#     "encoder_ip": "192.168.25.90",
#     "encoder_port": 50008,
#     "encryption": False,
#     "ttl": 1,
# }

# urls = [api_url] * 20

# loop = asyncio.get_event_loop()

# request_number = 1  # Initialize request number

# results = loop.run_until_complete(asyncio.gather(
#     *[send_put_request(url, request_body, request_number + i) for i, url in enumerate(urls)]
# ))

# for i, response_body in enumerate(results):
#     if response_body is not None:
#         print(f'Response {request_number + i}: {response_body}')
#     else:
#         print(f'Response {request_number + i} had an error.')



