from flask_restful import Resource
from app.models import Bird
from flask import jsonify,make_response,request
from app.db import db


class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

    def post(self):

        data = request.get_json()
        name=data.get("name")
        species=data.get("species")
        image=data.get("image")

        # new_bird = Bird(
        #     name=data['name'],
        #     species=data['species'],
        #     image=data['image'],
        # )
        if name and species and image:

            new_bird=Bird(name=name,species=species,image=image)

            db.session.add(new_bird)
            db.session.commit()

            response=new_bird.to_dict()

            return make_response(response, 201)

        return {"message":"Provide data for all fields"}

        


class BirdByID(Resource):
    
    def get(self, id):
        bird = Bird.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(bird), 200)

    def patch(self, id):

        data = request.get_json()

        bird = Bird.query.filter_by(id=id).first()

        for attr in data:
            setattr(bird, attr, data[attr])

        db.session.add(bird)
        db.session.commit()

        return make_response(bird.to_dict(), 200)

    def delete(self, id):

        bird = Bird.query.filter_by(id=id).first()
        db.session.delete(bird)
        db.session.commit()

        #return make_response('', 204)
        return {},204