# LyricsGenius API usage
This code uses the lyricsgenius package to search for an artist and song lyrics using the Genius API.

## Prerequisites
You need to have a Genius account to get an API key, if you don't have one already. Visit https://genius.com/developers to create one.
Install the lyricsgenius package using pip. You can do this by running the command: pip install lyricsgenius
## Code Explanation
First, we import the lyricsgenius package and assign our API key to a variable named api_key.
We create an instance of the Genius class using our API key.
We use the search_artist method to search for an artist with the name "Pop Smoke" and limit the search to a maximum of 5 songs sorted by title.
We select a specific song by calling the song method of the Artist class and pass the title of the song as an argument.
Finally, we print the lyrics of the selected song using the lyrics attribute of the Song class.
## Note
Make sure to replace "83784testi" with your own API key.
You can change the artist and song name to search for different results.