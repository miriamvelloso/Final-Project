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
    movies=random.sample(movies,3)
    return ", ".join(movies)

def int_check(l,h,user_input): #for inputting integers
    s = int(user_input)
    if l<=s<=h:
        return s
            

def getWeb(mood):
    recomendaciones={
        "sad":"https://www.buzzfeed.com/jasminnina/25-images-that-will-make-you-realize-it-could-be-worse",
        "disgust":"https://www.happify.com",
        "angry": "https://www.buzzfeed.com/alexnaidus/pictures-of-food-that-will-soothe-you-and-make-you-hungry",
        "fear":"https://www.buzzfeed.com/pepsimaxuk/photos-with-unbelievable-hidden-surprises",
        "happy":"https://www.happify.com",
        "neutral":"https://www.buzzfeed.com/mugdhakusray/give-yourself-a-day-off-with-these-products-52982rd8tw",
        "surprise":"https://www.buzzfeed.com/pepsimaxuk/photos-with-unbelievable-hidden-surprises"
        }
    
    return webbrowser.open(recomendaciones[mood])
    

def getPlaylist(mood):
    url="https://open.spotify.com/playlist/"
    recomendaciones={
        "sad":url+"4rFp8l9vekheKOpeJLVkar",
        "disgust":url+"3cu1Oj5DY0FsJicjKh3L1A",
        "angry": url+"639kcOKOW2e8qmkRT14HqI",
        "fear":url,"4SjGQDq1wVTUqn8NtGaAzK"
        "happy":url+"37i9dQZF1DX3rxVfibe1L0",
        "neutral":url+"37i9dQZF1DX6VdMW310YC7",
        "surprise":url+"37i9dQZF1DZ06evO2vjEpW"
        }
    return webbrowser.open(recomendaciones[mood])
