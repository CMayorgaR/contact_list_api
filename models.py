from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact (db.Model):
    __tablename__='contact'
    id= db.Column(db.Integer, primary_key=True)
    full_name=db.Column(db.String(70), nullable=False)
    email=db.Column(db.String(70), nullable=False)
    address=db.Column(db.String(100), nullable=False)
    phone=db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Contact %r>" % self.full_name
    
    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "address":self.address,
            "phone":self.phone
            }