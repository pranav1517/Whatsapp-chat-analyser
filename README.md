
# WhatsApp-Chat-Analysis


## Content

1. [Description](#description)
1. [Screenshots](#screenshots)
1. [Project structure](#project-structure)
1. [Walkthrough](#walkthrough)
1. [Application](#application)




## Description

WhatsApp-Chat-Analyzer web app allows user to get analysis of their whatsapp chat data. User can see analysis of overall group (including all users) as well as of individual users.
User can get analysis of messages, timeline of usage, activity map, wordcloud, most active users, etc. All of these analysis can be shown for both overall group and individual
user.

## Screenshots

<a href="https://drive.google.com/uc?export=view&id=1T1HXj-ItZBiTwarR0jxypQvmmtcAO51S"><img src="https://drive.google.com/uc?export=view&id=1T1HXj-ItZBiTwarR0jxypQvmmtcAO51S" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />
<a href="https://drive.google.com/uc?export=view&id=1hytvT5S7B0-IRuGysfvsjYbS45C0ey1q"><img src="https://drive.google.com/uc?export=view&id=1hytvT5S7B0-IRuGysfvsjYbS45C0ey1q" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />
<a href="https://drive.google.com/uc?export=view&id=1B3YMOKFJgOsl94Nu-U51ldnNmguAQbum"><img src="https://drive.google.com/uc?export=view&id=1B3YMOKFJgOsl94Nu-U51ldnNmguAQbum" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />
<a href="https://drive.google.com/uc?export=view&id=1oTiIqrzTbw1Q-2-b1n0OikKa0XDjG6e2"><img src="https://drive.google.com/uc?export=view&id=1oTiIqrzTbw1Q-2-b1n0OikKa0XDjG6e2" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

## Project structure

```   
  ├── app.py                      Streamlit python application file 
  ├── helpers.py                  python file that contains helper functions for chat analysis 
  ├── datapreprocessing.py        python file for preprocessing raw text data from chat to dataframe
  ├── requirements.txt            list of all required libraries used in app
  ├── stop_hinglish.txt           contains all stop words 
  
```
## Walkthrough
- to get chat data follow: whatsapp -> chat -> options -> More -> Export chat -> Without media
- access [App](https://pranav1517-whatsapp-chat-analyser-app-l9ujp2.streamlit.app/) and select chat file
- in show analysis wrt select the user, for overall group select overall 


## Application

[WhatsApp-Chat-Analysis](https://pranav1517-whatsapp-chat-analyser-app-l9ujp2.streamlit.app/)

