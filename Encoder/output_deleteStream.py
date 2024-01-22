# import asyncio
# import aiohttp
# import time
# import json  # Import the json module to read the request bodies from a JSON file

# async def send_put_request(url, request_body):
#     try:
#         start_time = time.time()  # Record the start time
#         async with aiohttp.ClientSession() as session:
#             async with session.put(url, json=request_body) as response:
#                 response_body = await response.json()
#                 end_time = time.time()  # Record the end time
#                 response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
#                 print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
#                 if response.status == 200:
#                     return response_body, True  # Mark the response as successful
#                 else:
#                     return response_body, False  # Mark the response as unsuccessful
#     except Exception as e:
#         print(f'Error for {url}: {str(e)}')
#         return None, False

# async def send_delete_request(url, request_body):
#     try:
#         start_time = time.time()  # Record the start time
#         async with aiohttp.ClientSession() as session:
#             async with session.put(url, json=request_body) as response:
#                 response_body = await response.json()
#                 end_time = time.time()  # Record the end time
#                 response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
#                 print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
#                 if response.status == 200:
#                     return response_body, True  # Mark the response as successful
#                 else:
#                     return response_body, False  # Mark the response as unsuccessful
#     except Exception as e:
#         print(f'Error for {url}: {str(e)}')
#         return None, False


# # Load request bodies from a JSON file
# with open('delete_reqbody.json', 'r') as file:
#     request_bodies = json.load(file)

# api_url = 'http://192.168.25.90/webapi/v1/settings/outstreams'
# api_url2 = 'http://192.168.25.90/webapi/v1/settings/outstreams/delete/2'

# loop = asyncio.get_event_loop()

# successful_count = 0  # Initialize a counter for successful requests
# delete_successful_count = 0
# for _ in range(10):
#     for i, request_body in enumerate(request_bodies):
#         response_body, success = loop.run_until_complete(send_put_request(api_url, request_body))
#         if response_body is not None:
#             print(f'Response {i + 1}: {response_body}')
#             if success:
#                 successful_count += 1  # Increment the successful count
#     total_request_bodies = len(request_bodies)
#     print(f'PUT successful requests: {successful_count}/{total_request_bodies}')

#     for i, request_body in enumerate(request_bodies):
#         response_body, success = loop.run_until_complete(send_delete_request(api_url2, request_body))
#         if response_body is not None:
#             print(f'Response {i + 1}: {response_body}')
#             if success:
#                 delete_successful_count += 1  # Increment the successful count
#     print(f'DELETE successful requests: {delete_successful_count}/{total_request_bodies}')

# # Print the total number of successful requests

# Now I have 2 API url endpoint.
# api_url1 = 'http://192.168.25.90/webapi/v1/settings/outstreams'
# api_url2 = 'http://192.168.25.90/webapi/v1/settings/outstreams/delete/{id}'
# api1_url1 need to have the body request from json file which contain the list of the 3 json body in the array
# api_url2 doesn't need any body to do the request. 
# Now I want to make the switcing request by first I want to run the api_url1 with the first body from the json file, then run the api_url2 by the {id} of the endpoint keep changing base on the {id} number. And keep this process until it finish the reqeust of the body from json file. 
# I want to change because my id is specific, firs I want id=2, then id=11 and last id=22.







# import asyncio
# import aiohttp
# import json
# import time

# # Define API URLs
# api_url1 = 'http://192.168.25.90/webapi/v1/settings/outstreams'
# api_url2_template = 'http://192.168.25.90/webapi/v1/settings/outstreams/delete/{id}'

# async def send_post_request(url, request_body):
#     try:
#         start_time = time.time()  # Record the start time
#         async with aiohttp.ClientSession() as session:
#             async with session.put(url, json=request_body) as response:
#                 end_time = time.time()  # Record the end time
#                 response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
#                 print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
#                 return response.status == 200
#     except Exception as e:
#         print(f'Error for {url}: {str(e)}')
#         return False

# async def send_delete_request(url):
#     try:
#         start_time = time.time()  # Record the start time
#         async with aiohttp.ClientSession() as session:
#             async with session.put(url) as response:
#                 end_time = time.time()  # Record the end time
#                 response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
#                 print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
#                 if response.status == 200:
#                     response_body = await response.text()
#                     print(f'Success\nResponse Body: {response_body}')
#                     print(f'Deleted ID: {url.split("/")[-1]}')  # Print the deleted ID
#                 else:
#                     response_body = await response.text()
#                     print(f'Error: {response.status}\nResponse Body: {response_body}')
#                 return response.status == 200
#     except Exception as e:
#         print(f'Error for {url}: {str(e)}')
#         return False

# # Load request bodies from a JSON file
# with open('delete_reqbody.json', 'r') as file:
#     request_bodies = json.load(file)

# # Define specific IDs for DELETE requests
# delete_ids = [0, 2, 12, 22]

# loop = asyncio.get_event_loop()

# successful_count = 0  # Initialize a counter for successful requests

# # Iterate through specific IDs
# for delete_id in delete_ids:
#     # Send a POST request to api_url1 with the current JSON body
#     success = loop.run_until_complete(send_post_request(api_url1, request_bodies[0]))
#     if success:
#         successful_count += 1  # Increment the successful count

#     # Construct the api_url2 with the specific {id}
#     api_url2 = api_url2_template.format(id=delete_id)

#     # Send a DELETE request to api_url2 with the specific {id}
#     success = loop.run_until_complete(send_delete_request(api_url2))

# # Print the total number of successful requests
# print(f'Total successful requests: {successful_count}')


import asyncio
import aiohttp
import json
import time

# Define API URLs
api_url1 = 'http://192.168.25.90/webapi/v1/settings/outstreams'
api_url2_template = 'http://192.168.25.90/webapi/v1/settings/outstreams/delete/{id}'

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

# Load request bodies from a JSON file
with open('delete_reqbody.json', 'r') as file:
    request_bodies = json.load(file)

# Specific IDs for DELETE requests
delete_ids = [2, 12, 22]

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

# Print the total number of successful requests
print(f'Total successful requests: {successful_count}')

