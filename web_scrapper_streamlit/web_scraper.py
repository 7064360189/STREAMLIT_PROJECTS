import streamlit as st 
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
st.set_page_config(page_title="Web scraper",page_icon="🌐", layout="wide")
st.markdown("<h1 style='text-align: center;'>WEB SCRAPER</h1>",unsafe_allow_html=True)
with st.form("search"):
    keyword = st.text_input("enter keyword")
    search = st.form_submit_button("search")
placeholder = st.empty()    
if keyword:
    
    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content,'lxml')
    rows = soup.find_all("div",class_="d95fI")
    col1,col2 = placeholder.columns(2)
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img=figures[i].find("img",class_="ApbSI z1piP vkrMA")
            list=(img["srcset"].split("?"))
            anchor=figures[i].find("a",class_="Prxeh")
            print(anchor["href"])
            if i == 0:
                col1.image(list[0])
                btn = col1.button("download",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            else:
                col2.image(list[0])    
                btn = col2.button("download",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
