import moviepy.editor as mp 
import speech_recognition as sr 

def transcribe_text ():
    # Load the video 
    video = mp.VideoFileClip("D:\InterviewPro\static\speech_to_text\Interview_1.mp4") 
    # Extract the audio from the video 
    audio_file = video.audio 
    audio_file.write_audiofile("D:\InterviewPro\static\speech_to_text\Interview_1.wav") 
    
    # Initialize recognizer 
    r = sr.Recognizer() 
    
    # Load the audio file 
    with sr.AudioFile("D:\InterviewPro\static\speech_to_text\Interview_1.wav") as source: 
        data = r.record(source) 
    
    # Convert speech to text 
    text = r.recognize_google(data)
    print(text)
    print('\n\n\n')
    return text