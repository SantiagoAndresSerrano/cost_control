from telnetlib import OUTMRK
from flask import Blueprint, jsonify
from ..model.bill import Bill
from ..schema.bill_schema import bill_schema, bills_schema
bills = Blueprint("bill",__name__)


@bills.route("/bills")
def listBills():
    return (bills_schema.dump(Bill.query.all()))

