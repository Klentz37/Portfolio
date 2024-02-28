import requests
from urllib.parse import urlencode
import base64
import webbrowser

# Function to obtain authorization code
def obtain_authorization_code(client_id, redirect_uri, scope):
    auth_headers = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope
    }

    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

    # Wait for the user to paste the authorization code obtained from the browser
    return input("Paste the authorization code obtained from the browser here: ")

# Function to obtain authorization token
def obtain_authorization_token(client_id, client_secret, code, redirect_uri):
    encoded_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }

    response = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None

# Function to retrieve currently playing track's artist and album
def get_currently_playing_track_info(access_token):
    user_headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    response = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=user_headers)
    if response.status_code == 200:
        current_track = response.json()["item"]
        song_name = current_track["name"]
        artist = current_track["artists"][0]["name"]  # Get the first artist's name
        album = current_track["album"]["name"]
        return {"song": song_name, "artist": artist, "album": album}
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None

def main():
    # Replace 'your_client_id' and 'your_client_secret' with your actual client ID and client secret
    client_id = ''
    client_secret = ''
    redirect_uri = "http://localhost:7777/callback"
    scope = "user-read-currently-playing"

    # Obtain authorization code
    code = obtain_authorization_code(client_id, redirect_uri, scope)

    # Obtain authorization token using authorization code
    access_token = obtain_authorization_token(client_id, client_secret, code, redirect_uri)
    if access_token:
        print("Access token:", access_token)
        # Retrieve currently playing track information
        currently_playing_track_info = get_currently_playing_track_info(access_token)
        if currently_playing_track_info:
            print("Currently playing track information:")
            print(currently_playing_track_info)
        else:
            print("No track is currently playing.")

if __name__ == '__main__':
    main()
