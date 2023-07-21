import csv
import json

def generate(response):
    response = json.loads(response)
    content = response['choices'][0]['message']['content']

    # split content into lines
    lines = content.split('\n\n')

    # separate questions and answers
    qa_pairs = []
    for i in range(0, len(lines), 2):
        try:
            qa_pairs.append((lines[i], lines[i + 1]))
        except IndexError:  # handles the case where there is not an even number of lines
            qa_pairs.append((lines[i], ''))  # uses an empty string as the answer if there is no pair

    # write to CSV
    with open('answers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Answer"])
        writer.writerows(qa_pairs)

