# Text-to-Speech using gTTS and Pygame
## Dependencies
pygame
gTTS
You can install these dependencies using pip:


pip install pygame
pip install gTTS

## Usage
1. Change the text to be spoken in the tts = gTTS('') line, within the single quotes.
2. Save the text-to-speech audio file by running tts.save('output.mp3').
3. Load the audio file using Pygame mixer by running mixer.music.load('output.mp3').
4. Play the audio file by running mixer.music.play().

You can use this code as a starting point to create your own text-to-speech program.