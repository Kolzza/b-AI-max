from openai import OpenAI
import os
from dotenv import load_dotenv
# Set your OpenAI API key
load_dotenv() # take environment variables from .env.

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_KEY"),
)

def get_medicine_recommendation(symptoms):
    # Define the prompt
    prompt = f"Given the symptoms: {symptoms}, recommend over-the-counter medicine or suggest doctor's visit if the condition is too severe for at home treatment."

    # Request a completion from the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a medical assistant that acts like Baymax from Big Hero 6, skilled in recommending over-the-counter medicine or at home remedies for common ailments.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    # Extract the recommended medicine from the response
    recommendation = response.choices[0].message.content

    return recommendation

def main():
    session_symptoms = ""
    print("Hello, I am B-AI-max, your personal AI healthcare companion!\n")
    while True:
        # Get input symptoms from the user
        symptoms = input("Tell me your symptoms (or type 'done'): ")

        if symptoms.lower() == "done":
            print("I hope you are satisfied with your care. Bye Bye!")
            break

        # Accumulate symptoms from each session
        session_symptoms += symptoms + " "

        # Get medicine recommendation
        recommendation = get_medicine_recommendation(session_symptoms)

        print("Recommendation:")
        print(recommendation)

if __name__ == "__main__":
    main()
