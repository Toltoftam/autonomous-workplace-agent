from src.agents.base_agent import BaseAgent
 
 
class CustomerSupportAgent(BaseAgent):
 
def __init__(self):
super().__init__("CustomerSupportAgent")
 
def execute(self, request):
 
return {
"status": "drafted",
"response":
f"Thank you for contacting support regarding: {request}"
}
