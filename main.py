from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase
from langchain_groq import ChatGroq
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
import os
from dotenv import load_dotenv
import uvicorn
# Load environment variables
load_dotenv()

app = FastAPI()

# Request model for database connection
data_store = {}

class DBConfig(BaseModel):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    api_key: str  # Groq API Key

class QueryRequest(BaseModel):
    query: str

def get_sql_agent(db_url: str, api_key: str):
    try:
        engine = create_engine(db_url)
        db = SQLDatabase(engine)
        llm = ChatGroq(api_key=api_key, model='gemma2-9b-it')
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
        return create_sql_agent(llm=llm, toolkit=toolkit, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

@app.post("/connect")
def connect_db(config: DBConfig):
    db_url = f"postgresql://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
    try:
        agent = get_sql_agent(db_url, config.api_key)
        data_store["agent"] = agent  
        return {"message": "Database connected successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
def execute_query(request: QueryRequest):
    agent = data_store.get("agent")
    if not agent:
        raise HTTPException(status_code=400, detail="Database not connected. Please connect first.")
    try:
        result = agent.run(request.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query execution error: {str(e)}")

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI SQL Analysis API! Use /connect to set up the database and /query to run queries."}


if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=4000)