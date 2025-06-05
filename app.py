import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

final_df = pickle.load(open('final_df.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

client_id = "44633c40f40c49d3abc50ef0d3570d90"
client_secret = "4b9ad8b611f6418d9cf2c9e78d3fdcdb"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))


@st.cache_data
def get_track_info(track_name):
    result = sp.search(q=f"track:{track_name}", type="track", limit=1)
    try:
        track = result['tracks']['items'][0]
        album_img_url = track['album']['images'][0]['url']
        artist_name = track['artists'][0]['name']
        track_name = track['name']
        return track_name, artist_name, album_img_url
    except (IndexError, KeyError):
        return track_name, "Unknown Artist", None

def recommend_song(song_name):
    index = np.where(final_df.index == song_name)[0][0]
    distances = similarity_scores[index]
    song_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    recommended_songs = [final_df.index[i[0]] for i in song_list]
    return recommended_songs

st.markdown("""
<style>

/* Global app background */
.stApp {
    background-image: linear-gradient(to right, #1a1a2e, #16213e);
    color: #f1f1f1;
}

/* Headings */
h1, h2, h3, h4 {
    color: #f9a826;
    text-shadow: 1px 1px 2px #000;
}

/* Buttons */
div.stButton > button {
    background-color: #1db954;
    color: white;
    padding: 10px 24px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: bold;
    transition: 0.3s ease;
    border: none;
    box-shadow: 2px 2px 5px #00000040;
}

div.stButton > button:hover {
    background-color: #1ed760;
    color: black;
    transform: scale(1.05);
}

/* Select box */
.css-1wa3eu0:focus, .css-1wa3eu0:active {
    border-color: #1db954;
    box-shadow: 0 0 0 1px #1db954;
}

/* Cards for recommendations */
.song-card {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid #1db954;
    border-radius: 20px;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)



st.title('🎵 Music Recommender System')



songs_list = final_df.index.tolist()

selected_song = st.selectbox('Select a song to get recommendations:', songs_list)

if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        recommendations = recommend_song(selected_song)

        for song_name in recommendations:
            name, artist, img_url = get_track_info(song_name)

            if img_url:
                st.image(img_url, width=300)
            else:
                st.write("🎵 No album art found")
            st.markdown(f"**{name}** by *{artist}*")
            st.markdown("---")
