import asyncio
import aiohttp
import time
import json  # Import the json module to read the request bodies from a JSON file

async def send_put_request(url, request_body):
    try:
        start_time = time.time()  # Record the start time
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=request_body) as response:
                response_body = await response.json()
                end_time = time.time()  # Record the end time
                response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
                print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
                if response.status == 200:
                    return response_body, True  # Mark the response as successful
                else:
                    return response_body, False  # Mark the response as unsuccessful
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return None, False

        

# Load request bodies from a JSON file
with open('input_instreams_startid.json', 'r') as file:
    request_bodies = json.load(file)

api_url = 'http://192.168.25.189/webapi/v1/settings/instreams'

api_urls_sequence = [
    ('http://192.168.25.189/webapi/v1/settings/instreams/startid/0', 'API URL Start ID 0'),
    ('http://192.168.25.189/webapi/v1/settings/instreams/startid/1', 'API URL Start ID 1'),
    ('http://192.168.25.189/webapi/v1/settings/instreams/startid/0', 'API URL Start ID 0'),
    ('http://192.168.25.189/webapi/v1/settings/instreams/startid/21', 'API URL Start ID 21'),
]

loop = asyncio.get_event_loop()

successful_count0 = 0  # Initialize a counter for successful requests
successful_count = 0

for i, request_body in enumerate(request_bodies):
    response_body, success = loop.run_until_complete(send_put_request(api_url, request_body))
    if response_body is not None:
        print(f'Response {i + 1}: {response_body}')
        if success:
            successful_count0 += 1  # Increment the successful count
total_request_bodies = len(request_bodies)
# Print the total number of successful requests
print(f'Total successful PUT requests: {successful_count0}/{total_request_bodies}')

print('__________________________________________________________________________________________________\n')

for i, (api_url, custom_message) in enumerate(api_urls_sequence):
    success = loop.run_until_complete(send_put_request(api_url, custom_message))
    if success:
        successful_count += 1  # Increment the successful count
    print(f'{custom_message} finished.\n')  # Print a custom message when the request is finished
    

# Print the total number of successful requests
print(f'Total successful Start ID requests: {successful_count}')

