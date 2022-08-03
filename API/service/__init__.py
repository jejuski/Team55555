from flask import Blueprint

customer_v1 = Blueprint('customer_v1_routes', __name__)

from .customer_v1_routes import *