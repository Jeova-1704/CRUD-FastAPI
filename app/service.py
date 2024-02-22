from sqlalchemy.orm import Session
from model import Book
from schemas import BooksSchema


def get_book(db:Session, skipt:int=0, limit:int=100):
    return db.query(Book).offset(skipt).limit(limit).all()


def get_book_by_id(db:Session, book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db:Session, book: BooksSchema):
    _book = Book(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)  # Corrigir aqui
    db.delete(_book)
    db.commit()



def update_book(db:Session, id:int, title:str, description:str):
    _book = get_book_by_id(db=db, book_id=id)
    _book.title = title
    _book.description = description
    db.commit()
    db.refresh(_book)
    return _book
