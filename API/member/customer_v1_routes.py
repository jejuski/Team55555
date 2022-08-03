from . import customer_v1
from services.customer_v1_service import CustomerService
from flask import request, Response
from util.print_util import *
import json


# Get Login Auth
@customer_v1.route('/auth', methods=['POST'])
def loginAuth():
    user_info = request.get_json()
    if (user_info is not None):
        if (user_info['username'] is None):
            ...

        customer = CustomerService()
        result = customer.create_jwt_token(user_info['username'], user_info['password'])


...


# Get Customer Stats
@customer_v1.route('/stats_customer', methods=['GET'])
def getCustomerStats():
    query_dict = request.args.to_dict()


...


# Get Customer Msg_History
@customer_v1.route('/msg_histories', methods=['GET'])
def getMsgHistory():
    query_dict = request.args.to_dict()


...