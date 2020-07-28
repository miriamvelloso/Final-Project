#import files
from flask import Flask, render_template, request, redirect
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

app = Flask(__name__, template_folder='.')
app.debug = True
bot = ChatBot("Candice")
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'Candice'])
trainer.train(['who are you?', 'I am a BOT'])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

APPROUT=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():    
    return render_template("upload.html") 

"""@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')   
    return str(bot.get_response(userText)) 
"""

@app.route("/upload", methods=["POST"])
def upload():
    target= os.path.join(APPROUT, "image/")
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


    return render_template("index.html")

    """if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            return redirect(request.url)


    return render_template("upload.html")"""

if __name__ == "__main__":    
    app.run()