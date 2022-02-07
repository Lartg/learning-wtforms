from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Store Title')
    address = StringField('Store Address')
    submit = SubmitField('Submit')


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Item Name')
    price = FloatField('Price')
        # validators=[
        #     #must have 2 decimals
        # ])
    category = SelectField('Item Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo URL')
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')

