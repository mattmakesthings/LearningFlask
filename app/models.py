from app import db
from sqlalchemy.sql import func

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64),index = True, unique = False)
    last_name = db.Column(db.String(64),index = True, unique = False)
    specialty = db.Column(db.String(64),index = True, unique = False)
    rating = db.Column(db.Float,index=True)
    office_id = db.Column(db.Integer,db.ForeignKey('office.id'))
    office = db.relationship('Office')
    

    # similar doctors have same specialty and work in same city
    def get_similar_doctors(self):
        o = Office.query.get(self.office_id)
        d = Doctor.query.join(Doctor.office).filter_by(city = o.city, state = o.state).filter(Doctor.id != self.id,Doctor.specialty == self.specialty).all()
        return d

    def __repr__(self):
        return '\nDoctor id: {}\n\tfirst_name: {}\n\tlast_name: {}\n\tspecialty: {}\n\toffice: {}'.format(self.id,
                                                                                       self.first_name,
                                                                                       self.last_name,
                                                                                       self.specialty,
                                                                                       self.office)

# class Review(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     doctor_id = db.Column(db.Integer,db.ForeignKey("doctor.id"))
#     rating = db.Column(db.Integer)

class Office(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String(64),index = True, unique = False)
    city = db.Column(db.String(64),index = True, unique = False)
    state = db.Column(db.String(64),index = True, unique = False)

    def __repr__(self):
        return '\nOffice id: {}\n\taddress: {}\n\tcity: {}\n\tstate: {}'.format(self.id,self.address,self.city,self.state)