from bs4 import BeautifulSoup
import re 
import requests
import random
import webbrowser


def getMovie(mood): 
    url='http://www.imdb.com/search/title?genres='
    end='&title_type=feature&sort=moviemeter, asc'
    recomendaciones={
        "sad":url+'drama'+end,
        "disgust":url+'sci-fi'+end,
        "angry": url+'action'+end,
        "fear":url+'horror'+end,
        "happy":url+'comedy'+end,
        "neutral":url+'comedy,romance'+end,
        "surprise":url+'mystery'+end
        }
    res = requests.get(recomendaciones[mood]) 
    soup=BeautifulSoup(res.text, "html.parser")
    results=soup.select(".lister-item.mode-advanced h3 a")
    movies=[movie.text for movie in results]
    print("How many recommendations do you want? Please type in a number.")
    number_movies=int(input("You: "))
    if len(movies)<number_movies:
        print(f"Please insert a number no greater than {len(movies)}.")
        getMovie(mood)
    else:
        print(random.sample(movies,number_movies))
    return movies

def int_check(l,h,user_input): #for inputting integers
    s = int(user_input)
    if l<=s<=h:
        return s
            

def getWeb(mood):
    if mood=='happy':
        webbrowser.open("https://www.happify.com")
    elif mood=='sad': 
        a = int_check(1,2,"\n\nWhat link would you like to view?\n1. 39 Pictures For Anyone Who Is Just Sad\n2. 42 Pictures That Will Make You Almost Too Happy\n\nPlease select a corresponding integer: ")
        if a==1:
            webbrowser.open("https://www.buzzfeed.com/jasminnina/25-images-that-will-make-you-realize-it-could-be-worse")
        elif a==2:
            webbrowser.open("https://www.buzzfeed.com/jimwaterson/pictures-of-happy-men-with-giant-vegetables")
    elif mood=='angry': 
        a = int_check(1,2,"\n\nWhat link would you like to view?\n1. 21 Pictures That Will Definitely Make You Feel Better\n2. 28 Pictures That Will Help You Calm The Hell Down Today\n\nPlease select a corresponding integer: ")
        if a==1:
            webbrowser.open("https://www.buzzfeed.com/pampers/ways-to-smile-like-a-happy-happy-baby")
        elif a==2:
            webbrowser.open("https://www.buzzfeed.com/alexnaidus/pictures-of-food-that-will-soothe-you-and-make-you-hungry")
    elif mood=='neutral': 
        a = int_check(1,2,"\n\nWhat link would you like to view?\n1. Give Yourself A Relaxing Day Off With These 24 Products\n2. 12 Perfect GIFs To Keep You Relaxed & Soothe Your Spirit \n\nPlease select a corresponding integer: ")
        if a==1:
            webbrowser.open("https://www.buzzfeed.com/mugdhakusray/give-yourself-a-day-off-with-these-products-52982rd8tw")
        elif a==2:
            webbrowser.open("https://www.buzzfeed.com/adamjkurtz/handwriting-plus-sunsets-equals-art")
    elif mood=='surprise':
        webbrowser.open("https://www.buzzfeed.com/pepsimaxuk/photos-with-unbelievable-hidden-surprises")


def getSong(mood):
    if mood=='happy':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0')
    elif mood=='sad':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0')
    elif mood=='angry':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0')
    elif mood=='neutral':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7')
    elif mood=='surprise':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DXcZK031Zeh47?si=WlZ6V-bNQOWGS5T7uD53WQ')


    

  

