import streamlit as st
import requests

FASTAPI_URL = "http://backend:4000"  

st.title("SQL Query Executor with FastAPI & Streamlit")

st.sidebar.header("Database Connection")
db_name = st.sidebar.text_input("Database Name")
db_user = st.sidebar.text_input("User")
db_password = st.sidebar.text_input("Password", type="password")
db_host = st.sidebar.text_input("Host", value="localhost")
db_port = st.sidebar.text_input("Port", value="5432")
api_key = st.sidebar.text_input("Groq API Key", type="password")

if st.sidebar.button("Connect"):
    payload = {
        "db_name": db_name,
        "db_user": db_user,
        "db_password": db_password,
        "db_host": db_host,
        "db_port": db_port,
        "api_key": api_key
    }
    response = requests.post(f"{FASTAPI_URL}/connect", json=payload)
    if response.status_code == 200:
        st.sidebar.success("Connected to the database successfully!")
    else:
        st.sidebar.error(f"Error: {response.json().get('detail')}")

st.header("Execute SQL Query")
query = st.text_area("Enter your SQL query:")

if st.button("Run Query"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        query_payload = {"query": query}
        response = requests.post(f"{FASTAPI_URL}/query", json=query_payload)
        
        if response.status_code == 200:
            result = response.json().get("result", "No result returned.")
            st.success("Query executed successfully!")
            st.write(result)
        else:
            st.error(f"Error: {response.json().get('detail')}")