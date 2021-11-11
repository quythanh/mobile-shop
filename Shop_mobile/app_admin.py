import os
import os.path as op
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Markup
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user
from flask_admin.contrib import sqlamodel
from Shop_mobile.Xu_ly.Xu_ly_Model import *
from Shop_mobile.Xu_ly.frm_admin import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from sqlalchemy.orm import configure_mappers
from flask_admin import BaseView, expose
from Shop_mobile import app
import flask_admin as admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import helpers, expose

configure_mappers()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbSession = DBSession()

class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).render('my_master.html')

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p style="text-align:center">Chưa có tài khoản? <a href="' + url_for('.register_view') + '">Click đăng ký.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).render('admin/login.html')

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()
            form.populate_obj(user)
            user.password = generate_password_hash(form.password.data)
            user.ma_loai_nguoi_dung=0
            dbSession.add(user)
            dbSession.commit()
            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p style="text-align:center">Đã có tài khoản? <a href="' + url_for('.login_view') + '">Click vào đây để đăng nhập.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).render('admin/dang_ky.html')

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Initialize flask-login
init_login()
admin = admin.Admin(app, 'bán tivi', index_view=MyAdminIndexView(name="TTTH"), base_template='my_master.html', template_mode='bootstrap3')

class Nguoi_dung_View(ModelView):
    column_display_pk = True # Hiển thị cột khóa chính. Mặc định False
    can_create = True # Mặc định True: có thể thêm mới
    can_delete = True # Mặc định True: Có thể xóa
    can_export = True # Xuất thành file excel. Mặc định False
    can_edit = False # Mặc định True: có thể chỉnh sửa
    page_size = 20 # Hiển thị 20 dòng trên 1 trang
    column_list = ('ten_dang_nhap', 'mat_khau', 'ho_ten')
    form_columns = ('ten_dang_nhap', 'mat_khau', 'ho_ten', 'email', 'dien_thoai', 'ma_trang_thai')

admin.add_view(Nguoi_dung_View(Nguoi_dung, dbSession))