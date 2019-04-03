from app import db
from app.models import Doctor, Office

offices = Office.query.all()

for o in offices:
    db.session.delete(o)
db.session.commit()

doctors = Doctor.query.all()

for d in doctors:
    db.session.delete(d)
db.session.commit()