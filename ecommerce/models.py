from dataclasses import dataclass
from ecommerce import db


@dataclass
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    activated = db.Column(db.Boolean, default=True)

    def __init__(self, id, username, email, password, activated):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.activated = activated
@dataclass
class Admin(db.Model):
    __tablename__="admin"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(120), nullable=False)
    mod = db.Column(db.Integer, default=0)

    def __init__(self, id, name, email, password, mod):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.mod = mod

@dataclass
class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, id, name):
        self.id = id
        self.name = name
@dataclass
class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.Float)
    oldPrice = db.Column(db.Float)
    description = db.Column(db.String(120))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    def __init__(self, id, name, price, oldPrice, description, category_id):
        self.id = id
        self.name = name
        self.price = price
        self.oldPrice = oldPrice
        self.description = description
        self.category_id = category_id