import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urlextract import URLExtract
from IPython.display import HTML
from wordcloud import WordCloud
import emoji
from collections import Counter



extract = URLExtract()

def all_stats(df,selected_user):
    
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    num_messages = total_messages(df)
    num_words = total_words(df)
    num_media = total_media(df)
    num_links,links = total_links(df)
    links_df = links_dataframe(links)

    
    return num_messages, num_words,num_media, num_links, links_df
    
def total_messages(df):
    
    return df.shape[0]

def total_words(df):
    
    words = []
    df_word = df.drop(df[df['message']=='<Media omitted>\n'].index,axis=0)
    for message in df_word['message']:
        words.extend(message.split())
    return len(words)

def total_media(df):
    
    df = df[df['message'] == '<Media omitted>\n']
    return df.shape[0]

def total_links(df):
    
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return len(links),links 

def links_dataframe(links):

    ldf = pd.DataFrame(links,columns=['shared_links'])
    ldf = HTML(ldf.to_html(render_links=True,escape=False))

    return ldf


def top_users(df):
    n = df.shape[0]
    x = df['user'].value_counts().head()
    maxdf = df['user'].value_counts().reset_index()
    maxdf.columns = ['user','message_count']
    maxdf['percentage'] = round(100 * (maxdf['message_count']/n),2)
    
    return x,maxdf

def monthly_timeline(df):
    monthlydf = df.groupby(['year','month_num','month']).count()['message'].reset_index()
    monthlst = []
    for i in range(monthlydf.shape[0]):
        monthlst.append(monthlydf['month'][i]+"-"+str(monthlydf['year'][i]))
    monthlydf['time'] = monthlst

    return monthlydf

def daily_timeline(df):

    dailydf = df.groupby('date').count()['message'].reset_index()

    return dailydf

def week_activity_map(df):

    return df['day'].value_counts()

def month_activity_map(df):

    return df['month'].value_counts()

def activity_heatmap(df):

    user_heatmap = df.pivot_table(index='day', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap

def create_wordcloud(df):

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    temp = df[df['user'] != 'group-notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc

def emoji_helper(df):

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

def convert_df(df):
    return df.to_csv().encode('utf-8')


