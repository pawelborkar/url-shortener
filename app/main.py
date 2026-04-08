from fastapi import FastAPI
from app.api.v1.link import router


app = FastAPI(debug=True, title="Cutlet: The URL shortener API docs")


app.include_router(router)


@app.get("/health")
async def health_check():
    return {"message": "System is working fine."}
