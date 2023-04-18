from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
app=Flask(__name__)
app.config['SECRET_KEY'] = '323b22caac41acbf'
app.config["SQLALCHEMY_DATABASE_URI"] =  'mysql://root:root@localhost/arjundb'

db = SQLAlchemy(app)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    quantity = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

class Location(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

class ProductMovement(db.Model):
    movement_id = db.Column(db.Integer, primary_key=True)
    from_location = db.Column(db.String(50))
    to_location = db.Column(db.String(50))
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"))
    quantity = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

with app.app_context():
    db.create_all()
    db.session.commit()


@app.route('/')
def index():
    products = Product.query
    return render_template('product_table.html', title='Product Table',
                           products=products)
@app.route('/locations')
def locations():
    locations = Location.query
    return render_template('location_table.html', title='Location Table',
                           locations=locations)

@app.route('/pms')
def pms():
    pms = db.session.query(ProductMovement, Product).join(Product).all()
    return render_template('product_movement_table.html', title='Product Movement Table',
                           pms=pms)

@app.route('/location/edit/<int:location_id>' , methods=["GET", "POST"])
def edit_location(location_id):
    loc = Location.query.get_or_404(location_id)
    if request.method == "POST":
        print(request.form["name"])
        loc.name = request.form["name"]
        db.session.add(loc)
        db.session.commit()
        flash('Location has been edited!')
        return redirect('/locations')
    
    return render_template('edit_location.html', title='Edit Location', location=loc)


@app.route('/post/edit/<int:product_id>' , methods=["GET", "POST"])
def edit_product(product_id):
    pro = Product.query.get_or_404(product_id)
    if request.method == "POST":
        pro.name = request.form["name"]
        pro.quantity = request.form["quantity"]
        db.session.add(pro)
        db.session.commit()
        flash('Product has been edited!')
        return redirect('/')
    
    return render_template('edit_product.html', title='Edit Product', product=pro)

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    
    if request.method == "POST":
        print(request.form["name"])
        print(request.form["quantity"])
        product = Product(name=request.form["name"],quantity=request.form["quantity"])
        db.session.add(product)
        try:
            db.session.commit()
            flash(f'Your Product {request.form["name"]} has been added!', 'success')
            return redirect('/')
        except IntegrityError :
            db.session.rollback()
            flash(f'This Product already exists','danger')
            return redirect('/')
        
    return render_template("addProduct.html",title='Add Product')

@app.route("/add_location", methods=["GET", "POST"])
def location_add():
    
    if request.method == "POST":
        print(request.form["name"])
        loc = Location(name=request.form["name"])
        db.session.add(loc)
        try:
            db.session.commit()
            flash(f'Your Location {request.form["name"]} has been added!', 'success')
            return redirect('/locations')
        except IntegrityError :
            db.session.rollback()
            flash(f'This Location already exists','danger')
            return redirect('/locations')
        
    return render_template("addLocation.html",title='Add Location')


@app.route("/add_pm", methods=["GET", "POST"])
def pm_add():
    
    if request.method == "POST":
        pm = ProductMovement(product_id=request.form["product_id"], quantity=request.form["quantity"],
                             from_location=request.form["from_location"], to_location=request.form["to_location"])
        db.session.add(pm)
        try:
            db.session.commit()
            flash(f'New Product Movement has been added!', 'success')
            return redirect('/pms')
        except IntegrityError :
            db.session.rollback()
            flash(f'This Product Movement already exists','danger')
            return redirect('/pms')
        
    products = Product.query
    locations = Location.query
    return render_template("addPM.html",title='Add Product Movement', products=products, locations=locations)



@app.route("/delete")
def delete():
    type = request.args.get('type')
    if type == 'product':
        pid = request.args.get('product_id')
        product = Product.query.filter_by(product_id=pid).delete()
        db.session.commit()
       # return redirect(url_for('/'))
        flash('Product Deleted!')
        products = Product.query
        return render_template('product_table.html', title='Product Table',
                           products=products)
    elif type == 'location':
        lid = request.args.get('location_id')
        product = Location.query.filter_by(location_id=lid).delete()
        db.session.commit()
    
        flash('Location Deleted!')
        locations = Location.query
        return render_template('location_table.html', title='Location Table',
                           locations=locations)

app.run(host='0.0.0.0', port=81)