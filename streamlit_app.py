import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Mom New Healthy Diner')
streamlit.header('Breakfast favourites')
streamlit.text('🥣 omega 3 and blueberry oatemal')
streamlit.text('🥗 kale,spinach and roacket smothiee')
streamlit.text('🐔 Hard-boiled free-range egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])

# Display the table on the page.
fruits_selected=streamlit.multiselect('pick some fruitss:',list(my_fruit_list.index),['Avocado','strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


# import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

streamlit.write('Thanks for adding',add_my_fruit)
my_cur.exe("insert into fruit_load_list values('from streamlit')");

streamlit.header('fruityvice fruit advice!')
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
   else:
     fryityvise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      fruityvice_normalized=pandas.json_normalize(fruityvice_responxe.json())
      streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
      



