# Billboard Top 100 Playlist Creator

This Python script allows you to create a Spotify playlist based on the Billboard Top 100 songs for a specific date. The playlist is automatically populated with tracks from the specified date, making it easy to travel back in time and enjoy the hits from that day.

## Features

- Fetch Billboard Top 100 songs for any given date.
- Search for these songs on Spotify.
- Create a private Spotify playlist containing these songs.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `spotipy`

## Setup

1. **Install Required Python Packages**

    Before running the script, you need to install the required Python libraries. You can do this by running the following command:

2. **Spotify API Credentials**

    You will need to register your application on the Spotify Developer Dashboard to obtain the `client_id` and `client_secret`. Set up a redirect URI that Spotify can call after authentication.

3. **Environment Variables**

    Replace `CLIENT-ID`, `CLIENT-SECRET`, and `USERNAME` in the script with your Spotify client ID, client secret, and username respectively. Also, update the `redirect_uri` with your redirect URI.

4. **Authorization**

    The script uses the `SpotifyOAuth` for authentication. The `scope` parameter is set to allow creating and modifying a private playlist.

## Usage

Run the script using Python. 

You will be prompted to enter a date in the format YYYY-MM-DD. After entering the date, the script will automatically fetch the top 100 songs from Billboard, search for them on Spotify, and create a playlist named <DATE> Billboard 100.
