import numpy as np
import pandas as pd
import json
import os
import random
import time
import tone_analyzer
import transcribe

def api_call():
    send_to_api = {}
    # Video to Speech to text conversion
    text = transcribe.transcribe_text()

    # Open the JSON file
    with open("D:\InterviewPro\static\\tone_analyzer\\answers.json", "r") as f:
        # Read the file contents into a string
        texts = f.read()
    # Tone analysis of the text
    def analyze_tone(text):
        res = tone_analyzer.main(text)
        return res

    send_to_api['Tone_analysis'] = analyze_tone(text)
    
    import openai
    try:
        # Set your OpenAI API key here
        api_key = "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"
        
            # Define the conversation as a list of messages
        conversation = [
            {"role": "system", "content": "You are a mentor providing feedback on the response."},
            {"role": "user", "content": "Can you help me improve my response to 'Tell me about yourself' in a job interview?"},
            {"role": "assistant", "content": "Of course! Please share your response to the question, and I'll provide feedback."},
            {"role": "user", "content": "Ayesha thank you for the opportunity to interview for the software engineer position at Google I am Alisha Sharma and I have a Software Engineer with three years of experience in the tech industry in my previous show that Amazon I was responsible for developing and maintaining large scale distributed systems I have a proven track record of success and building and deploying reliable and scalable software for example I like to development of new feature that increase user engagement by 10% I also have an experience of working at Microsoft skilled in Python Java and C plus plus oriented individual and I'm confident that I have the skills and experience necessary website about the opportunity to join Google because I am passionate about building products that make a difference in the world I'm also impressed by Google's commitment to engineering excellence and its culture of innovation confident that I can make a significant contribution to your team and eager to learn more about the software engineering process thank you for your time and consideration"},
        ]

        # Make an API call to OpenAI using the chat/completions endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can specify the model of your choice
            messages=conversation,
            api_key=api_key
        )
        # Get the generated response
        generated_text = response['choices'][0]['message']['content']

    except:
        with open('D:\InterviewPro\static\input_data.json', 'r') as json_file:
            data = json.load(json_file)
        generated_text = data['Speech']

        
    print('Speech Analysis Report :\n\n',generated_text)
    print('\n\n\n\n')
    send_to_api['Speech_analysis_report'] = generated_text
    # Print the generated text
    json_filename = "D:\InterviewPro\\api_output"
    # Save the list of dictionaries to a JSON file using json.dump()
    with open(json_filename, "w+") as json_file:
        json.dump(send_to_api, json_file, indent=6)  # The indent argument adds pretty-printing
    return send_to_api

api_call()
