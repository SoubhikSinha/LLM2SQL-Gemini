# Creating the application
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load "Gemini" model and generate SQL queries (as reespone)
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content([prompt, question]) # This will generate a response based on the prompt and question
    return response.text

# Function to retrieve data from the SQLite database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db) # This will connect to the SQLite database
    cursor = conn.cursor() # This is for executing SQL commands
    cursor.execute(sql) # This will execute the SQL query
    data = cursor.fetchall() # This will fetch all the records from the executed query
    # conn.commit() # This will commit the changes to the database
    conn.close() # This will close the connection to the database

    # Printing the data in a readable format
    for row in data:
        print(row)
    
    # Returning the data
    return data


# Defining the Prompt
prompt ="""
You are an expert in converting natural language questions into database queries.

The database is named 'student.db' and it has only one table named 'students and has the following columns: NAME, CLASS, SECTION and MARKS.

Below is the schema of the table:
CREATE TABLE IF NOT EXISTS students (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT);

For example:
Input: “How many students are studying in 10th Grade?”

Output:
SELECT * FROM students WHERE CLASS = "10";

Your task is to convert each English question into its correct query form using the above schema. Do not add any explanations or extra words—just return the query.
"""

# Streamlit application
st.set_page_config(page_title="LLM2SQL-Gemini", page_icon=":guardsman:")
st.header("LLM2SQL-Gemini")

question = st.text_input("Enter your question here:")

submit_button = st.button("Ask a Question")

# If the submit button is clicked, process the question
if submit_button and question:
    response= get_gemini_response(question, prompt)
    print("Response from Gemini:", response)
    data = read_sql_query(response, "student.db")  # This will read the SQL query from the response and execute it on the student.db database
    st.subheader("Query Result:")
    for row in data:
        print(row)
        st.write(row)  # Displaying the result in the Streamlit app