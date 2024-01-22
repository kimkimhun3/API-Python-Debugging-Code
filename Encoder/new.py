# import asyncio
# import aiohttp

# async def send_post_request(url):
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.post(url, json=request_body) as response:
#                 response_body = await response.json()
#                 print(f'Request to {url} - Status Code: {response.status}')
#                 return response_body
#     except Exception as e:
#         print(f'Error for {url}: {str(e)}')
#         return None

# api_url = 'http://192.168.25.189/webapi/v1/login'
# request_body = {
#     'username': 'user',
#     'password': 'user',
#     # Add more key-value pairs as needed
# }

# urls = [api_url] * 20

# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*[send_post_request(url) for url in urls]))

# for i, response_body in enumerate(results):
#     if response_body is not None:
#         print(f'Response {i + 1}: {response_body}')
#     else:
#         print(f'Response {i + 1} had an error.')

import asyncio
import aiohttp

async def send_post_request(url, request_body, request_number):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=request_body) as response:
                response_body = await response.json()
                print(f'Request {request_number} - Status Code: {response.status}')
                return response_body
    except Exception as e:
        print(f'Error for Request {request_number}: {str(e)}')
        return None

api_url = 'http://192.168.25.189/webapi/v1/login'
request_body = {
    'username': 'user',
    'password': 'user',
    # Add more key-value pairs as needed
}

urls = [api_url] * 20

loop = asyncio.get_event_loop()

request_number = 1  # Initialize request number

results = loop.run_until_complete(asyncio.gather(
    *[send_post_request(url, request_body, request_number + i) for i, url in enumerate(urls)]
))

for i, response_body in enumerate(results):
    if response_body is not None:
        print(f'Response {request_number + i} - {response_body}')
    else:
        print(f'Response {request_number + i} had an error.')



