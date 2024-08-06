from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1,64)])
    email = StringField('E-mail', validators=[DataRequired(), Length(1,32), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(1,16)])
    confirm_password =  PasswordField('Confirm Password', validators=[DataRequired(), Length(1,64), EqualTo("password")])
    submit = SubmitField('Register')

class AddProductForm(FlaskForm):
    """Add Product Form"""
    product_name = StringField('Product Name', validators=[DataRequired(), Length(1,64)])
    product_description = PasswordField('Product Description', validators=[DataRequired(), Length(1,64)])
    stock_available = SelectField('Stock Available', choices=[('1', '1'), ('5', '5'), ('12', '12'), ('20', '20')])
    submit = SubmitField('Add product')