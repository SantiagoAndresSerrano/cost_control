import datetime 
from flask import Blueprint, request
from flask_api import status

from app.model.bill import Bill
from ..model.users import Users
from ..schema.user_schema import user_schema, users_schema
from ..schema.bill_schema import bill_schema, bills_schema
from ..utils.db import db
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound

users = Blueprint("users",__name__)


@users.route("/users/<string:user>/bills", methods=["POST"])
def saveBill(user):
    try:
        userFound = Users.query.filter(Users.username == user).one()
    except NoResultFound:
        return "user with username "+user+" not found", status.HTTP_404_NOT_FOUND
    try:
        type_ = int(request.json["type"])
        value = int(request.json["value"])
        observation = request.json["observation"]
        date_bill = datetime.date.today()
        bill = Bill(None, date_bill, userFound.id, value, type_, observation)
        db.session.add(bill)
        db.session.commit()

    except ValueError:
        return "invalid data", status.HTTP_400_BAD_REQUEST

    return bill_schema.dump(bill), status.HTTP_200_OK

@users.route("/users" , methods=["GET"]) 
def getAllUser():
    all_users= Users.query.all()
    return users_schema.dump(all_users), status.HTTP_200_OK

@users.route("/users/<string:user>/bills" , methods=["GET"]) 
def getAllBillsByUsername(user):
    try:
        userFound = Users.query.filter(Users.username == user).one()
        idUser= userFound.id
        bills = Bill.query.filter(Bill.user_id == idUser).all()
        return bills_schema.dump(bills), status.HTTP_200_OK
    except NoResultFound:
        return "user with username "+user+" not found", status.HTTP_401_UNAUTHORIZED


@users.route("/users/<string:user>/bills/<int:bill_id>" , methods=["GET"]) 
def getBillByUsername(user, bill_id):
    try:
        userFound = Users.query.filter(Users.username == user).one()
        idUser= userFound.id
        bill = Bill.query.filter(and_(Bill.user_id == idUser,Bill.id == bill_id)).one()
        
        return bill_schema.dump(bill), status.HTTP_200_OK
    except NoResultFound:
        return "user or bill not found", status.HTTP_404_NOT_FOUND



@users.route("/users/<string:user>/bills/<int:bill_id>" , methods=["DELETE"]) 
def deleteBill(user, bill_id):
    try:
        userFound = Users.query.filter(Users.username == user).one()
        idUser= userFound.id
        bill = Bill.query.filter(and_(Bill.user_id == idUser,Bill.id == bill_id)).one()
        db.session.delete(bill)
        db.session.commit()
        return bill_schema.dump(bill), status.HTTP_200_OK

    except NoResultFound:
        return "user or bill not found", status.HTTP_404_NOT_FOUND


@users.route("/login", methods=["POST"])
def login():
    try:
        username = request.json["username"]
        password = request.json["password"] 
        user = Users.query.filter(and_(Users.username == username, Users.password == password)).one()
        response = {
            "login": True,
            "username": user.username,
            "email": user.email,
            "mensaje": "Welcome"
        }

        return response, status.HTTP_200_OK

    except NoResultFound:
        response = {'login':False, 'mensaje':"Usuario o contraseña invalido"}
        return response, status.HTTP_400_BAD_REQUEST
