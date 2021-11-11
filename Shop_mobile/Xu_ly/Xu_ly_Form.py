from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, PasswordField, StringField, validators, ValidationError
from wtforms.widgets import PasswordInput
from flask_ckeditor import CKEditorField
 
class Form_Dang_ki(Form):  
    Th_Ho_ten = TextField("Họ tên",[validators.Required("Vui lòng nhập họ tên.")])
    Th_ten_dang_nhap = TextField("Tên đăng nhập", [validators.Required("Vui lòng nhập tên đăng nhập.")])
    Th_mat_khau = PasswordField("Mật khẩu", [validators.Required("Vui lòng nhập mật khẩu.")])
    Th_nhap_lai_mat_khau = PasswordField("Nhập lại mật khẩu", [validators.Required("Vui lòng nhập lại mật khẩu.")])
    Th_Phai = RadioField("Giới tính", choices = [('1', 'Nam'), ('0', 'Nữ')], default='0')
    Th_Ngay_sinh = TextField("Ngày sinh")
    Th_Dia_chi = TextField("Địa chỉ",[validators.Required("Vui lòng nhập địa chỉ.")])
    Th_Dien_thoai = TextField("Điện thoại",[validators.Required("Vui lòng nhập điện thoại.")])
    Th_Email = TextField("Email",[validators.Email("Vui lòng nhập đúng cấu trúc email.")])
    Th_submit = SubmitField("Đăng kí")

class Form_Dang_nhap(Form):
    Th_ten_dang_nhap = TextField("Tên đăng nhập", [validators.Required("Vui lòng nhập tên đăng nhập.")])
    Th_mat_khau = PasswordField("Mật khẩu", [validators.Required("Vui lòng nhập mật khẩu.")])
    Th_submit = SubmitField("Đăng nhập")

class Form_Gop_y(Form):
    Th_Ho_ten = TextField("Họ tên",[validators.Required("Vui lòng nhập họ tên.")])
    Th_Email = TextField("Email",[validators.Email("Vui lòng nhập email.")])
    Th_Ly_do = SelectField("Góp ý cho", choices = [('TGGH', 'Thời gian giao hàng'), ('CSKH', 'Chăm sóc khác hàng'), ('SP', 'Sản phẩm'), ('TDNV', 'Thái độ nhân viên'), ('KHAC', 'Khác')], default = 'TGGH')
    Th_Gop_y = CKEditorField("Nội dung")
    Th_submit = SubmitField("Gửi ý kiến")
