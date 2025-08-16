from fastapi import FastAPI
from pydantic import BaseModel
import jwt
import time

# بيانات Stream الخاصة بيك
API_KEY = "qcn666ttrhvb"
API_SECRET = "bgw93xfbgnu2mm88g9w8kev2qsj9g3ts8h7ra2a8qmhautpzcujnzy5n6dycb4ty"

app = FastAPI()

class User(BaseModel):
    user_id: str

@app.post("/get_token")
def get_token(user: User):
    payload = {
        "user_id": user.user_id,
        "iat": int(time.time()),              # وقت إنشاء التوكين
        "exp": int(time.time()) + 3600,       # صلاحية ساعة واحدة
    }
    token = jwt.encode(payload, API_SECRET, algorithm="HS256")
    return {
        "user_id": user.user_id,
        "token": token,
        "api_key": API_KEY
    }