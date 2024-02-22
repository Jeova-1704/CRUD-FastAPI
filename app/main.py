from fastapi import FastAPI
import model
from config import engine
import bookController

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def Home():
    return "Hello word"


app.include_router(bookController.router,prefix="/book", tags="book")