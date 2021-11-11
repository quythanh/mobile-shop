from flask import render_template, request, Markup, session, redirect
from Shop_mobile import app
from Shop_mobile.Xu_ly.Xu_ly_Form import *
from Shop_mobile.Xu_ly.Xu_ly_Mail import *
from Shop_mobile.app_san_pham import *
from Shop_mobile.app_quan_li import *
from Shop_mobile.Xu_ly.Xu_ly_Database import *
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
from datetime import datetime

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testmailpython513@gmail.com'
app.config['MAIL_PASSWORD'] = 'T_H*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

ckeditor = CKEditor(app)
mail = Mail(app)

@app.route('/khach-hang/dang-ki', methods=['GET', 'POST'])
def Dang_ki():
    form = Form_Dang_ki()
    Thong_bao = ''
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('dang_ki.html', form = form)
        else:
            # Lấy dữ liệu trên HTML
            Ho_ten = request.form.get("Th_Ho_ten")
            Ten_dang_nhap = request.form.get("Th_ten_dang_nhap")
            Mat_khau = request.form.get("Th_mat_khau")
            Nhap_lai_mat_khau = request.form.get("Th_nhap_lai_mat_khau")
            Gioi_tinh = request.form.get("Th_Phai")
            Ngay_sinh = request.form.get("Th_Ngay_sinh")
            Dia_chi = request.form.get("Th_Dia_chi")
            Dien_thoai = request.form.get("Th_Dien_thoai")
            Email = request.form.get("Th_Email")

            # Lưu vào Databse
            if Nhap_lai_mat_khau == Mat_khau:
                kt = Kiem_tra_tai_khoan(Ten_dang_nhap)
                if kt == True:
                    ChuoiSQL = "INSERT into nguoi_dung(ho_ten, ten_dang_nhap, mat_khau, gioi_tinh, ngay_sinh, dia_chi, dien_thoai, email, ma_trang_thai) values(?,?,?,?,?,?,?,?,?)"
                    kq = execute(ChuoiSQL,(Ho_ten, Ten_dang_nhap, Mat_khau, int(Gioi_tinh), Ngay_sinh, Dia_chi, Dien_thoai, Email, 3))
                    if kq == 1:
                        Thong_bao = 'Đăng kí thành công. Nhấn vào <a href="/khach-hang/dang-nhap">đây</a> để đăng nhập'
                else:
                    Thong_bao = '<h3><b>Tên đăng nhập đã tồn tại! Vui lòng sử dụng tên đăng nhập khác.</b></h3>'
                return render_template('dang_ki.html', Thong_bao = Markup(Thong_bao), form = form)

    elif request.method == 'GET':
        return render_template('dang_ki.html', form = form)

@app.route('/khach-hang/dang-nhap', methods=['GET', 'POST'])
def Dang_nhap():
    form = Form_Dang_nhap()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('dang_nhap.html', form = form)
        else:
            Ten_dang_nhap = request.form.get("Th_ten_dang_nhap")
            Mat_khau = request.form.get("Th_mat_khau")
            if Kiem_tra_tai_khoan(Ten_dang_nhap) == True:
                Thong_bao = '<b>Tài khoản không tồn tại</b>'
                return render_template('dang_nhap.html', form = form, Thong_bao = Markup(Thong_bao))
            else:
                Nguoi_dung = Lay_thong_tin_nguoi_dung(Ten_dang_nhap)
                if Mat_khau == Nguoi_dung["mat_khau"]:
                    session["Dang_nhap"] = Nguoi_dung
                    session["Gio_hang"] = []
                    if Nguoi_dung["ma_trang_thai"] == 3:
                        return redirect(url_for("index"))
                    elif Nguoi_dung["ma_trang_thai"] == 4:
                        return redirect(url_for("QL_SP"))
                else:
                    Thong_bao = "<b>Mật khẩu sai! Vui lòng thử lại.</b>"
                    return render_template('dang_nhap.html', form = form, Thong_bao = Markup(Thong_bao))
    
    elif request.method == "GET":
        return render_template('dang_nhap.html', form = form)
    
@app.route('/khach-hang/gui-mail-gop-y', methods=['GET', 'POST'])
def GopY():
    Thong_bao = ''
    form = Form_Gop_y()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('gui_mail_gop_y.html', form = form)
        else:
            ten = request.form.get('Th_Ho_ten')
            email = request.form.get('Th_Email')
            ly_do = request.form.get('Th_Ly_do')
            noi_dung = request.form.get('Th_Gop_y')
            Thong_bao = GuiMailGopY(ten, email, ly_do, noi_dung)
            PhanHoiGopY(ten, email)
            return render_template('gui_mail_gop_y.html', form = form, Thong_bao = Markup(Thong_bao))
    elif request.method == 'GET':
        return render_template('gui_mail_gop_y.html', form = form)

@app.route('/khach-hang/gio-hang', methods=['GET', 'POST'])
def Gio_hang():
    if session.get("Dang_nhap") == None:
        return redirect(url_for("Dang_nhap"))
    else:
        ds = session["Gio_hang"]
        Chuoi_HTML_Gio_hang = Tao_chuoi_HTML_Gio_hang(ds)
        # Xuất hoá đơn
        if request.method == 'POST':
            ma_hoa_don = Dem_hoa_don() + 1
            tong_tien = 0
            ngay_dat = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for sp in ds:
                ChuoiSQL_ct_hoa_don = "INSERT into ct_hoa_don(ma_hoa_don, ma_san_pham, so_luong, don_gia) values(?,?,?,?)"
                if int(sp["don_gia_khuyen_mai"]) != 0:
                    tong_tien += int(sp["don_gia_khuyen_mai"])
                    execute(ChuoiSQL_ct_hoa_don, (ma_hoa_don, sp["ma_san_pham"], sp["so_luong"], sp["don_gia_khuyen_mai"]))
                else:
                    tong_tien += int(sp["don_gia"])
                    execute(ChuoiSQL_ct_hoa_don, (ma_hoa_don, sp["ma_san_pham"], sp["so_luong"], sp["don_gia"]))
            ChuoiSQL_hoa_don = "INSERT into hoa_don(ten_dang_nhap, ngay_dat, tong_tien, hinh_thuc_thanh_toan, ma_trang_thai) values (?, ?, ?, ?, ?)"
            execute(ChuoiSQL_hoa_don, (session["Dang_nhap"]["ten_dang_nhap"], ngay_dat, tong_tien, 'Tiền mặt', 5))
            Phan_hoi_dat_hang(session["Dang_nhap"])
            session["Gio_hang"] = []
            return redirect(url_for('Hoa_don'))
        elif request.method == "GET":
            return render_template('gio_hang.html', Chuoi_HTML_Gio_hang = Markup(Chuoi_HTML_Gio_hang))

@app.route('/khach-hang/hoa-don', methods=['GET', 'POST'])
def Hoa_don():
    ds = Doc_danh_sach_Hoa_don(session["Dang_nhap"]["ten_dang_nhap"])
    if request.method == "POST":
        ma_hoa_don = request.form.get('Ma_hoa_don')
        ChuoiSQL = "UPDATE hoa_don set ma_trang_thai = ? where ma_hoa_don = ?"
        execute(ChuoiSQL, (7, ma_hoa_don))
        ds = Doc_danh_sach_Hoa_don(session["Dang_nhap"]["ten_dang_nhap"])
    Chuoi_HTML_Hoa_don = Tao_chuoi_HTML_Hoa_don(ds)
    return render_template('hoa_don.html', Chuoi_HTML_Hoa_don = Markup(Chuoi_HTML_Hoa_don))

@app.route('/khach-hang', methods=['GET', 'POST'])
def Khach_hang():
    if session.get("Dang_nhap") == None:
        return redirect(url_for("Dang_nhap"))
    else:
        if session["Dang_nhap"]["ma_trang_thai"] == 4:
            return redirect(url_for("QL_SP"))
        else:
            return render_template('khach_hang.html', KH = session["Dang_nhap"])

@app.route('/khach-hang/dang-xuat', methods = ['GET', 'POST'])
def Dang_xuat():
    session.pop("Dang_nhap", None)
    session.pop("Gio_hang", [])
    return redirect(url_for("index"))
    