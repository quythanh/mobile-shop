from wtforms import form, fields, validators
import flask_login as login
from Shop_mobile import app
from Shop_mobile.Xu_ly.Xu_ly_Model import *
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbSession = DBSession()
class LoginForm(form.Form):
	
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user')
        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')
            print('false ======================================')
            print(generate_password_hash(self.password.data))
            print(user.password)
        else:
            print('OK ======================================')
    def get_user(self):
        return dbSession.query(User).filter_by(login=self.login.data).first()

class RegistrationForm(form.Form):
	first_name = fields.StringField(validators=[validators.required()])
	last_name = fields.StringField(validators=[validators.required()])
	id_loai_nguoi_dung = fields.IntegerField()
	email = fields.StringField(validators=[validators.required()])
	login = fields.StringField(validators=[validators.required()])
	password = fields.PasswordField(validators=[validators.required()])

	def validate_login(self, field):
		if dbSession.query(User).filter_by(login=self.login.data).count() > 0:
			raise validators.ValidationError('Duplicate username')

# Initialize flask-login
def init_login():
	login_manager = login.LoginManager()
	login_manager.init_app(app)

	# Create user loader function
	@login_manager.user_loader
	def load_user(user_id):
		return dbSession.query(User).get(user_id)
