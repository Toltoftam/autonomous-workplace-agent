DANGEROUS=["ignore previous instructions","reveal system prompt"]

def scan(text):
 return any(x in text.lower() for x in DANGEROUS)