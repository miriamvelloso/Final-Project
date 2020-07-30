#import files
from flask import Flask, render_template, request, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os
from src.mood import getMood
from recommend.recom import getMovie, int_check, getWeb, getSong

app = Flask(__name__, template_folder='./templates/')
app.debug = True
bot = ChatBot("Candice")
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'Candice','Who are you?', 'I am a BOT'])
trainer.train(["What can you do?", "I can detect your mood if you upload an image of your face. Type in upload for this task."])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
ROUTE=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():    
    return render_template("index.html") 


@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    print(type(userText))
    if userText=="upload":
        return render_template("upload.html")

    if userText in ["1","2","3"]:
        feeling=emotion.split("...")[-1]
        print(feeling)
        option=int_check(1,3,userText)
        print(option)
        return redirect(url_for("recommendation", feeling=feeling, option=option))
    else:
        return str(bot.get_response(userText)) 


@app.route("/upload", methods=["POST"])
def upload():
    target= os.path.join(ROUTE, "image/")
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
    destination="/".join([target,filename])
    print(destination)
    upload.save(destination)
    return redirect(url_for("mood",filename=filename))

@app.route("/mood/<filename>", methods=['GET','POST'])
def mood(filename):
    global emotion
    emotion = getMood(f"image/{filename}")
    return render_template("emotion.html",emotion=emotion)

@app.route("/recommendation/<feeling>/<option>")
def recommendation(feeling,option):
    print(feeling,type(option))
    option=int(option)
    if option==1:
        print("hello")
        print(feeling)
        return getWeb(feeling)
    elif option==2:
        return getSong(feeling)
    elif option==3:
        return getMovie(feeling)
    else:
        print("Sorry there is no recommendation available to your request. Please try antoher one.")
        return render_template("recommendation.html")



if __name__ == "__main__":    
    app.run()