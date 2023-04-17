import sounddevice as s
from scipy.io.wavfile import write
fs =44100
second = int(input("enter the time duration in seconds : "))
print("Recording.....\n")
record_voice = s.rec(int(second + fs),samplerate=fs, channels=2)
s.wait()
write("out.wav", fs,record_voice)
print("Finished... \nPlease check it...")
