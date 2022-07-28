from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import user, post
from services import services as _services
from myData import getIpAddress as getIp

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000", getIp()],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

_services.create_database()

app.include_router(user.router)
app.include_router(post.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)