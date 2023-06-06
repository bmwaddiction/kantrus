from fastapi import APIRouter, FastAPI
from fastapi.openapi.utils import get_openapi
import json

router = APIRouter()

@router.get('/generateOpenAPIDefinition')
async def generate_openapi_definition():
    from main import app
    openapi_schema = get_openapi(
        title="Kantrus",
        description="Kantrus Server",
        version="1.0.0",
        routes=app.routes
    )
    with open("openapi.json", "w") as file:
        json.dump(openapi_schema, file)
    return {"message": "OpenAPI definition generated"}
