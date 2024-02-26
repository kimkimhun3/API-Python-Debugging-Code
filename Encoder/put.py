import requests
from concurrent.futures import ThreadPoolExecutor

# Define your API endpoint and request body
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
"sync": 0,
"jitter": 30,
"function": 1,
"encoder_ip": "192.168.25.90",
"encoder_port": 50008,
"encryption": False,
"ttl": 1

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
urls = [api_url] * 2

# Use ThreadPoolExecutor to send requests concurrently
with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
    executor.map(send_post_request, urls)
import requests
from concurrent.futures import ThreadPoolExecutor

# Define your API endpoint and request body
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
"sync": 0,
"jitter": 30,
"function": 1,
"encoder_ip": "192.168.25.90",
"encoder_port": 50008,
"encryption": False,
"ttl": 1

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
urls = [api_url] * 2

# Use ThreadPoolExecutor to send requests concurrently
with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
    executor.map(send_post_request, urls)
