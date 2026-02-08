import requests
import json

# FleetDM API base URL
FLEETDM_API_URL = 'https://your_fleetdm_instance.com/api/v1'  # Replace with your actual FleetDM instance URL

# Device Enrollment function

def enroll_device(api_key, device_info):
    url = f'{FLEETDM_API_URL}/devices/enroll'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(device_info))
    return response.json()

# Track Unlock Events function

def track_unlock_event(api_key, event_info):
    url = f'{FLEETDM_API_URL}/devices/track_unlock'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(event_info))
    return response.json()

# Example usage
if __name__ == '__main__':
    API_KEY = 'your_api_key'  # Replace with your FleetDM API key

    # Device information for enrollment
    device_info = {
        'device_name': 'iPhone 14',
        'os': 'iOS',
        'serial_number': '123456789',
        'user': 'user@example.com'
    }

    # Enroll device
    enroll_response = enroll_device(API_KEY, device_info)
    print('Enroll Device Response:', enroll_response)

    # Event information for tracking unlock events
    unlock_event_info = {
        'device_id': '123456789',
        'event_time': '2026-02-08 00:19:29',
        'event_type': 'unlock'
    }

    # Track unlock event
    unlock_response = track_unlock_event(API_KEY, unlock_event_info)
    print('Track Unlock Event Response:', unlock_response)