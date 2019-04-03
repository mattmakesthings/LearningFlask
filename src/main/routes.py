# from app import app
from flask import render_template
from src.models import Doctor
from src.main import bp

import operator


@bp.route('/')
@bp.route('/all_doctors')
@bp.route('/all_doctors/<attribute>')
def index(attribute=None):
    doctors = Doctor.query.all()
    if(attribute == None):
        return render_template('all_doctors.html',doctors = doctors)
    else:
        if attribute == "rating":
            reverse = True
        else:
            reverse = False
        doctors.sort(key=operator.attrgetter(attribute),reverse = reverse)
        return render_template('all_doctors.html',doctors = doctors)

@bp.route('/doctors/<id>')
def details(id):
    selected_doctor = Doctor.query.get(id)
    # doctors are selected based on specialty on being located in the same city
    doctors = selected_doctor.get_similar_doctors()
    # then sorted by rating in descending order
    doctors.sort(key=operator.attrgetter('rating'),reverse = True)
    return render_template('doctor_detail.html', selected = selected_doctor, doctors = doctors)
