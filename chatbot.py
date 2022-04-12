from predict import *
from tkinter import *
from nltk import stem


cat_vids = "https://www.youtube.com/results?search_query=cat+videos"
dank_memes = "https://www.reddit.com/r/dankmemes/"
res = ""
stemmer = stem.PorterStemmer()
root = Tk()



def send():

    message = e.get()
    usermood = get_mood(message)
    empathy_response = ""
    negative_vibes = usermood.get('neg')
    positive_vibes = usermood.get('pos')

    gui_output = "> You: {0}".format(
        "*makes eye contact" if not message else message)
    txt.insert(END, "\n" + gui_output)

    # if bot not sure what it means, get new prediction this time using stemmed input
    # message is to stemmed and then converted back to string
    ints = predict_classes(message) 
    if float(ints[0].get('probability')) < 0.75 and ~(not message): 
        print("stemming")
        ints = predict_classes("".join(map(str, (stemmer.stem(x) for x in clean_up_sentence(message)))))

    response_predict = get_response(ints, intents)

    if (negative_vibes >= 0.55):
        empathy_response = random.choice(["I am really sorry to hear that.", "We're sorry about that...",
                                         ":(( That's so unfortunate.", "I understand your sentiment. Please allow me to help you, what do you need to know?"])
        res = empathy_response
        if (negative_vibes >= 0.65):
            response_predict += random.choice( ##replacement of predicted response
                [f"Here are some cat videos: {cat_vids}", f"Here are some dank memes: {dank_memes}"])
    elif (positive_vibes >= 0.7):
        empathy_response = random.choice([":)", "Happy spring!!!", "I'm glad that you're satistifed with my service.",
                                         "Fantastic!!!", "Awesome!", "I LOVE to hear that!", "You fill my heart with joy :))"])+"\n"

    final_response = "> Bot: {0} ".format(empathy_response) + response_predict
    txt.insert(END, "\n" + final_response)
    e.delete(0, END)


txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=50)
send = Button(root, text="Speak", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("Customer Service Chatbot")
txt.insert(END, "Click 'Speak' to interact with the customer service bot")

root.mainloop()
