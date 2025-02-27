from flask import Flask
from src.main.routes.event import event_route_bp
from src.main.routes.event_link import event_link_route_bp
from src.main.routes.sub import sub_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)
app.register_blueprint(sub_route_bp)
app.register_blueprint(event_link_route_bp)
