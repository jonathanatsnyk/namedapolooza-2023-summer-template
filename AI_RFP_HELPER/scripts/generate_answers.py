import csv
import json

def generate(response):
    response = json.loads(response)
    content = response['choices'][0]['message']['content']

    # split content into answers
    answers = content.split('Answer to Question')[1:]  # splitting by 'Answer to Question' and skipping the first element to exclude any leading text

    # clean up answers (remove numbers and extra spaces)
    answers = [answer.split(': ')[1].strip() for answer in answers]

    # write to CSV
    with open('answers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Answer"])  # header
        for answer in answers:
            writer.writerow([answer])

