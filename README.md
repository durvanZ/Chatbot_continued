# Hudson's Drip™ customer service AI Chatbot

  We created an Artificial-intelligence powered chatbot to serve the customers of our online clothing store: Hudson's Drip. We used an agile SDLC methodology, with our development cycle consisting of two scrums.
  
  Our software consists of two input JSON files used to train the neural network and make personalized answers based on customer information. The training.py imports data from intents.py and trains the neural network. training.py outputs words and classes pk1 files, which are used by the predict.py module to estimate the probability that a user input addresses a particular topic in the intents.JSON. A random response from the most likely topic is outputted by the chatbot. Our bot is also able to empathize with the user and take into account the mood of the user when generating responses.

Several libraries were used: tkntr, random, json, pickle, numpy, nltk (Porterstemmer, word net lemmatizer, Sentiment intensity analyzer), and tensorflow.

The Google Maps API was implemented.

[JIRA Roadmap](https://durvan.atlassian.net/jira/software/projects/CT3/boards/).  
[Reference material](https://www.youtube.com/watch?v=1lwddP0KUEg). 
  
## COSC 310 Group members:
- Guiherme Durvan António Zandamela
- Lakshay Karnwal
- Abdulaziz Almutlaq
- Ravil Bigvava
- Jordan onwuvuche

### Assignment 3 tasks:

#### GUI Implementation
![GUI Screenshot](https://raw.githubusercontent.com/durvanZ/COSC301_Team3/tree/main/screenshots/botdemo.png)

The GUI was implemented using the Python tkinter module for graphical interfaces. Using this module we created a text box where the user enters their query/text. This helps the app become intuitivey easy-to-use for the user.

#### Test cases implementation

The Automated Unit Testing Framework used for this was pytest due to its easy to use module functions. We created multiple test cases for all the important functions which checks if all the functions are working as desired. You can run the Unit testing file using the pytest command. After running the test file, pytest displays a summary of failed and passed functions. If the functions do not pass that means the chatbot will have errors, if all the functions pass that means the program is working as desired.

![Unit Testing Screenshot](https://user-images.githubusercontent.com/60047109/159101549-550633ec-41f7-408e-8fa5-5a43b64d2d75.png)

In the screenshot example above, one of the functions failed because the value of probability was not correct. This is a useful feature as it reduces effort to debug the code.

#### Sentiment analysis

We used a natural language toolkit "Sentiment intensity analyzer" to obtain positivity and negativity scores from the words in the user input. This information was used to make conditional statements in which the response of the bot is either complemented or replaced (depending on the intensity) by a response designed to address the sentiment of the user.

![Sentiment analysis demo](https://raw.githubusercontent.com/durvanZ/COSC301_Team3/main/screenshots/sentimentdemo.png)

#### Word stemming in ambiguous cases

Word stemming was used in addition to unstemmed input. Our algorithm stems the user input if the bot is not able to find a probable intent (probability > 0.50).
This helps to prevent inaccurate responses and can address suffixes.

![Sentiment analysis demo](https://raw.githubusercontent.com/durvanZ/COSC301_Team3/main/screenshots/sentimentdemo.png)

#### Google maps API

This feature enabls the user to ask for directions.

![Maps API](https://raw.githubusercontent.com/durvanZ/Chatbot_continued/master/screenshots/api.png)
