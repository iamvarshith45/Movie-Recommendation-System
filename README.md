# Movie-Recommendation-System

This project is a Content-Based Movie Recommendation System using the TMDB 5000 Movie Dataset. The system analyzes metadata such as movie overviews, genres, cast, crew, and keywords to recommend movies similar to a user's selected movie.

-> Data Collection and Preprocessing
Loads movie metadata and credits from the TMDB dataset, and merged both datasets on the title field, later extracted meaningful features:
genres, keywords, cast (top 3 actors), and crew (only director) and performed Tokenization and cleans the overview text.
and also removed spaces and converted all tokens to lowercase for consistency and to avoid ambiguity in identifying entities(tags) <br>

-> Feature Engineering Combines all textual features (overview, genres, keywords, cast, crew) into a single unified feature called tags.
and applied stemming to reduce words to their root forms and avoid duplication later used CountVectorizer to convert the tags text into a matrix of token counts (bag-of-words model) and 
Computed cosine similarity between all movie vectors to create a similarity matrix. <br>

-> Recommendation Function takes one argument: a movie title (movie) that the user wants recommendations for and final_df is a DataFrame that contains movie titles and preprocessed text features (tags) and Filters the DataFrame to find the row where the title matches the input movie and Gets the index (row number) of that movie.
{cosine similarity matrix is indexed by row numbers, so we need to know which row corresponds to the selected movie} <br>

enumerate(distance): Creates (index, score) pairs for each movie in the dataset and Converts the enumerated object into a list of tuples.
sorted(reverse=True, key=lambda x: x[1]): Sorts the list by similarity score in descending order and finally [1:6]: Skips the first result and keeps the next 5 most similar movies. <br>

-> The app.py script creates a simple, user-friendly interface using Streamlit to interact with the recommendation engine.
Loads Pickled Data movies_dict.pkl: Contains movie titles and tags and similarity.pkl: Contains precomputed similarity scores.
Recommendation Logic defines a recommend() function that replicates the logic from the notebook using loaded data and Returns the top 5 movie recommendations for a selected movie.
and for Interactive UI Uses st.selectbox() to let the user choose a movie, On clicking the "Recommend Movie" button, it displays similar movie titles using st.write().


-> Tech Stack --
Python (Pandas, NumPy, scikit-learn, NLTK) <br>
Natural Language Processing (NLP): Tokenization, stemming, vectorization <br>
Machine Learning: Cosine similarity for content-based filtering <br>
Streamlit: Rapid UI development for deploying the recommendation engine <br>
 
