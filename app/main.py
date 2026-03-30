from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
async def health_check():
    return {"message": "System is working fine."}
