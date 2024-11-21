from flask import Blueprint, jsonify
from src.sales.service import SalesService
from src.sales.repository import SalesRepository
from src.db.database import db

sales_bp = Blueprint('sales', __name__)

sales_repository = SalesRepository(db.session)
sales_service = SalesService(sales_repository)

@sales_bp.route('/sales/weekly', methods=['GET'])
def get_weekly_sales():
    weekly_sales = sales_service.calculate_weekly_sales()
    return jsonify({"weekly_sales": weekly_sales})

@sales_bp.route('/sales/probability', methods=['GET'])
def get_sales_probability():
    probabilities = sales_service.calculate_sales_probability()
    return jsonify({"sales_probabilities": probabilities})
