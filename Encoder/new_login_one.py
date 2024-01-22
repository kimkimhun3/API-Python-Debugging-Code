import asyncio
import aiohttp

async def send_post_request(url, request_body):  # Pass request_body as an argument
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=request_body) as response:
                response_body = await response.json()
                print(f'Request to {url} - Status Code: {response.status}')
                return response_body
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return None

# Define your API endpoint and request body
api_url = 'http://192.168.25.90/webapi/v1/login'
request_body = {
    'username': 'user',
    'password': 'user',
    # Add more key-value pairs as needed
}

urls = [api_url] * 20

loop = asyncio.get_event_loop()

# Send and process requests one by one
for i, url in enumerate(urls):
    response_body = loop.run_until_complete(send_post_request(url, request_body))
    if response_body is not None:
        print(f'Response {i + 1}: {response_body}')
    else:
        print(f'Response {i + 1} had an error.')
