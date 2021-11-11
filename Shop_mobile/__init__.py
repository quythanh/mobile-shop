from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'ShopMobile'

import Shop_mobile.app_san_pham
import Shop_mobile.Xu_ly.Xu_ly_Model
import Shop_mobile.app_admin
import Shop_mobile.app_khach_hang
import Shop_mobile.app_quan_li