''' How to run pytest automated testing:
run command: pytest test.py
Uncomment the "from project import *" line'''


#from predict import *
import random
import numpy as np
import json
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import pytest  # we are using the pytest framework for automated unit testing

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
words = pickle.load(open('words.pk1', 'rb'))
intents = json.loads(open('intents.json').read())
#model= load_model('chatbot_model.h5')

# commented all the functions from the predict.py class


'''def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):  # convert sentence into a bag of word
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  # initial bag with just 0z
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_classes(sentence):
    bow = bag_of_words(sentence)  # create a bag of words
    # predicts classes based on the bag of words
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25  # certin threshold so not much uncertainty
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        # first one is the index next one is the result
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list  # return list full of intents and probabilities


def get_response(intents_list, intents_json):
    diagnostic = str(intents_list)
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = "Sorry, I can't understand what you mean, but here's my guess \n {0}".format(
        diagnostic)  # default output
    # print(list_of_intents)
    # print(tag)
    for i in list_of_intents:
        if i['topics'] == tag:
            # assigns output messages to be printed
            result = random.choice(i['outputs'])
            break
    return result'''


# three different test cases, to test the seperation of words, and to test the seperating of commas
def test_clean_up_sentence():
    test_cases = ["My name is Lakshay", "How do I order?", "Goodbye, see you"]
    expected_answers = ['My', 'name', 'is', 'Lakshay', 'How',
                        'do', 'I', 'order', '?',
                        'Goodbye', ',', 'see', 'you']
    answers = []

    for test_case in test_cases:
        answers = answers + clean_up_sentence(test_case)
        # print(answers)

    assert(answers == expected_answers)


# three different test cases to check the presence of lemmetized senetence in the intents (from intent.json)
def test_bag_of_words():
    test_case1 = "How do I return my order"
    test_case2 = "order details"
    test_case3 = "Hello"

    answer1 = bag_of_words(test_case1)
    answer2 = bag_of_words(test_case2)
    answer3 = bag_of_words(test_case3)

    expected_answer1 = [0] * len(words)
    expected_answer2 = [0] * len(words)
    expected_answer3 = [0] * len(words)

    indexes1 = [22, 23, 81, 131, 139, 151]
    indexes2 = [78, 139]

    for index1 in indexes1:
        expected_answer1[index1] = 1

    for index2 in indexes2:
        expected_answer2[index2] = 1

    expected_answer1 = np.array(expected_answer1)
    expected_answer2 = np.array(expected_answer2)
    expected_answer3 = np.array(expected_answer3)

    assert(np.array_equal(answer1, expected_answer1))
    assert(np.array_equal(answer2, expected_answer2))


# different test cases to predict the intent type along with its probablity
def test_predict_classes():
    answer1 = predict_classes("Refund item")
    expected_answer1 = [{'intent': 'returns', 'probability': '0.8146781'}]

    answer2 = predict_classes("Hello")
    expected_answer2 = [{'intent': 'greetings', 'probability': '0.68960893'}]

    answer3 = predict_classes("See you")
    expected_answer3 = [{'intent': 'goodbyes', 'probability': '0.99989593'}]

    assert answer1 == expected_answer1
    assert answer2 == expected_answer2
    assert answer3 == expected_answer3


# test case to check if the response is taken from the correct intent
def test_get_response():
    test_case = [{'intent': 'returns', 'probability': '0.8146781'}]
    res = get_response(test_case, intents)

    counter = 0
    list_of_intents = intents['intents']
    for i in list_of_intents:
        if i['topics'] == test_case[0]['intent']:
            for output in i['outputs']:
                if res == output:
                    counter = counter + 1
                    break

    assert counter == 1
