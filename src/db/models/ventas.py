from src.db.database import db

class Ventas(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.String(255), primary_key=True)  # Especificar tamaño para VARCHAR
    precio_Fn = db.Column(db.Float, nullable=False)
    id_mesa = db.Column(db.String(255), nullable=False)  # Especificar tamaño para VARCHAR
    estado = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=db.func.current_timestamp())
