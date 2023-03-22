from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.ping_models import ping_model
import json

router = APIRouter()

@router.get("/status")
async def status(models: str = ""):
    model_list = models.split(",") if models else []
    availability = {}
    for model in model_list:
        is_available = ping_model(model)
        availability[model] = {"is_available": str(is_available).lower()}

    formatted_json = json.dumps(availability, indent=2, separators=(',', ': '))
    return JSONResponse(content=json.loads(formatted_json))
