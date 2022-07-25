import streamlit as st
import requests
from math import *

st.set_page_config(
         page_title="Qurany",
     page_icon="📖",
     initial_sidebar_state="expanded"
     
 )
title =st.title("Qurany")
remove_menu_footer = """
<style>
#MainMenu {visibility: hidden;}
footer { visibility:hidden; }
</style>
"""
input = st.sidebar.text_input("رقم الصفحة", "1")
inputstartingout=print(input)
#inputpage = st.sidebar.text_input("الصفحة")
st.markdown(remove_menu_footer, unsafe_allow_html=True)

if "load_state" not in st.session_state:
     st.session_state.load_state = False
if 'count' not in st.session_state:
    st.session_state.count =0
#st.session_state.count += 1
if st.session_state.count == 0:
    st.session_state.count = 1
    print (st.session_state.count)

def decrement_button():
    decrement_value = 1
    st.session_state.count -= decrement_value
    print ("def"+str(st.session_state.count)) 

def increment_button():
    increment_value = 1
    st.session_state.count += increment_value
    print ("def"+str(st.session_state.count))

input =int(input)

if st.session_state.count<10:
    pagenum = "00"+str(st.session_state.count)
elif st.session_state.count<100:
    pagenum = "0"+str(st.session_state.count)
else:
    pagenum = st.session_state.count     
print(st.session_state.count)
    
if input=="1":
    
    image = f"https://www.searchtruth.org/quran/images1/001.jpg"
    st.image(image, use_column_width=True)
    st.markdown(f"<h6>الصفحة {pagenum}</h6>", unsafe_allow_html=True)
    
elif input<10:
    pagenum = "00"+str(st.session_state.count)
    image = f"https://www.searchtruth.org/quran/images1/{pagenum}.jpg"
    st.image(image, use_column_width=True)
    st.markdown(f"<h6>الصفحة {pagenum}</h6>", unsafe_allow_html=True)
    print(45+input)
elif input<100:
    pagenum = "0"+str(st.session_state.count)
    image = f"https://www.searchtruth.org/quran/images1/{pagenum}.jpg"
    st.image(image, use_column_width=True)
    st.markdown(f"<h6>الصفحة {pagenum}</h6>", unsafe_allow_html=True)
    print(45+input)
else:
    image = f"https://www.searchtruth.org/quran/images1/{pagenum}.jpg"
    st.image(image, use_column_width=True)
    st.markdown(f"<h6>الصفحة {pagenum}</h6>", unsafe_allow_html=True)        



    

#pagenum = st.session_state.count
#print(pagenum)
#req = requests.get(f"https://dorar-hadith-api.herokuapp.com/api/search?value={input}&page=pagenum")
#data = req.json()
#data_len=len(data)
#for i in range(data_len):
#    number = i
#    hadith_uncleaned = data[number]["hadith"]
#    hadith = hadith_uncleaned.replace(".", "")
#    source = data[number]["source"]
#    rawi = data[number]["el_rawi"]
#    mohdith = data[number]["el_mohdith"]
#    numpage = data[number]["number_or_page"]
#    grade = data[number]["grade"]
#    align_right_i = f"<p style='text-align:right;'>{i+1}</p>"
#    st.markdown(align_right_i, unsafe_allow_html=True)
#    st.markdown(f"<p style='text-align:right;'>الحديث: {hadith}</p>", unsafe_allow_html=True)
#    align_right = f"<p style='text-align:right;'>الراوي: {rawi}  |المحدث: {mohdith}  |المصدر: {source}</p>"
#    st.markdown(align_right,unsafe_allow_html=True)
#    st.markdown(f"<p style='text-align:right;'>خلاصة حكم الحديث: {grade}  | الصفحة أو الرقم: {numpage}  </p>",unsafe_allow_html=True)
#    st.markdown("<br>",unsafe_allow_html=True)

increment_button = st.button("next", on_click=increment_button)
decrement_button = st.button("previous", on_click=decrement_button)


#st.button("next",on_click=button_hadith(),kwargs=dict(increment_value=1))   
#st.markdown(f"<p style='text-align:right;'>< button  onclick = ""  > Search  </ button ></p>",unsafe_allow_html=True)

