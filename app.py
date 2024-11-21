from config import Config
from flask import Flask
from src.db.database import db
from src.sales.router import sales_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(sales_bp)
@app.route("/")
def index():
    return "Hola mundo :)"
if __name__ == "__main__":
    app.run(debug=True)