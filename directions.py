import json
import urllib.request
import xml
import xml.etree.ElementTree
import re
from tkinter import *


TAG_RE = re.compile(r"<[^>]+>")

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
img_endpoint = 'https://maps.googleapis.com/maps/api/streetview?'

key = 'AIzaSyAalSnw9kKlfIAEQkGlVT--Du5vOm-5Tw4'
img_key = "AIzaSyA7mv4dzuKQylITi6wZ5fbdFqr4lpJpi7A"
current_location = "UBCO Exchange, Transit Way, Kelowna, BC"
store_location = "Hudson's Bay, Harvey Avenue, Kelowna, British Columbia"


#making json file
#directions_string = json.dumps(directions)
#directions_json = open("directions.json", "w")
#directions_json.write(directions_string)
#directions_json.close()
#
def get_directions():  ##outer function to enable calling from predict module

    root = Tk()   #init window

    def cleanHTML(text):
        print(text)
        #return "".join(xml.etree.ElementTree.fromstring("<b>test</b>").itertext())
        return TAG_RE.sub('',text)

    def send():
 
        current_location = e.get()
        print(current_location)

        req = endpoint + "origin={} &destination={} &key={}".format(current_location,store_location,key).replace(" ","")
       ## img_req = img_endpoint + "size={} &location={} &key={}".format('600x400',store_location,img_key).replace(" ","")
        
        req_output = urllib.request.urlopen(req).read()
       ## img_req_output = urllib.request.urlopen(img_req)

        directions = json.loads(req_output)
        distance = directions['routes'][0]['legs'][0]['distance']['text']
        duration = directions['routes'][0]['legs'][0]['duration']['text']

        dir_to_user = ""

        for step in directions['routes'][0]['legs'][0]['steps']:
            dir_to_user += cleanHTML(step['html_instructions'])+ ' and continue for {}\n'.format(step['distance']['text']) 
            print(dir_to_user)
    
        res = "The shortest route is {} long and takes {} driving.\nDirections: \n".format(distance,duration) + dir_to_user
        bot_response = "> Bot: {0} ".format(res)
        txt.insert(END, "\n" + bot_response)
    

    txt = Text(root)
    txt.grid(row=0, column=0, columnspan=2) 
    e = Entry(root, width=50)
    send = Button(root, text="Speak", command=send).grid(row=1, column=1)
    e.grid(row=1, column=0)
    root.title("Customer Service Chatbot - Directions")
    txt.insert(END, "Please type-in your current location (Street adress, City, Province) and click on 'speak'")

    

    root.mainloop()     #close window
