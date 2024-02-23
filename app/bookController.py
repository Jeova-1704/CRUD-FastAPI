from fastapi import APIRouter, HTTPException, Path, Depends
from config import sessionLocal
from sqlalchemy.orm import Session
from schemas import BooksSchema, RequestBook, Response
import service 

router = APIRouter()

async def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request: RequestBook, db: Session = Depends(get_db)):
    _book = service.create_book(db, book=request.parameter)
    return Response(code="201", status="ok", message="Livro criado com sucesso", result=_book).dict(exclude_none=True)


@router.get("/")
async def get(db: Session = Depends(get_db)):
    _book = service.get_book(db, 0, 100)
    return Response(code="200", status='ok', message="Success Fetch all data", result=_book).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _book = service.get_book_by_id(db, id)
    return Response(code="200", status="ok", message="Success get data", result=_book).dict(exclude_none=True)


@router.put("/update")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    _book = service.update_book(db, id=request.parameter.id, title=request.parameter.title, description=request.parameter.description)
    return Response(code="200", status="ok", message="success update data", result=_book).dict(exclude_none=True)


@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    service.remove_book(db, book_id=id)
    return Response(code="204", status="ok", message="success delete data", result=None).dict(exclude_none=True)
