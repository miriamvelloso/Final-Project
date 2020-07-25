from bs4 import BeautifulSoup as SOUP 
import re 
import requests

def main(emotion): 
    if(emotion == "Sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
        
    elif(emotion == "Angry"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "Disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "Happy"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "Neutral"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    response = requests.get(urlhere) 
    data = response.text 
    soup = SOUP(data, "lxml") 
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    return title 
  

