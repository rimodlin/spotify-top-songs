import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from itertools import chain

# Load the dataset
file_path = "C:/Users/rimod/OneDrive/Desktop/spotify-top-songs-data-analysis/playlist_2010to2023.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Convert all text to lowercase and remove leading/trailing spaces
df["artist_genres"] = df["artist_genres"].str.lower().str.strip()

# Split multiple genres in one cell (e.g., "Pop, Dance" → ["pop", "dance"])
all_genres = list(chain.from_iterable(df["artist_genres"].str.split(',')))

# Combine all genres into a single string
all_genres = " ".join(df["artist_genres"].astype(str))


# Clean the genre strings by removing extra characters
all_genres = all_genres.replace("[", "").replace("]", "").replace("'", "").replace(",", "")

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(all_genres)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Music Genres", fontsize=14)
plt.show()

