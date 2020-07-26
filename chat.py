
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
from recommended_system.getRecom import getRecommendation
from recommended_system.webscrapping import getMovie
import random


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
            mood="Sad"
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

