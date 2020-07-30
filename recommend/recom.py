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
    


def getSong(mood):
    url="https://open.spotify.com/playlist/"
    recomendaciones={
        "sad":url,
        "disgust":url,
        "angry": url,
        "fear":url,
        "happy":url+"37i9dQZF1DX3rxVfibe1L0",
        "neutral":url+"37i9dQZF1DX6VdMW310YC7",
        "surprise":url+"37i9dQZF1DXcZK031Zeh47?si=WlZ6V-bNQOWGS5T7uD53WQ"
        }
    return webbrowser.open(recomendaciones[mood])
    

  

