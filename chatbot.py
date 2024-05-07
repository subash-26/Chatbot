import streamlit
import streamlit_option_menu
import os
from embedchain import App

os.environ["OPENAI_API_KEY"] = "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"

bot = App()


#Online website restricition
bot.add("https://www.w3schools.com/sql/")
bot.add("https://www.tutorialspoint.com/sql/index.htm")
bot.add("https://www.tutorialspoint.com/sql/sql-syntax.htm")
bot.add("https://www.tutorialspoint.com/sql/")

response = bot.query("Database Normalization")

print(response)
