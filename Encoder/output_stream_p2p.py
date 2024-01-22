import asyncio
import aiohttp
import time

async def send_put_request(url, request_body):
    try:
        start_time = time.time()  # Record the start time
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=request_body) as response:
                response_body = await response.json()
                end_time = time.time()  # Record the end time
                response_time_ms = (end_time - start_time) * 1000  # Calculate response time in milliseconds
                print(f'Request to {url} - Status Code: {response.status}, Response Time: {response_time_ms:.2f} ms')
                return response_body
    except Exception as e:
        print(f'Error for {url}: {str(e)}')
        return None

# Define a list of request bodies (16 request bodies)
request_bodies = [
    {"id": 1,	
    "v_codec": "hevc",	
    "coding_mode": "lfn",	
    "resolution": "auto",	
    "resolution_w": "",	
    "resolution_h": "",	
    "v_bitrate": "25000",	
    "v_bitrate_custom": "",	
    "v_framerate": "auto",	
    "a_codec": "none",	
    "a_bitrate": "",	
    "a_bitrate_custom": "",	
    "two_way_audio": False,	
    "two_way_ip_multi": False,	
    "two_way_ip": "",	
    "two_way_port": "",	
    "two_way_latency": "",	
    "two_way_volume": "",	
    "multiple_delivery": False,	
    "ip1_ipaddress": "239.1.2.3",	
    "ip1_dport": 5004,	
    "ip1_sport": "",	
    "ip2_ipaddress": "",	
    "ip2_dport": "",	
    "ip3_ipaddress": "",	
    "ip3_dport": "",	
    "ip4_ipaddress": "",	
    "ip4_dport": "",	
    "function": 0,	
    "encryption": False,	
    "ip_dscp": 0,	
    "ttl": 128,	
    "intra_type": "slice",	
    "minq": 0,	
    "rtp_mtu": 1400,	
    "storage_file": "off",	
    "storage_path": ""	},
    {"id": 1,	
    "v_codec": "avcM",	
    "coding_mode": "nbn",	
    "resolution": "1920x1080",	
    "resolution_w": "",	
    "resolution_h": "",	
    "v_bitrate": "10000",	
    "v_bitrate_custom": "",	
    "v_framerate": "30",	
    "a_codec": "aac",	
    "a_bitrate": "320",	
    "a_bitrate_custom": "",	
    "two_way_audio": True,	
    "two_way_ip_multi": False,	
    "two_way_ip": "",	
    "two_way_port": "7004",	
    "two_way_latency": "30",	
    "two_way_volume": "50",	
    "multiple_delivery": False,	
    "ip1_ipaddress": "192.168.25.89",	
    "ip1_dport": 6004,	
    "ip1_sport": "60004",	
    "ip2_ipaddress": "",	
    "ip2_dport": "",	
    "ip3_ipaddress": "",	
    "ip3_dport": "",	
    "ip4_ipaddress": "",	
    "ip4_dport": "",	
    "function": 1,	
    "encryption": True,	
    "ip_dscp": 63,	
    "ttl": 1,	
    "intra_type": "vframe",	
    "minq": 51,	
    "rtp_mtu": 1000,	
    "storage_file": "off",	
    "storage_path": ""	},
    # Add more request bodies as needed
]

api_url = 'http://192.168.25.90/webapi/v1/settings/outstreams'

loop = asyncio.get_event_loop()

for i, request_body in enumerate(request_bodies):
    response_body = loop.run_until_complete(send_put_request(api_url, request_body))
    if response_body is not None:
        print(f'Response {i + 1}: {response_body}')
    else:
        print(f'Response {i + 1} had an error.')
