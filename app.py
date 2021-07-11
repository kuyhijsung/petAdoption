from flask import Flask, url_for, render_template, redirect, flash, jsonify
from models import db, connect_db, Pet
# from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
connect_db(app)
db.create_all()


@app.route("/")
def list_pets():
    """List all pets."""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)


# @app.route("/add", methods=["GET", "POST"])
# def add_pet():
#     """Add a pet."""

#     form = AddPetForm()

#     if form.validate_on_submit():
#         data = {k: v for k, v in form.data.items() if k != "csrf_token"}
#         new_pet = Pet(**data)
#         # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
#         # db.session.add(new_pet)
#         # db.session.commit()
#         flash(f"{new_pet.name} added.")
#         return redirect(url_for('list_pets'))

#     else:
#         # re-present form for editing
#         return render_template("pet_add_form.html", form=form)
