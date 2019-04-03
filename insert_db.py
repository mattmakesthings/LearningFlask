from app import db
from app.models import Doctor, Office

offices = [ Office(address='1212 somewhere rd.',city='LA',state='CA',id=1),
            Office(address='1212 somewhere else rd.',city='SF',state='CA',id=2)]

for o in offices:
    db.session.add(o)
db.session.commit()

doctors = [Doctor(id=1,first_name = "james", last_name = "wilson", specialty = "oncology", office_id = "2",rating=3.5),
           Doctor(id=2,first_name = "lisa", last_name = "cuddy", specialty = "endocrinology", office_id = "1",rating=4.0),
           Doctor(id=3,first_name = "greg", last_name = "house", specialty = "diagnostic medicine", office_id = "1",rating=4.5),
           Doctor(id=4,first_name = "john", last_name = "dorian", specialty = "family medicin", office_id = "1",rating=2.5),
           Doctor(id=5,first_name = "adnan", last_name = "choudhury", specialty = "oncology", office_id = "2",rating=5.0),
           Doctor(id=6,first_name = "doogie", last_name = "hauser", specialty = "oncology", office_id = "2",rating=5.0),
           Doctor(id=7,first_name = "turk", last_name = "turkleton", specialty = "family medicine", office_id = "1",rating=2.5),
           Doctor(id=8,first_name = "perry", last_name = "cox", specialty = "family medicine", office_id = "1",rating=1.5),]
for d in doctors:
    db.session.add(d)
db.session.commit()

