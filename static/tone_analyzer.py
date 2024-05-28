import numpy as np
import pickle
import json
import joblib


def model_initialization(model_filename):
    '''Load the model from the .pkl file'''
    with open(model_filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    return loaded_model


def get_key(dict,val):
   
    for key, value in dict.items():
        if val == value:
            return key
        
def predict(X,model,vector):
    result_dict = {'Appreciative': 0,
                    'Diplomatic': 1,
                    'Direct': 2,
                    'Informative': 3,
                    'Thoughtful': 4,
                    'Witty': 5,
                    'Absurd': 6,
                    'Acerbic': 7,
                    'Admiring': 8,
                    'Aggressive': 9,
                    'Altruistic': 10,
                    'Ambivalent': 11,
                    'Apologetic': 12,
                    'Ardent': 13,
                    'Arrogant': 14,
                    'Assertive': 15,
                    'Belligerent': 16,
                    'Candid': 17}
    prob = model.predict_proba(vector.transform(X.split('.')))
    
    # Get the top 5 probabilities for each sample

    probabilities = []
    for i in range(len(prob[0])):
        pro = 0
        for j in range(len(prob)):
            pro += prob[j][i]
        probabilities.append(pro)
    probabilities.sort(reverse=True)
    probabilities = probabilities[:5]
    
    # Get the predicted classes for the top 5 probabilities
    full = sum(probabilities)
    probabilities = [prob/full for prob in probabilities]
    
    op = {}
    for i in range(len(probabilities)):
        op[get_key(result_dict,model.classes_[i])] = probabilities[i]
    json_file = sorted(op.items(), key=lambda x: x[1],reverse=True)[:5]
    for i in range(len(json_file)):
        json_file[i] = {json_file[i][0]:json_file[i][1]}
    return json_file


def json_output(outputs):
    # Specify the filename for the JSON file
    json_filename = "D:\InterviewPro\static\\tone_analyzer\output_tone_analyzer.json"
    # Save the list of dictionaries to a JSON file using json.dump()
    with open(json_filename, "w") as json_file:
        json.dump(outputs, json_file, indent=4)  # The indent argument adds pretty-printing



def main(texts):

    model_path = 'D:\\InterviewPro\\static\\tone_analyzer\\tone_analyzer.pkl'

    tfidf_vectorizer = joblib.load('D:\InterviewPro\static\\tone_analyzer\\tfidf_vectorizer.pkl')

    #input = "Hi Sarah, Thank you for the opportunity to interview for the Software Engineer position at Google. I'm Diya and I'm a Software Engineer with 3 years of experience in the tech industry. In my previous role at Amazon, I was responsible for developing and maintaining large-scale distributed systems. I have a proven track record of success in building and deploying reliable and scalable software. For example, I led the development of a new feature that increased user engagement by 10%. I'm also skilled in Python, Java, and C++. I'm a highly motivated and results-oriented individual, and I'm confident that I have the skills and experience necessary to be successful in this role. I'm excited about the opportunity to join Google because I'm passionate about building innovative products that make a difference in the world. I'm also impressed by Google's commitment to engineering excellence and its culture of innovation. I'm confident that I can make a significant contribution to your team and I'm eager to learn more about the Software Engineer position. Thank you for your time and consideration."
    model = model_initialization(model_path)
    tone_analysis_file = []
    overall_tone_analysis = {}
    for input in texts:
        outputs = predict(input,model,tfidf_vectorizer)
        tone_analysis_file.append(outputs)
        for item in outputs:
            tone = list(item.keys())[0]
            if tone not in overall_tone_analysis.keys():
                overall_tone_analysis[tone] = item[tone]
            else:
                overall_tone_analysis[tone] += item[tone]
    probs = list(overall_tone_analysis.values())
    probs.sort(reverse=True)
    probs = probs[:5]
    full = sum(probs)
    for key,prob in overall_tone_analysis.items():
        if prob in probs:
            overall_tone_analysis[key] = prob/full
    
    tone_analysis_file.append(overall_tone_analysis)

    import openai

    # Set your OpenAI API key here
    api_key = "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"

    # Define the conversation
    conversation = [
        {"role": "system", "content": "You are a mentor providing feedback on the tone analysis."},
        {"role": "user", "content": "Can you generate a report based on the tone analysis data?"},
        {"role": "assistant", "content": "Certainly! Please provide the tone analysis data you'd like the report for."},
        {"role": "user", "content": json.dumps({
            "Tone_analysis": tone_analysis_file
        })}
    ]
    try:
    # Make an API call to OpenAI using the chat/completions endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can specify the model of your choice
            messages=conversation,
            api_key=api_key
        )

        # Get the generated report
        generated_report = response['choices'][0]['message']['content']
    
    except:
        with open('D:\InterviewPro\static\input_data.json', 'r') as json_file:
            data = json.load(json_file)
            generated_report = data['Tone']

    # Print the generated report
    print("\n\n",generated_report)
    print('\n\n\n\n')

    file = {'Tone_analysis_percentage': overall_tone_analysis,'Tone_analysis_report':generated_report}

    return file
