import os
from dotenv import load_dotenv
load_dotenv()


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("GOREST_TOKEN")}'
}