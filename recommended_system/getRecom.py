from recommended_system.webscrapping import getMovie


def getRecommendation(mood):
    print("What would you like me to recommend?")
    recommendation=input("You: ")
    if recommendation=="Song":
        #llamar función que entra en el dataset y te devuelva una random de la emoción
        print("song")

    elif recommendation=="Movie":
        return getMovie(mood)
                
    else:
        print("Sorry there is no recommendation available to your request. Please try antoher one.")
        return getRecommendation(mood)