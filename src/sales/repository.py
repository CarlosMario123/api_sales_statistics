from sqlalchemy import func
from src.db.models.ventas import  Ventas
from datetime import datetime, timedelta

class SalesRepository:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_weekly_sales_count(self):
        today = datetime.today()
        week_ago = today - timedelta(days=7)
        return self.db_session.query(func.count(Ventas.id)).filter(Ventas.createdAt >= week_ago).scalar()

    def get_sales_by_day(self, days_back=14):
        today = datetime.today()
        start_date = today - timedelta(days=days_back)
        return self.db_session.query(
            func.dayofweek(Ventas.createdAt).label('day_of_week'),
            func.sum(Ventas.precio_Fn).label('total_sales')
        ).filter(Ventas.createdAt >= start_date).group_by('day_of_week').all()
