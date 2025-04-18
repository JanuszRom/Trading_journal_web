from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    instrument = db.Column(db.String(20))
    direction = db.Column(db.String(10))
    entry = db.Column(db.Float)
    exit = db.Column(db.Float)
    stop_loss = db.Column(db.Float)
    take_profit = db.Column(db.Float)
    size = db.Column(db.Float)
    risk = db.Column(db.Float)
    reward = db.Column(db.Float)
    profit_loss = db.Column(db.Float)
    duration = db.Column(db.String(20))
    strategy = db.Column(db.String(100))
    setup = db.Column(db.Text)
    mistakes = db.Column(db.Text)
    lessons = db.Column(db.Text)
    screenshots = db.relationship('Screenshot', backref='trade', lazy=True)

class Screenshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    filepath = db.Column(db.String(255))
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    trade_id = db.Column(db.Integer, db.ForeignKey('trade.id'), nullable=False)