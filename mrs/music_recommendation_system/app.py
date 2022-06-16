import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image

img = Image.open("download.png")


def recommend(song):
    song_index = songsdf[songsdf['title'] == song].index[0]
    distances = similar[song_index]
    songs_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    rec_songs = []
    for i in songs_list:
        song_id = i[0]
        rec_songs.append(songsdf.iloc[i[0]].title)
    return rec_songs


song_dict = pickle.load(open('songs_dict.pkl', 'rb'))
songsdf = pd.DataFrame(song_dict)
similar = pickle.load(open('similar.pkl', 'rb'))

st.set_page_config(page_title="Music Recommendation System", page_icon=img)
st.title('Music Recommendation System')

selected = st.selectbox(
    'Please select the song of your choice',
    songsdf['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected)
    for i in recommendations:
        st.write(i)
