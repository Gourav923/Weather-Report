import requests
# json used here for covert text to dictionary
import json
#pyttsx3 is tused to text to speech
import pyttsx3
h= pyttsx3.init() 
b='By By my friend'
while True:
    city=input('Enter name of the city\n') #take input from the user
    if city=='exit':
        print(b)
        h.say(b)
        h.runAndWait()
        break
    #6b5807874f994c97881103137243105&q this is api key I used in it
    url= f"https://api.weatherapi.com/v1/current.json?key=6b5807874f994c97881103137243105&q={city}"

    r= requests.get(url)

    #print(r.text)
   # #use this to get info in text and here all the info about weather in  in your preferred city
    wdic= json.loads(r.text)
    w= wdic['current']['temp_c']
    print(w)
  
    #this part is used to tell the temperature of the city that you entered
    h= pyttsx3.init()    
    h.say(f"The current weather in {city} is {w} degree celsius\n TThankyou to use my weather report speaker")
    h.runAndWait()
        