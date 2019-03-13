from flask import Flask
from flask import render_template
import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/view')
def view_db():
    engine = db.engine.create_engine('mysql+pymysql://root:lab2014@localhost/mpf', echo=True)
    connection = engine.connect()
    metadata = db.MetaData()
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    class Product(Base):
        __tablename__ = 'product'
        productID = Column(Integer, primary_key=True)
        name = Column(String)
        photoURL = Column(String)

        def __repr__(self):
            return "<Product(id='%s', name='%s', photoURL='%s')" % (self.productID, self.name, self.photoURL)

    r = session.query(Product.productID, Product.name, Product.photoURL)
    return render_template("view.html", result=r)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


