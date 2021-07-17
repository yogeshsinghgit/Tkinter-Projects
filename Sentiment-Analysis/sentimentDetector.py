# Instagram @dynamic.coding
# >> Follow us on Github <<
import tkinter as tk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# pip install vadersentiment

def detectSentiment():
    # get a whole input content from text box
    sentence = entry.get()
    text.delete(0.0,tk.END)
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    negative_string= str(sentiment_dict['neg']*100) + "% Negative"
    text.insert(tk.END,negative_string+'\n')

    neutral_string = str(sentiment_dict['neu']*100) + "% Neutral"
    text.insert(tk.END,neutral_string+'\n')

    positive_string = str(sentiment_dict['pos']*100) +"% Positive"
    text.insert(tk.END,positive_string+'\n')
     
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        string = "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        string = "Negative"
      
    else :
        string = "Neutral"

    text.insert(tk.END,f"Overall Result : {string}")

from tkinter import ttk
root = tk.Tk()
root.title("Sentiment Detector")
root.resizable(0,0)
root.configure(bg='#00003c')
root.geometry("300x300")


entry = tk.Entry(root,width=20,font=('arial',14))
entry.place(x=5,y=20)

btn = tk.Button(root,text='Analyze',bg='#201d2e', width=6,fg='white',
font=('Arial', 10 ),command=detectSentiment)
btn.place(x=232,y=20)

frame = tk.Frame(root,bd=2, relief=tk.RIDGE,bg='#201d2e')
frame.place(x=10,y=70,height=220,width=280)

label = tk.Label(frame,text='Result',bg='#201d2e',fg='white',font=('arial',12,'bold'))
label.place(x=10,y=5)

text = tk.Text(frame,bd=2,relief=tk.SUNKEN,font=('Calibri',12,'bold'))
text.place(x=10,y=30,width=255,height=150)

title_label = tk.Label(frame,text='@dynamic.coding',font=('arial',12,'bold'),fg='#ffffff',bg='#201d2e')
title_label.place(x=65,y=185)

root.mainloop()
