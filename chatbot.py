import random
class HealthcareChatbot:
    def __init__(self):
        self.symptoms = {
            'fever': ['rest', 'drink fluids', 'consult a doctor if fever persists'],
            'cough': ['stay hydrated', 'use cough drops', 'see a doctor if cough is severe'],
            'headache': ['get some rest', 'take over-the-counter pain relievers', 'avoid bright lights'],
            'default': ["I'm not sure. It's best to consult a medical professional."]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if 'symptom' in user_input:
            return self.handle_symptom(user_input)
        elif 'appointment' in user_input:
            return "Sure, I can help you schedule an appointment. Please provide more details."
        elif 'emergency' in user_input:
            return "If this is a medical emergency, please call 108 immediately."
        elif 'thanks' in user_input:
                return "No problem,, I'll always be available."
        elif 'thank you' in user_input:
            return "I am greatful."
        elif 'bye' in user_input:
            return "please type exit."
        else:
            return "How can I assist you with your healthcare needs?"

    def handle_symptom(self, user_input):
        for symptom in self.symptoms:
            if symptom in user_input:
                return f"If you're experiencing {symptom}, you should: {', '.join(self.symptoms[symptom])}"
        return self.symptoms['default']


# Create an instance of the HealthcareChatbot class
chatbot = HealthcareChatbot()

# Main loop for interacting with the chatbot
print("Healthcare Support Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Healthcare Support Chatbot: Goodbye! Take care.")
        break
    response = chatbot.get_response(user_input)
    print("Healthcare Support Chatbot:", response)
