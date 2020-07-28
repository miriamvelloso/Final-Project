from tkinter import *
from random import choice 

"""root = Tk()
user = StringVar()                          
bot  = StringVar()   

root.title("Chat Bot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

main_menu = Menu(root)


# Create the submenu 
file_menu = Menu(root)

# Add commands to submenu
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
#Add the rest of the menu options to the main menu
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)

messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)

Button= Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
Button.place(x=6, y=400, height=88)"""

                                                                    
root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
Label(root, text=" Python ChatBot ").pack()
Label(root, text="     ").pack()
Label(root, text="     ").pack()             
root.title(" Simple ChatBot ")                  
Label(root, text=" Say Something: ").pack()                
Entry(root, textvariable=user).pack()          
Label(root, text=" Bot : ").pack()                
Entry(root, textvariable=bot).pack() 

def main():
       question = user.get()     #assign user input to varianle "question"
       user_name = [ "Gemechis"] #you can define known person to bot :)
       known_person = ["hi, Gemechis  how are u "]   #bot reaction for define person
       user_first_input = ["hi", "hello"]   
       bot_ask_name = ["hi, what  is you name "]
       bot_greeting = ["Hello "+question, "Hi "+question, "How are you "+question]
       user_ans = ["fine", "good","am fine"]
       bot_ans = ["wow glad yo hear this :)"]
       error = ["what did you say ?"]

                             
       if question in user_first_input:                      
            bot.set(choice(bot_ask_name))
       elif question in user_name:
             bot.set(choice(known_person))
       elif question not in user_name:
       	user_name.append(question)
       	bot.set(choice(bot_greeting))
       	del user_name[1]
       	if question in user_ans:
       		bot.set(choice(bot_ans))
       else:
       	
       	bot.set(choice(error))
                           
                                
Label(root, text="     ").pack()
Button(root, text="Send", command=main).pack()


mainloop()