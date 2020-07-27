from recommend.recom import getMovie, int_check, getWeb, getSong

def getRecommendation(mood):
    print("What would you like me to recommend?")
    recommendation = int_check(1,3,"\nWhat is it that you'd like to be recommended based on your mood?\n\n1. Images\n2. Songs\n3. Movies\n\nPlease enter the corresponding digit: ")
    if recommendation==1:
        return getWeb(mood)
    elif recommendation==2:
        return getSong(mood)
    elif recommendation==3:
        return getMovie(mood)
                
    else:
        print("Sorry there is no recommendation available to your request. Please try antoher one.")
        return getRecommendation(mood)