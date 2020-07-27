print("1")
from chatterbot import ChatBot 
print("2")
from chatterbot.trainers import ListTrainer
print("3")
from recommended_system.getRecom import getRecommendation
print("4")
from recommended_system.movies import getMovie
print("5")
import random
print("6")
from src.mood import getMood


bot = ChatBot(
    'Terminal',
     storage_adapter='chatterbot.storage.SQLStorageAdapter',
     database_uri='sqlite:///database.db'
) 
# create the chatbot

conv=open("greet_data.txt", "r").readlines()

trainer=ListTrainer(bot) # set the trainer

trainer.train(conv)
print("Hello, my name is Candice and I'm here to help you.")



while True:
    
    try:
        request=input("You: ")

        if request.startswith("http") or request.endswith(".jpg"):
            mood=getMood(request)
            print("output emocion: ")
            print("Do you want a recommendation?")
            request=input("You: ")
            if request=="Yes":
                getRecommendation(mood)
                
        elif request == 'goodbye':
            break
        
        else:
            response=bot.get_response(request)
            print("Bot :", response)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break

