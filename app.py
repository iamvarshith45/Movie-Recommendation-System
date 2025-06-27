import streamlit as st
import pandas as pd
import pickle


def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distance = similarity_score[movie_index]
  movies_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x: x[1])[1:6]
  recommended_movies  = []
  recommended_movies_img = []
  for i in movies_list:
      #movie_id = movies.iloc[i[0]].movie_id
      recommended_movies.append(movies.iloc[i[0]].title)
      #recommended_movies_img.append(fetch_poster(movie_id))
  return recommended_movies #, recommended_movies_img



# PICKLE FILES
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity_score = pickle.load(open('similarity.pkl', 'rb'))



## STREAMLIT DASHBOARD --
st.title('Movie Recommendation System')

selected_movie = st.selectbox('Please Enter Movie Name', movies['title'].values)

if st.button('Recommend Movie'):
    output = recommend(selected_movie)
    for r in output:
        st.write(r)



