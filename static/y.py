import json

# Create a dictionary with two keys and their corresponding values
data = {
    "Tone": """Tone Analysis Report:

Appreciative: This tone is strongly expressed with a score of 0.327. In an interview context, this is a positive trait as it reflects a genuine appreciation or gratitude. It's important to maintain this tone as it creates a favorable impression.

Diplomatic: With a score of 0.259, the "Diplomatic" tone is moderately expressed. In interviews, diplomacy is a valuable quality as it signifies the ability to communicate with sensitivity and tact. Continue to maintain a diplomatic tone for effective communication.

Direct: The "Direct" tone is moderately expressed with a score of 0.240. In interviews, being direct is often a good quality as it indicates clarity and straightforward communication. Maintain this tone while ensuring it doesn't come across as overly blunt.

Informative: This tone is subtly expressed with a score of 0.089. In interviews, being informative is crucial, but a higher score could indicate a more detailed explanation of your points. Consider providing more information to enhance your responses.

Thoughtful: The "Thoughtful" tone is subtly expressed with a score of 0.085. In interviews, thoughtfulness can be a positive trait as it shows consideration and reflection. Maintain this tone while ensuring it doesn't lead to overly lengthy responses.

Areas of Improvement:

To enhance the "Informative" and "Thoughtful" tones, consider providing more detailed explanations, examples, or anecdotes in your responses. This will make your answers more informative and thoughtful without being excessively lengthy.
Constructive Criticism:

Your "Appreciative" tone is well-expressed, and it's a valuable quality in interviews. Keep up the good work in expressing genuine appreciation and gratitude.

The "Diplomatic" and "Direct" tones are both well-balanced. Continue to be diplomatic in your communication while maintaining directness when needed.

Overall, your tone analysis suggests a good balance in your interview responses. Focus on providing more information for the "Informative" tone and ensuring that "Thoughtful" responses remain concise and relevant. Your strengths in "Appreciative," "Diplomatic," and "Direct" tones are commendable.
""",
    "Speech": """Overall, your response is quite strong and provides relevant information about your experience and skills. However, there are a few areas where you can make improvements:

1. Start with a brief introduction: Instead of immediately mentioning the specific position and company, begin by giving a concise introduction of yourself as a software engineer. For example, "I am a software engineer with three years of experience in the tech industry."

2. Highlight your achievements: While you mention your experience at Amazon and your responsibilities, try to focus more on your accomplishments and specific impact. For example, instead of just mentioning that you developed and maintained large-scale distributed systems, elaborate on the results you achieved through those projects. Mention the successful implementation of features, any improvements in user engagement or performance, or any recognition you received for your work.

3. Tailor your skills: While you mention being skilled in Python, Java, and C++, it's better to align your skills with the requirements of the position you're applying for. If possible, highlight specific skills or technologies that are most relevant to the job at Google, such as experience with cloud platforms, machine learning, or web development frameworks.

4. Express enthusiasm and alignment with the company: You briefly mention being passionate about building products that make a difference, but consider expanding on this to show a deeper understanding of Google's values and products. Mention specific projects or innovations from Google that inspire you and align with your interests.

5. Be more concise: Your response is a bit lengthy. Try to condense and prioritize your key points, focusing on the most relevant and impressive aspects of your experience.

Rewritten response:

"Thank you, Ayesha, for the opportunity to interview for the software engineer position at Google. I am Alisha Sharma, a software engineer with three years of experience in the tech industry. During my time at Amazon, I successfully developed and maintained large-scale distributed systems, achieving notable results such as a 10% increase in user engagement through the implementation of new features.

I have a strong skillset in Python, Java, and C++, with a particular focus on creating reliable and scalable software. I'm excited about the opportunity to join Google and contribute to their mission of building products that have a positive impact on the world. The commitment to engineering excellence and culture of innovation at Google is particularly inspiring to me.

I am confident that my skills and experience will allow me to make a significant contribution to your team. I'm eager to continue learning and developing my expertise in software engineering, and I look forward to exploring this further during the interview process.

Thank you for considering my application, and I appreciate your time."

Remember, this is just a suggestion, and you should personalize it further based on your own experiences and the specific requirements of the job you're applying for. Good luck with your interview!
"""
}

# Specify the file path where you want to save the JSON file
file_path = "static/input_data.json"

# Write the dictionary to a JSON file
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON data has been saved to '{file_path}'")