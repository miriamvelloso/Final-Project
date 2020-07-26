from recommended_system.webscrapping import main

if __name__ == '__main__': 
  
    emotion = input("Enter the emotion: ") 
    a = main(emotion) 
    count = 0
  
    if(emotion == "Disgust" or emotion == "Anger"
                           or emotion=="Surprise"): 
  
        for i in a: 
  
            # Splitting each line of the IMDb data to scrape movies 
            tmp = str(i).split('>;') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 13): 
                break
            count += 1
    else: 
        for i in a: 
            tmp = str(i).split('>') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 11): 
                break
            count+=1