#import urlextract
#extractor=.URLExtract()
from collections import Counter
#from wordcloud import  WordCloud
#from wordcloud_lite.wcl import WordCloudLite

import pandas as pd
#import emoji


def chat_stats(slected_user,df):
    if slected_user !='All User':
        df=df[df["User"]==slected_user]
    number_message=df.shape[0]
    # fetch Total word
    word=[]
    for message in df['message']:
        word.extend(message.split())
    # fetch number of video
    video=df[df['message']=='<Media omitted>\n']
    # fetch all url
    #link = []
    #for message in df['message']:
        #link.extend(urlextract.URLExtract.find_urls(message))

    return number_message,len(word),video.shape[0]
# fetch top 5 busy users in group
def busy_user(df):
    data=df['User'].value_counts().head(10)
    dataframe=round((df['User'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'User': 'User_name', 'count':'Contribution%'})
    return  data,dataframe

def word_cloud(selected_user,df):
    data_word = open(r'C:\Users\shaik\whatsapp-chat-analyzer\stop_hinglish.txt','r')
    stop_word = data_word.read()
    if selected_user !='All User':
        df = df[df["User"] == selected_user]
    # removing group notification
    temp_df = df[df['User'] != 'notification']
    #removing media file
    temp_df = temp_df[temp_df['message'] != '<Media omitted>\n']
    # Removing stopwords in chat
    words = []
    for message in temp_df['message']:
        print(message.lower().split())
        for word in message.lower().split():
            if word not in stop_word:
                words.append(word)
    top_30_word=pd.DataFrame(Counter(words).most_common(30))
    top_30_word = top_30_word.rename(columns={top_30_word.columns[0]:'Word',top_30_word.columns[1]:"Count"})

    return top_30_word
import re
#def create_wordCloud(selected_user,df):
    #if selected_user !='All User':
      #  df=df[df["User"]==selected_user]
    #wc=WordCloud()
    #df_wc=wc.generate(df['message'].str.cat(sep=" "))
    #df_wc=WordCloudLite.generate_wordcloud(df['message'].str.cat(sep=" "))
    #return df_wc

def fetch_emoji(selected_user,df):
    if selected_user !='All User':
        df = df[df["User"] == selected_user]
    #emojis=[]
    #for message in df["message"]:
        #emojis.extend([emoj for emoj in message if emoj in emoji.EMOJI_DATA])
    #df_emoji=pd.DataFrame(Counter(emojis).most_common(30))
    #return df_emoji
    import re

    # Regex pattern for emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    pic = []
    for message in df['message']:
        emojis = emoji_pattern.findall(message)
        pic.extend(emojis)
    total_emoji=pd.DataFrame(Counter(pic).most_common())
    total_emoji = total_emoji.rename(columns={total_emoji.columns[0]:'Emoji',total_emoji.columns[1]:"Count"})

    return total_emoji
#fecth most of the chat happend which month
def timeline(selected_user,df):
    if selected_user !='All User':
        df = df[df["User"] == selected_user]
    Timeline = df.groupby(['Year', 'Month']).count()['message'].reset_index()
    time = []
    for i in range(Timeline.shape[0]):
        print(Timeline['Month'])
        time.append(Timeline['Month'][i] + '-' + str(Timeline['Year'][i]))
    Timeline = Timeline.rename(columns={Timeline.columns[2]:'Total Message'})
    Timeline['Time'] =time
    return Timeline
##fecth most of the chat happend in datewise(daily basis)
def Dailytimeline(selected_user,df):
    if selected_user !='All User':
        df = df[df["User"] == selected_user]
    df['Day']=df['Date'].dt.date
    date_df = df.groupby('Day').count()['message'].reset_index()
    return date_df
# fetch most busy day in a week
def Busy_day(selected_user,df):
    if selected_user !='All User':
        df = df[df["User"] == selected_user]
    df['Day_name']=df['Date'].dt.day_name()
    day_name = df['Day_name'].value_counts()
    return day_name
# fetch most busy moth in a year
def Busy_month(selected_user,df):
    if selected_user !='All User':
        df = df[df["User"] == selected_user]
    day_name = df['Month'].value_counts()
    return day_name




