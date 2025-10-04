# Spotify Top Songs Popularity Prediction

## Introduction

Music streaming platforms such as Spotify and Apple Music have revolutionized the way we listen to music and made song popularity more important than ever for discoverability and success in the music industry. Understanding what contributes to a song’s success can help artists, producers, and record labels make data-driven decisions about promotion, production, and playlist curation.

In this study, I analyzed a dataset containing song characteristics from tracks in Spotify’s Top Hit Playlist from the years 2010-2023, to determine what characteristics are most important in predicting track popularity. Some characteristics include danceability, energy, valence and duration. Multiple regression techniques were used, including linear regression, LASSO regression, and random forest models to evaluate which features have the most impact on track popularity, and model performance was assessed using RMSE.

Features such as danceability, energy, valence, and duration can influence how engaging and emotionally appealing a song is to listeners. For example, high danceability may make a song more suitable for clubs and parties, increasing its chances of viral success. Energy levels can determine whether a song feels upbeat or mellow, affecting its placement in playlists. Similarly, valence, which measures musical positivity, may impact how frequently a song is streamed based on listener mood preferences. I also believe that duration could be important for how streamable songs are, given the fast pace of modern society and the increase in popularity of short-form content on platforms such as Tik Tok, Instagram, and YouTube. By analyzing these characteristics, I am to uncover trends and insights into what makes a song popular.

## Data

The dataset used is publicly available on Kaggle and was extracted from Spotify API directly. The dataset contains songs from Spotify’s Top Hit Playlist for each year from 2010-2023. Each playlist contains 100 songs, with the whole dataset consisting of 2400 tracks.

Here is a glimpse of the first 5 rows of data.

