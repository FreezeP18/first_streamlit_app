import streamlit
import pandas
streamlit.title('My parents new healty diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Advocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('Fruits Smoothie 🍓🍌🍍')
streamlit.text('Green Smoothie 🥦🍏🥒')
streamlit.text('Protein Smoothie 💪🥤')
streamlit.text('Blueberry Smoothie 🫐🍇🍓')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
stramlit.dataframe(my_fruit_list)
