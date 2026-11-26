from datetime import datetime

def log(action):
 return {"action":action,"timestamp":datetime.utcnow().isoformat()}