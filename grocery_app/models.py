from sqlalchemy_utils import URLType
from flask_login import UserMixin
from .extensions import db
from .utils import FormEnum

class ItemCategory(FormEnum):
    """Categories of grocery items."""
    PRODUCE = 'Produce'
    DELI = 'Deli'
    BAKERY = 'Bakery'
    PANTRY = 'Pantry'
    FROZEN = 'Frozen'
    OTHER = 'Other'

class GroceryStore(db.Model):
    """Grocery Store model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    items = db.relationship('GroceryItem', back_populates='store')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   

class GroceryItem(db.Model):
    """Grocery Item model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.Enum(ItemCategory), default=ItemCategory.OTHER)
    photo_url = db.Column(URLType)
    store_id = db.Column(
        db.Integer, db.ForeignKey('grocery_store.id'), nullable=False)
    store = db.relationship('GroceryStore', back_populates='items')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    shopping_list_items = db.relationship(
        'User',
        secondary='shopping_list',
        back_populates='shopping_list_items'
    )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(), nullable=False)
    shopping_list_items = db.relationship(
        'GroceryItem',
        secondary='shopping_list',
        back_populates='shopping_list_items'
    )

shopping_list_table = db.Table('shopping_list',
    db.Column('item_id', db.Integer, db.ForeignKey('grocery_item.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )