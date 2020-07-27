from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
import random
from src.mood import getMood
from recommend.getRecom import getRecommendation


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
            print(f"You are feeling {mood}.")
            print("Do you want a recommendation?")
            request=input("You: ")
            if request.lower()=="yes":
                getRecommendation(mood)
                print("Do you wish to request another recommendation?")
                answer=input("You: ")
                if answer.lower()=="yes":
                    getRecommendation(mood)
            
        elif request == 'goodbye':
            break
        
        else:
            response=bot.get_response(request)
            print("Bot :", response)
            
    except(KeyboardInterrupt,EOFError,SystemExit):
        break

