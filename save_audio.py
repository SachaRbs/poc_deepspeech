import pyaudio
# from pynput import keyboard
import wave
import _thread


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 20
filename = "audio/voice_test.wav"


def input_thread(a_list):
    input()
    a_list.append(True)


def recording():
    p = pyaudio.PyAudio()
    input("press enter to start record")
    print('Recording')
    print("press enter to stop recording")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames
    a_list = []
    _thread.start_new_thread(input_thread, (a_list,))
    while not a_list:
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


recording()
