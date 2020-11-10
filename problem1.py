import csv
import json

def setup():
    with open('input.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        json_file = []
        for row in csv_reader:
            data = {}
            data['category_path'] = row["category_path"]
            data['questions'] = row["questions"]
            data['content'] = row["content"]
            json_file.append(data)

    with open('input.json', 'w') as outfile:
        json.dump(json_file, outfile, indent=4)
    return

def wordCounter(dictionary, words):
    for word in words:
        if word in dictionary:
            dictionary[word] +=1
        else:
            dictionary[word] = 1
    return


def main():
    setup()
    dict_category = {}
    dict_questions = {}
    dict_content = {}
    with open('input.json') as json_file:
        x = json.load(json_file)
        for row in x:
            word_category = row['category_path'].split()
            word_question = row['questions'].split()
            word_content = row['content'].split()
            wordCounter(dict_category, word_category)
            wordCounter(dict_questions, word_question)
            wordCounter(dict_content, word_content)
    sorted_dictionary = {"category_path":dict_category, "questions":dict_questions, "content":dict_content}
    with open('Word.json', 'w') as outfile:
        json.dump(sorted_dictionary, outfile, indent=4)
    return


if __name__ == '__main__':
    main()