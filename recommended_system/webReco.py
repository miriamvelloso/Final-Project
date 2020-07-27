import webbrowser

def int_check(l,h,message): #for inputting integers
    while True:
        s = input(message)
        if s.isdigit():
            s=int(s)
            if l<=s<=h:
                return s
            else:
                print("\nError in input, please try again.")
        else:
            print("\nError in input, please try again.")

media_input = int_check(1,3,"\nWhat is it that you'd like to be recommended based on your mood?\n\n1. Images\n2. Songs\n3. Movies\n\nPlease enter the corresponding digit: ")
mood = "Surprise"
if media_input==1: 
    if mood=='Happy':
        webbrowser.open("https://www.happify.com")
    elif mood=='Sad': 
        a = int_check(1,2,"\n\nWhat link would you like to view?\n1. 39 Pictures For Anyone Who Is Just Sad\n2. 42 Pictures That Will Make You Almost Too Happy\n\nPlease select a corresponding integer: ")
        if a==1:
            webbrowser.open("https://www.buzzfeed.com/jasminnina/25-images-that-will-make-you-realize-it-could-be-worse")
        elif a==2:
            webbrowser.open("https://www.buzzfeed.com/jimwaterson/pictures-of-happy-men-with-giant-vegetables")
    elif mood=='Angry': 
        a = int_check(1,2,"\n\nWhat link would you like to view?\n1. 21 Pictures That Will Definitely Make You Feel Better\n2. 28 Pictures That Will Help You Calm The Hell Down Today\n\nPlease select a corresponding integer: ")
        if a==1:
            webbrowser.open("https://www.buzzfeed.com/pampers/ways-to-smile-like-a-happy-happy-baby")
        elif a==2:
            webbrowser.open("https://www.buzzfeed.com/alexnaidus/pictures-of-food-that-will-soothe-you-and-make-you-hungry")
    elif mood=='Neutral': 
        a = int_check(1,2,"\n\nWhat link would you like to view?\n1. Give Yourself A Relaxing Day Off With These 24 Products\n2. 12 Perfect GIFs To Keep You Relaxed & Soothe Your Spirit \n\nPlease select a corresponding integer: ")
        if a==1:
            webbrowser.open("https://www.buzzfeed.com/mugdhakusray/give-yourself-a-day-off-with-these-products-52982rd8tw")
        elif a==2:
            webbrowser.open("https://www.buzzfeed.com/adamjkurtz/handwriting-plus-sunsets-equals-art")
    elif mood=='Surprise':
        webbrowser.open("https://www.buzzfeed.com/pepsimaxuk/photos-with-unbelievable-hidden-surprises")


elif media_input==2: 
    if mood=='Happy':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0')
    elif mood=='Sad':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0')
    elif mood=='Angry':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0')
    elif mood=='Neutral':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7')
    elif mood=='Surprise':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open('https://open.spotify.com/playlist/37i9dQZF1DXcZK031Zeh47?si=WlZ6V-bNQOWGS5T7uD53WQ')
