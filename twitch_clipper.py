import requests
from decouple import config

# Load Twitch credentials from the .env file
TWITCH_CLIENT_ID = config('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET = config('TWITCH_CLIENT_SECRET')

# Define the Twitch API endpoints
TWITCH_API_BASE_URL = 'https://api.twitch.tv/helix'
CREATE_CLIP_URL = f'{TWITCH_API_BASE_URL}/clips'

# Define headers with authentication
headers = {
    'Client-ID': TWITCH_CLIENT_ID,
    'Authorization': f'Bearer {TWITCH_CLIENT_SECRET}',
}

def create_clip(broadcaster_id):
    # Parameters for creating a clip
    params = {
        'broadcaster_id': broadcaster_id,
    }

    try:
        # Send a POST request to create a clip
        response = requests.post(CREATE_CLIP_URL, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 201:
            clip_data = response.json()
            clip_url = clip_data['data'][0]['url']
            print(f'Clip created: {clip_url}')
        else:
            print(f'Error creating clip: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Error creating clip: {str(e)}')

if __name__ == '__main__':
    # Replace 'broadcaster_id' with the ID of the Twitch channel you want to clip
    broadcaster_id = 'your_broadcaster_id'

    create_clip(broadcaster_id)
