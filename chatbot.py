#import files
from flask import Flask, render_template, request, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os
from src.mood import getMood


app = Flask(__name__, template_folder='.')
app.debug = True
bot = ChatBot("Candice")
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'Candice'])
trainer.train(['who are you?', 'I am a BOT'])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

ROUTE=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():    
    return render_template("index.html") 


@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    if userText=="emotion":
        return render_template("upload.html")
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

@app.route("/mood/<filename>")
def mood(filename):
    emotion=getMood(f"image/{filename}")

    return render_template("emotion.html",emotion=emotion)



if __name__ == "__main__":    
    app.run()