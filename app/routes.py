from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm, AddProductForm


@app.route('/')
@app.route('/Shop')
def shop ():
    """Shop URL"""
    return render_template('shop.html', title='Shop Page',)


@app.route('/Register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to login in {form.username.data}')
        return redirect('/Register') 
    return render_template('register.html', title='Register', form=form)


@app.route('/Add-Product', methods=['GET','POST']) 
def addproduct():
    """Add-Product URL"""
    form = AddProductForm()  
    if form.validate_on_submit():
        flash(f'You are requesting to login in {form.username.data}')
        return redirect('/Add-Product')  
    return render_template('Add_product.html', title='Add Product', form=form)

