doctors = Doctor.query.all()

for d in doctors:
    db.session.delete(d)
db.session.commit()