import asyncio
import aiohttp
import json
import time

# Define API URLs
api_url1 = 'http://192.168.25.189/webapi/v1/settings/instreams'
api_url2_template = 'http://192.168.25.189/webapi/v1/settings/instreams/delete/2/{id}'
api_url3_template = 'http://192.168.25.189/webapi/v1/settings/instreams/delete/22/{id}'

#p2p
async def send_put_request(url, request_body):
    try:
        start_time = time.time()  # Record the start time
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=request_body) as response:
                end_time = time.time()  # Record the end time
                response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
                print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
                return response.status == 200
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return False

async def send_delete_request(url):
    try:
        start_time = time.time()  # Record the start time
        async with aiohttp.ClientSession() as session:
            async with session.put(url) as response:
                end_time = time.time()  # Record the end time
                response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
                print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
                if response.status == 200:
                    response_body = await response.text()
                    print(f'Success\nResponse Body: {response_body}')
                    print(f'Deleted ID: {url.split("/")[-1]}\n')  # Print the deleted ID
                else:
                    response_body = await response.text()
                    print(f'Error: {response.status}\nResponse Body: {response_body}')
                return response.status == 200
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return False


#srt
async def send_put_request_srt(url, request_body):
    try:
        start_time = time.time()  # Record the start time
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=request_body) as response:
                end_time = time.time()  # Record the end time
                response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
                print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
                return response.status == 200
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return False

async def send_delete_request_srt(url):
    try:
        start_time = time.time()  # Record the start time
        async with aiohttp.ClientSession() as session:
            async with session.put(url) as response:
                end_time = time.time()  # Record the end time
                response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
                print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
                if response.status == 200:
                    response_body = await response.text()
                    print(f'Success\nResponse Body: {response_body}')
                    print(f'Deleted ID: {url.split("/")[-1]}\n')  # Print the deleted ID
                else:
                    response_body = await response.text()
                    print(f'Error: {response.status}\nResponse Body: {response_body}')
                return response.status == 200
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return False

# Load request bodies from a JSON file
with open('p2p_delete_instreams_reqbody.json', 'r') as file:
    request_bodies = json.load(file)

# Load request bodies from a JSON file
with open('srt_delete_instreams_reqbody.json', 'r') as file:
    request_bodies_srt = json.load(file)

# Specific IDs for DELETE requests
delete_ids = [0,1]
delete_ids_srt = [0,1]


loop = asyncio.get_event_loop()

successful_count = 0  # Initialize a counter for successful requests

# Iterate through request bodies and specific IDs alternately
for i in range(max(len(request_bodies), len(delete_ids))):
    if i < len(request_bodies):
        current_request_body = request_bodies[i]
        # Send a PUT request to api_url1 with the current JSON body
        success = loop.run_until_complete(send_put_request(api_url1, current_request_body))
        if success:
            successful_count += 1  # Increment the successful count

    if i < len(delete_ids):
        current_delete_id = delete_ids[i]
        # Construct the api_url2 with the current {id}
        current_api_url2 = api_url2_template.format(id=current_delete_id)
        # Send a DELETE request to api_url2 with the current {id}
        success = loop.run_until_complete(send_delete_request(current_api_url2))
        if success:
            successful_count += 1  # Increment the successful count

#srt
for i in range(max(len(request_bodies_srt), len(delete_ids))):
    if i < len(request_bodies_srt):
        current_request_body = request_bodies_srt[i]
        # Send a PUT request to api_url1 with the current JSON body
        success = loop.run_until_complete(send_put_request_srt(api_url1, current_request_body))
        if success:
            successful_count += 1  # Increment the successful count

    if i < len(delete_ids_srt):
        current_delete_id = delete_ids_srt[i]
        # Construct the api_url2 with the current {id}
        current_api_url2 = api_url3_template.format(id=current_delete_id)
        # Send a DELETE request to api_url2 with the current {id}
        success = loop.run_until_complete(send_delete_request_srt(current_api_url2))
        if success:
            successful_count += 1  # Increment the successful count



# Print the total number of successful requests
print(f'Total successful requests: {successful_count}/8')


