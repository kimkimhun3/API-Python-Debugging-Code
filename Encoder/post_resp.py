import requests
from concurrent.futures import ThreadPoolExecutor

# Define your API endpoint and request body
api_url = 'http://192.168.25.90/webapi/v1/login'
request_body = {
    'username': 'user',
    'password': 'user1',
    # Add more key-value pairs as needed
}

# Function to send a single POST request and return the response body
def send_post_request(url):
    try:
        response = requests.post(url, json=request_body)
        response_body = response.json()  # Assuming the response is in JSON format
        print(f'Request to {url} - Status Code: {response.status_code}')
        return response_body
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return None

# Create a list of 100 identical URLs (the same endpoint)
urls = [api_url] * 1

# Use ThreadPoolExecutor to send requests concurrently and collect response bodies
with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
    response_bodies = list(executor.map(send_post_request, urls))

# Now you have a list of response bodies from the POST requests
for i, response_body in enumerate(response_bodies):
    if response_body is not None:
        print(f'Response {i + 1}: {response_body}')
    else:
        print(f'Response {i + 1} had an error.')
