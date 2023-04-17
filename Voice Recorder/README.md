# Audio Recording with Python
This Python code records audio from your microphone and saves it to a WAV file.

## Prerequisites
You need to have Python installed on your system.
You also need to have the following Python packages installed:
sounddevice
scipy
You can install these packages using pip:


pip install sounddevice scipy

## Usage
Run the Python script using the command:

python voice_recorder.py

Enter the duration of the recording in seconds when prompted.

Speak into your microphone during the recording.

After the recording is finished, a WAV file named out.wav will be saved in the current directory.

## Customization
You can change the name of the output file by changing the argument of the write() function in the last line of the script.
You can change the sample rate and number of channels by changing the values of the fs and channels variables in the script.