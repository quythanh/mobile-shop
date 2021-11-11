from flask import render_template, request, redirect, session
from Shop_mobile import app
from Shop_mobile.Xu_ly.Tao_chuoi_HTML import *
from Shop_mobile.Xu_ly.Xu_ly_Database import *
from Shop_mobile.app_khach_hang import *

@app.route('/', methods=['GET', 'POST'])
def index():
    # Đọc dữ liệu
    danh_sach_xem_nn = Doc_danh_sach_Xem_nhieu_nhat()
    danh_sach_mua_nn = Doc_danh_sach_Mua_nhieu_nhat()
    danh_sach_moi_cap_nhat = Doc_danh_sach_Moi_cap_nhat()

    # Tạo chuỗi HTML
    Chuoi_HTML_Xem_NN = Tao_chuoi_HTML_San_pham(danh_sach_xem_nn)
    Chuoi_HTML_Mua_NN = Tao_chuoi_HTML_San_pham(danh_sach_mua_nn)
    Chuoi_HTML_Moi = Tao_chuoi_HTML_San_pham(danh_sach_moi_cap_nhat)

    return render_template('trang_chu.html', Chuoi_HTML_Xem_NN = Markup(Chuoi_HTML_Xem_NN), Chuoi_HTML_Mua_NN = Markup(Chuoi_HTML_Mua_NN), Chuoi_HTML_Moi = Markup(Chuoi_HTML_Moi))

@app.route('/san-pham', methods=['GET', 'POST'])
def San_Pham():
    Chuoi_tim_kiem = ''
    danh_sach = Doc_danh_sach_sp()
    Chuoi_HTML_San_pham = Tao_chuoi_HTML_San_pham(danh_sach)
    Chuoi_HTML_San_pham_xem = Chuoi_HTML_San_pham
    if request.form.get("Th_Chuoi_Tim_kiem") != None:
        Chuoi_tim_kiem = request.form.get("Th_Chuoi_Tim_kiem")
        lst_tim_kiem = Tim_kiem(Chuoi_tim_kiem)
        Chuoi_HTML_San_pham_xem = Tao_chuoi_HTML_San_pham(lst_tim_kiem)
    return render_template('tat_ca_san_pham.html', Chuoi_HTML_San_pham = Markup(Chuoi_HTML_San_pham_xem))

@app.route('/san-pham/<int:ma_sp>/', methods=['GET', 'POST'])
def Chi_tiet(ma_sp):
    sp = Lay_san_pham_theo_ma(ma_sp)
    Chuoi_SQL_luot_xem = "UPDATE san_pham set so_luot_xem = ? where ma_san_pham = ?"
    execute(Chuoi_SQL_luot_xem, (sp["so_luot_xem"] + 1, ma_sp))
    if request.method == "POST":
        if session.get("Dang_nhap") == None:
            return redirect(url_for('Dang_nhap'))
        else:
            Chuoi_SQL_luot_mua = "UPDATE san_pham set so_luot_dat_mua = ? where ma_san_pham = ?"
            execute(Chuoi_SQL_luot_mua, (sp["so_luot_dat_mua"] + 1, ma_sp))
            sp["so_luong"] = request.form.get("Th_So_luong")
            session["Gio_hang"].append(sp)
    Chuoi_HTML_Chi_tiet = Tao_Chuoi_HTML_Chi_tiet(ma_sp)
    return render_template('chi_tiet.html', Chuoi_HTML_Chi_tiet = Markup(Chuoi_HTML_Chi_tiet))

@app.route('/phone', methods=['GET', 'POST'])
def Phone():
    Chuoi_HTML_Dien_thoai = Tao_chuoi_HTML_Dien_thoai()
    return render_template('phone.html', Chuoi_HTML_Dien_thoai = Markup(Chuoi_HTML_Dien_thoai))

@app.route('/tablet', methods=['GET', 'POST'])
def Tablet():
    # Đọc dữ liệu
    danh_sach_ipad = Doc_danh_sach_ipad()
    danh_sach_tablet_samsung = Doc_danh_sach_tablet_samsung()
    danh_sach_tablet_khac = Doc_danh_sach_tablet_khac()

    # Tạo chuỗi HTML
    Chuoi_HTML_iPad = Tao_chuoi_HTML_San_pham(danh_sach_ipad)
    Chuoi_HTML_Samsung = Tao_chuoi_HTML_San_pham(danh_sach_tablet_samsung)
    Chuoi_HTML_Tablet_Khac = Tao_chuoi_HTML_San_pham(danh_sach_tablet_khac)
    
    return render_template('tablet.html', Chuoi_HTML_iPad = Markup(Chuoi_HTML_iPad), Chuoi_HTML_Samsung = Markup(Chuoi_HTML_Samsung), Chuoi_HTML_Tablet_Khac = Markup(Chuoi_HTML_Tablet_Khac))

@app.route('/phu-kien', methods=['GET', 'POST'])
def Phu_kien():
    # Đọc dữ liệu
    DS_Cap_sac = Doc_danh_sach_Cap_sac()
    DS_Op = Doc_danh_sach_Op_lung()
    DS_Tai_nghe = Doc_danh_sach_Tai_nghe()
    DS_PK_Khac = Doc_danh_sach_Phu_kien_khac()

    # Tạo chuỗi HTML
    Chuoi_HTML_Sac_cap = Tao_chuoi_HTML_San_pham(DS_Cap_sac)
    Chuoi_HTML_Op = Tao_chuoi_HTML_San_pham(DS_Op)
    Chuoi_HTML_Tai_nghe = Tao_chuoi_HTML_San_pham(DS_Tai_nghe)
    Chuoi_HTML_Khac = Tao_chuoi_HTML_San_pham(DS_PK_Khac)

    return render_template('phu_kien.html', Chuoi_HTML_Sac_cap = Markup(Chuoi_HTML_Sac_cap), Chuoi_HTML_Op = Markup(Chuoi_HTML_Op), Chuoi_HTML_Tai_nghe = Markup(Chuoi_HTML_Tai_nghe), Chuoi_HTML_Khac = Markup(Chuoi_HTML_Khac))