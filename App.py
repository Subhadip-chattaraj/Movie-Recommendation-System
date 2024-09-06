import streamlit as st
import pickle

movie_list=pickle.load(open('movies.pkl','rb'))
movie_names=movie_list['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))

def recommender(movie):
    movie_index = movie_list[movie_list['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_names=sorted(list(enumerate(distances)),reverse=True,key=lambda x :x[1])[1:6]
    recommended_movies=[]
    for i in movie_names:
        recommended_movies.append(movie_list.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommender System')

selected_movieName=st.selectbox('Enter the movie Name?',movie_names)
if st.button("Recommend"):
    movies=recommender(selected_movieName)
    for i in movies:
        st.write(i)
