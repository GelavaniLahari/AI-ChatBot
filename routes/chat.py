from fastapi import APIRouter
from models.request_models import ChatRequest
from fastapi.responses import StreamingResponse
from services.llm_service import  get_llm_response,stream_response


from utils.helpers import history

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):
    response = await get_llm_response(request.question)

    return {
        "response": response
    }

@router.post("/stream-chat")
async def stream_chat(request:ChatRequest):
    return StreamingResponse(
        stream_response(request.question),
        dia_type="text/plane"
    )

@router.get("/history")
async def get_history():
    return{
        "history":history
    }
