import csv
import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_KEY/env variable"


def read_csv(filename):
    messages = []
    count = 0;
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            message = row['Questions'].strip()
            count = count +1;
            if message:
                messages.append('Question ' + str(count) + ':' + message)
    return messages

#commenting out this function for now
'''
def chat_gpt_api_call(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" for faster response times
        messages=messages
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    csv_filename = 'questions.csv'
    messages = read_csv(csv_filename)

    if messages:
        api_response = chat_gpt_api_call(messages)
        print(api_response)
    else:
        print("No messages found in the CSV file.")
'''
