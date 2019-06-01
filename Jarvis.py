import pyttsx3
import datetime
import wikipedia
import lxml
from bs4 import BeautifulSoup
from googlesearch import search
import requests
import urllib
import os
import random
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print('==>JARVIS:'+'good morning master Reshab')
        speak("good morning master Reshab")
    elif hour >= 12 and hour < 19:
        print('==>JARVIS:'+'good evening master Reshab')
        speak("good evening master Reshab")
    else:
        pass
    print('==>JARVIS:'+'I am jarvis at your service how may i help you')
    speak('I am jarvis at your service how may i help you')

  

if __name__== "__main__" :
    reply="==>JARVIS:"
    WishMe()
    coin=['heads','tails']
    greetings=['Hi','Hey','hi','hey','hello','Hello','hola','Hola']
    foul_lang=['stupid','idiot','go to hell','noob','useless']
    question =['how are you doing?','how are you?','sup','are you ok?']
    jokes=['I don’t worry about terrorism. I was married for two years.','I don’t have a girlfriend, but I know a girl that would get really mad if she heard me say that']
    response=['okay','i am doing fine','amazing as mazing','blazing with motivation','fine,thanks for asking']
    while True:
        query=input(">>>Me:") 

        try:

            if 'music' in query:
                music_dir ='F:\MOVIES\Duck Tales'
                songs = os.listdir(music_dir)   
                os.startfile(os.path.join(music_dir, songs[0]))
        
            elif 'intro'in query:
                print(reply+"Hi, I'm Jarvis the AI assistant of Reshab")
                speak("Hi, I'm Jarvis the AI assistant of Reshab")


            elif query in greetings:
                gre_res=random.choice(greetings)
                print(reply+gre_res)
                speak(gre_res)
        
            elif query in foul_lang:
                print(reply+"i am sorry master but you should not use such language. I will improve myself")
                speak('i am sorry master but you should not use such language. I will improve myself')

            elif 'cmd' in query :
                os.system("cmd")
        
            elif 'jokes' in query or 'joke' in query:
                jok_res=random.choice(jokes)
                speak('this might make you laugh')
                print(reply+jok_res+" :)")
                speak(jok_res+":)")
                speak('hahahahah')

            elif 'repeat' in query:
                f=query.replace("repeat","")
                print(reply+f)
                speak(f)

            elif query in question:
                que_res=random.choice(response)
                print(reply+que_res)
                speak(que_res)

            elif 'exit'in query or 'bye' in query:
                print(reply+'Ok, Master Reshab , i am going offline')
                speak('Ok, Master Reshab , i am going offline')
                exit()

            elif 'restart' in query:
                check = input("Want to restart your computer ? (y/n): ") 
                if check=='n':
                    continue
                else:
                    os.system("shutdown /r /t 1")
            elif 'reshab' in query:
                print(reply+"Reshab is my creator, without him i wouldn't be here")
                speak("Reshab is my creator, without him i wouldn't be here")

            elif "coin" in query or 'flip' in query:
                flp_coin="it's " +random.choice(coin)
                print(reply+ flp_coin)
                speak(flp_coin)


            elif  'w'in query:
                query=query.replace('w','')
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(reply+results)
                speak(results)
            
            #elif 'g' in query:
                #query=query.replace('g','')'''
            else:
                speak('google search for')
                speak(query)
                for j in search(query,tld='co.in',lang='en',num=10,stop=1,pause=2):
                    pp=j
                    print(j)
                src = requests.get(pp).text
                soup=BeautifulSoup(src,'lxml')
                Title=soup.find('title').text
                print(Title)
                speak(Title)
            
        except Exception as e:
           # print(e)
            print(reply+'not a valid input or may internet is down')
            speak('not a valid input or may be internet is down')
            continue

        

    

    
  
  
  
  
  

        