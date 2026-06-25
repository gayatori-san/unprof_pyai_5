import re

text = """
Contact support@technova.com or admin@domain.org
Call +91-9876543210 or (555) 123-4567
Deployment: 15/04/2026, Next audit: 2026-05-20
"""

# Extract emails
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Emails:", emails)

# Extract phone numbers
phones = re.findall(r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
print("Phones:", phones)

# Extract dates
dates = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2}', text)
print("Dates:", dates)