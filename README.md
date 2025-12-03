# 🎵 Music Recommendation System

A **Content-Based Filtering** recommendation system that suggests songs based on audio features such as tempo, energy, and danceability. This project utilizes a Spotify dataset to mathematically calculate the similarity between songs using Cosine Similarity.

## 📌 Project Overview

Unlike collaborative filtering which relies on user history, this system analyzes the intrinsic properties of the audio itself. If a user likes a specific track, the system identifies other tracks with a similar audio profile.



* **Type:** Content-Based Filtering
* **Algorithm:** Cosine Similarity
* **Dataset:** Spotify Songs Dataset (Audio features + Genres)

## 📂 Dataset Features

The system analyzes the following audio features to generate recommendations:
* **Numerical Features:** `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `duration_ms`.
* **Categorical Features:** `playlist_genre` (Processed via One-Hot Encoding).

## 🛠️ Tech Stack

* **Python**
* **Pandas** (Data manipulation and cleaning)
* **NumPy** (Numerical operations)
* **Scikit-Learn**:
    * `StandardScaler` (Feature scaling)
    * `OneHotEncoder` (Categorical encoding)
    * `cosine_similarity` (Distance metric)
* **Pickle** (Model serialization)

## ⚙️ Methodology

1.  **Data Preprocessing**:
    * Loaded the dataset and sampled 1,800 songs for efficient processing.
    * Removed non-essential identifiers (e.g., `track_id`, `track_artist`, `track_album_release_date`).
    * Handled duplicate records to ensure data quality.

2.  **Feature Engineering**:
    * **Scaling**: Applied `StandardScaler` to numerical columns (like `loudness` and `tempo`) to normalize the data range.
    * **Encoding**: Applied `OneHotEncoder` to the `genre` column to convert categorical data into a machine-readable format.
    * **Concatenation**: Combined scaled numerical features and encoded genre features into a single dataframe.

3.  **Model Building**:
    * Calculated a **Cosine Similarity Matrix** ($N \times N$) representing the similarity score (angle) between every pair of songs vectors.

    

4.  **Recommendation Engine**:
    * The `recommend_song(song_name)` function looks up the vector index of the input song.
    * It sorts the similarity scores in descending order and returns the top 5 most similar tracks.

