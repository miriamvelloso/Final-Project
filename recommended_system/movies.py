from bs4 import BeautifulSoup
import re 
import requests
import random
"""from recommended_system.getRecom import getRecommendation"""

def getMovie(emotion): 
    url='http://www.imdb.com/search/title?genres='
    end='&title_type=feature&sort=moviemeter, asc'
    recomendaciones={
        "Sad":url+'drama'+end,
        "Disgust":url+'sci-fi'+end,
        "Angry": url+'action'+end,
        "Fear":url+'horror'+end,
        "Happy":url+'comedy'+end,
        "Neutral":url+'comedy,romance'+end,
        "Surprise":url+'mystery'+end
        }
    res = requests.get(recomendaciones[emotion]) 
    soup=BeautifulSoup(res.text, "html.parser")
    results=soup.select(".lister-item.mode-advanced h3 a")
    movies=[movie.text for movie in results]
    print("How many recommendations do you want? Please type in a number.")
    number_movies=int(input("You: "))
    if len(movies)<number_movies:
        print(f"Please insert a number no greater than {len(movies)}.")
        getMovie(emotion)
    else:
        print(random.sample(movies,number_movies))

    return movies
    
"""return getRecommendation(emotion)"""
  

