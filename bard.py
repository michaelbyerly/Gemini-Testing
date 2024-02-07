import requests
import json

def generate_content(api_key, query):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": query}
                ]
            }
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()  # Parse the response as JSON

def main():
    api_key = input("Enter API Key: ")
    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        response_json = generate_content(api_key, query)

        # Extracting the 'text' part from the response
        if 'candidates' in response_json and len(response_json['candidates']) > 0:
            text_response = response_json['candidates'][0]['content']['parts'][0]['text']
            print("\nResponse:\n" + text_response + "\n")
        else:
            print("No valid response received.")

if __name__ == "__main__":
    main()
