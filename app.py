from fastapi import FastAPI
from workflows.email_triage import EmailTriageWorkflow

app = FastAPI(
    title="Autonomous Workplace Agent",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "name": "Autonomous Workplace Agent",
        "version": "0.1.0"
    }

@app.post("/triage")
def triage(message: str):

    workflow = EmailTriageWorkflow()

    return workflow.run(message)
