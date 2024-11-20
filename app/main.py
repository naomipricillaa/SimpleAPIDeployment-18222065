import uvicorn
from fastapi import FastAPI, Depends
from .routers import secure, public
from .auth import get_user

app = FastAPI()

app.include_router(
    public.router,
    prefix="/api/v1/public"
)
app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)

@app.get("/")
async def root():
    return {"message": "Naomi Pricilla Agustine - 18222065"}   

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)