import streamlit 
streamlit.title('My Mom New Healthy Diner')
streamlit.header('Breakfast favourites')
streamlit.text('🥣 omega 3 and blueberry oatemal')
streamlit.text('🥗 kale,spinach and roacket smothiee')
streamlit.text('🐔 Hard-boiled free-range egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
