from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("home.html", {"request": request})
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, host="0.0.0.0",
                reload=True, access_log=False)

    