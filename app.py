import streamlit as st
import requests
import time

API_URL = "http://backend:4000"

st.set_page_config(page_title="📊 AI Business Insights", layout="wide")

st.sidebar.header("📂 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

st.title("📊 AI-Powered Business Insights")
st.write("Leverage AI to analyze your data and extract meaningful insights.")

if uploaded_file is not None:
    if "dataset_uploaded" not in st.session_state:
        st.session_state["dataset_uploaded"] = False

    if not st.session_state["dataset_uploaded"]:
        with st.sidebar:
            with st.spinner("Uploading file..."):
                files = {"file": uploaded_file.getvalue()}
                response = requests.post(f"{API_URL}/upload/", files=files)
                time.sleep(1)  
                if response.status_code == 200:
                    st.success("✅ File uploaded successfully!")
                    columns = response.json().get("columns", [])
                    st.session_state["dataset_uploaded"] = True
                    st.session_state["columns"] = columns
                else:
                    st.error("❌ Error uploading file. Please try again.")

if "dataset_uploaded" in st.session_state and st.session_state["dataset_uploaded"]:
    st.sidebar.subheader("📌 Dataset Columns")
    st.sidebar.write(", ".join(st.session_state["columns"]))

st.subheader("💡 Ask a Question About Your Data")
question = st.text_input("Enter your question", placeholder="E.g., What are the key trends in the data?")

if st.button("🔍 Get Insights"):
    if "dataset_uploaded" not in st.session_state or not st.session_state["dataset_uploaded"]:
        st.error("❌ Please upload a dataset first.")
    elif not question:
        st.error("❌ Please enter a question.")
    else:
        with st.spinner("Generating insights..."):
            params = {"question": question}
            response = requests.get(f"{API_URL}/analyze/", params=params)
            time.sleep(1)  

            if response.status_code == 200:
                insights = response.json().get("insights", "No insights found.")
                st.subheader("📢 AI-Generated Insights")
                st.write(insights)
            else:
                st.error("❌ Error retrieving insights. Please try again.")

with st.expander("📌 About This App"):
    st.write("""
    - **Upload any dataset** and analyze it with AI.
    - **Ask business-related questions** to get insights.
    - **Powered by LLMs** for advanced analytics.
    - **Future enhancements:** Data visualization, trend predictions, and more!
    """)

st.sidebar.markdown("---")
st.sidebar.info("Developed by AI-Powered Data Team 🚀")
