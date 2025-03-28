import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import io
import uvicorn

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = FastAPI(title="AI-Powered Data Analysis API")

chat = ChatGroq(api_key=GROQ_API_KEY, model='llama-3.3-70b-versatile')

df = None


@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    global df

    try:
        df = pd.read_csv(io.StringIO(file.file.read().decode("utf-8")))
        return {"message": "File uploaded successfully", "columns": df.columns.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV file: {str(e)}")


@app.get("/analyze/")
async def analyze_data(question: str = Query(..., description="Ask a question about the dataset")):
    global df

    if df is None:
        raise HTTPException(status_code=400, detail="No dataset uploaded. Please upload a CSV file first.")

    summary = df.describe(include="all").to_string()

    template = PromptTemplate(
        input_variables=["data_summary", "question"],
        template="""
        You are a data analyst and business strategist. Your goal is to analyze datasets and extract key insights.
        
        **Dataset Summary:**  
        {data_summary}  

        **Business Intelligence Tasks:**  
        - Identify key trends, patterns, and outliers in the data.  
        - Highlight critical factors affecting business performance.  
        - Provide strategic recommendations based on the data.  
        - Suggest actions for optimizing operations, customer satisfaction, or revenue growth.  

        **User Question:**  
        {question}  

        Provide a detailed, well-structured response with actionable insights.
        """
    )

    prompt = template.format(data_summary=summary, question=question)

    response = chat([HumanMessage(content=prompt)])

    return {"question": question, "insights": response.content}


if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=4000)