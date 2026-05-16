from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import router as chat_router
from middleware.error_handler import global_exception_handler

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request


app = FastAPI(
    title="AI-ChatBot"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(chat_router)

templates=Jinja2Templates(directory="frontend/templates")
@app.get("/",response_class=HTMLResponse)

async def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

app.add_exception_handler(Exception, global_exception_handler)


@app.get("/")
def main():
    return {
        "message": "AI-ChatBot Running"
    }


@app.get("/health")
def health_checkk():
    return {
        "status": "healthy"
    }

