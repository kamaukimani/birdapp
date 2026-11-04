from flask import Flask,render_template 
from flask_restful import Api 
from .db import db,migrate 
from .config import Config  
from .models import *
from flask_cors import CORS
from .routes import *

def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)

    CORS(app,origins=["http://localhost:3000","http://127.0.0.1:3000"],supports_credentials=True)

    db.init_app(app)
    migrate.init_app(app,db)



    api=Api(app)

    api.add_resource(Birds, '/birds')
    api.add_resource(BirdByID, '/birds/<int:id>')

    @app.errorhandler(404)
    def not_found(e):
        return render_template("index.html")


    return app