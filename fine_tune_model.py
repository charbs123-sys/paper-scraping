from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()
token = os.environ.get("hugging_face_token")
print(token)
#login(token = 'hugging_face_token')