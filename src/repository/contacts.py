from datetime import date
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel


async def create_contact(body: ContactModel, db: Session):
    contact = Contact(**body.dict(), user_id=user.id)
    db.add(contact)
    db.commit()
    return contact


async def update_contact(user: User, contact_id: int, body: ContactModel, db: Session):
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        contact.additional_data = body.additional_data
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_contact(keyword: str, db: Session):
    contacts = db.query(Contact).filter(and_(Contact.user_id == user.id,
                                             (Contact.first_name.ilike(f"%{keyword}%")) |
                                             (Contact.last_name.ilike(f"%{keyword}%")) |
                                             (Contact.email.ilike(f"%{keyword}%"))
                                             )).all()
    return contacts


async def get_contacts(db: Session):
    contacts = db.query(Contact).filter(and_(Contact.user_id == user.id)).all()
    return contacts


async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    return contact


async def get_contact_by_email(email: str, db: Session):
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, email == email)).first()
    return contact


async def get_contact_by_phone(phone_number: str, db: Session):
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, phone_number == phone_number)).first()
    return contact


async def get_birthdays(days: int, db: Session):
    contacts_with_birthdays = []
    today = date.today()
    current_year = today.year
    contacts = db.query(Contact).filter(and_(Contact.user_id == user.id)).all()
    for contact in contacts:
        td = contact.birthday.replace(year=current_year) - today
        if 0 <= td.days <= days:
            contacts_with_birthdays.append(contact)
        else:
            continue
    return contacts_with_birthdays

