import openai

openai.api_key = "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"

# Prompt the user to enter the press release text
with open('press_release.txt', 'r', encoding='utf-8') as f:
    press_release_text = f.readlines()

while True:
    # Prompt the user to enter a question or exit
    user_input = input("Enter a question or type 'exit' to quit: ")
    
    if user_input.lower() == "exit":
        break
        
    # Define the prompt for the chatbot
    prompt = (f"I have some questions about the following press release:"
              f"\n{press_release_text}"
              f"\n\nQuestion: {user_input}"
              )

    # Define the parameters for the completion
    params = {
        "engine": "text-davinci-002",
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(**params)

    # Extract the answer from the response
    answer = response.choices[0].text.strip()

    # Print the answer
    print(answer)
