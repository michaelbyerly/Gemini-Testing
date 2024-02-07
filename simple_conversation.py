"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import google.generativeai as genai

# API key
genai.configure(api_key="AIzaSyA--rVJsv2FGdPzJJ_1N8Fp_gxT1qcYa68")

# Model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Start a new conversation
convo = model.start_chat(history=[])

while True:
    # Take user input
    user_input = input("Enter your message (or type 'stop' to end): ")

    # Check if the user wants to stop the conversation
    if user_input.lower() == "stop":
        break

    # Send the message to the model
    convo.send_message(user_input)

    # Print the model's response
    print("\nResponse: ", convo.last.text, "\n")
