from PIL import Image
from cv2 import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
import numpy as np
import os

def get_label(argument):
    labels = {0:'Angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Sad' , 5:'Surprise', 6:'Neutral'}
    return(labels.get(argument, "Invalid emotion"))

model_p = os.path.join(os.getcwd(),"input","model.h5")

def getMood(path):
    model2=load_model(model_p)
    img = Image.open(path)
    face_cascade = cv2.CascadeClassifier('src/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(np.asarray(img), 1.1, 4)
    for (x, y, w, h) in faces:
        cropped_img = img.crop((x,y,x+w,y+h))
    plt.imshow(cropped_img)
    test_image = cropped_img.resize((48,48),Image.ANTIALIAS)
    test_image = np.array(test_image)
    gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    gray = gray/255
    gray = gray.reshape(-1, 48, 48, 1)
    res = model2.predict(gray)
    result_num = np.argmax(res)
    emotion=get_label(result_num)
    print("Bot: With a probability of " + str(np.max(res[0]))+" you are feeling...")
    
    return emotion
