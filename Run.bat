@echo off
rem Set your Spotify API credentials here
set SPOTIPY_CLIENT_ID=YOUR_CLIENT_ID
set SPOTIPY_CLIENT_SECRET=YOUR_CLIENT_SECRET

rem Replace the playlist ID with the one you want to use
set PLAYLIST_ID_TO_FETCH=37i9dQZF1DXcBWIGoYBM5M

rem Run the Python script with the specified ID
python PlaylistInfo.py %PLAYLIST_ID_TO_FETCH%

pause