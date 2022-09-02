from ..model.bill import Bill
from ..utils.ma import ma
from marshmallow import fields
class BillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Bill
        load_instance = True
        type_=fields.Number(attribute="type")
    user = ma.Function(lambda obj: obj.user.username)
        
bill_schema = BillSchema()
bills_schema =BillSchema(many=True, exclude=("user",))