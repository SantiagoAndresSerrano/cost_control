from app.model.users import Users
from ..utils.ma import ma
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
user_schema = UserSchema()
users_schema = UserSchema(many=True)