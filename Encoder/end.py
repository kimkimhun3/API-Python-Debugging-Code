import requests
from concurrent.futures import ThreadPoolExecutor

# Define your API endpoint and request body
api_url = 'http://192.168.25.90/webapi/v1/settings/outstreams/active/0'
request_body = {
    'username': 'user',
    'password': 'user',
    # Add more key-value pairs as needed
}

# Function to send a single POST request
def send_post_request(url):
    try:
        response = requests.put(url, json=request_body)
        print(f'Request to {url} - Status Code: {response.status_code}')
    except Exception as e:
        print(f'Error for {url}: {str(e)}')

# Create a list of 100 identical URLs (the same endpoint)
urls = [api_url] * 1

# Use ThreadPoolExecutor to send requests concurrently
with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
    executor.map(send_post_request, urls)
