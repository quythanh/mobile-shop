from flask import render_template, request, Markup, session, redirect
from Shop_mobile import app
from Shop_mobile.Xu_ly.Xu_ly_Database import *
from Shop_mobile.Xu_ly.Tao_chuoi_HTML import *
from Shop_mobile.app_khach_hang import *

@app.route('/quan-li/san-pham', methods=["POST", "GET"])
def QL_SP():
    Chuoi_tim_kiem = ''
    danh_sach = Doc_danh_sach_sp()
    Chuoi_HTML_San_pham = Tao_chuoi_HTML_SP_QL(danh_sach)
    Chuoi_HTML_San_pham_xem = Chuoi_HTML_San_pham
    if request.form.get("Th_Chuoi_Tim_kiem") != None:
        Chuoi_tim_kiem = request.form.get("Th_Chuoi_Tim_kiem")
        lst_tim_kiem = Tim_kiem(Chuoi_tim_kiem)
        Chuoi_HTML_San_pham_xem = Tao_chuoi_HTML_SP_QL(lst_tim_kiem)
    return render_template('quan_li/quan_li_san_pham.html', Chuoi_HTML_San_pham = Markup(Chuoi_HTML_San_pham_xem))

@app.route('/quan-li/san-pham/<int:ma_sp>/', methods=['GET', 'POST'])
def QL_Chinh_sua_SP(ma_sp):
    sp = Lay_san_pham_theo_ma(ma_sp)
    Thong_bao = ''
    if request.form.get("Th_ten") != None:
        ten = request.form.get("Th_ten")
        if ten != '':
            ChuoiSQL_ten = "UPDATE san_pham set ten_san_pham = ? where ma_san_pham = ?"
            execute(ChuoiSQL_ten, (ten, ma_sp))
            Thong_bao = 'Đã cập nhật'
    if request.form.get("Th_mttt") != None:
        mttt = request.form.get("Th_mttt")
        if mttt != '':
            ChuoiSQL_mttt = "UPDATE san_pham set mo_ta_tom_tat = ? where ma_san_pham = ?"
            execute(ChuoiSQL_mttt, (mttt, ma_sp))
            Thong_bao = 'Đã cập nhật'
    if request.form.get("Th_tskt") != None:
        tskt = request.form.get("Th_tskt")
        if tskt != '':
            ChuoiSQL_tskt = "UPDATE san_pham set mo_ta = ? where ma_san_pham = ?"
            execute(ChuoiSQL_tskt, (tskt, ma_sp))
            Thong_bao = 'Đã cập nhật'
    if request.form.get("Th_Don_gia") != None:
        don_gia = request.form.get("Th_Don_gia")
        if int(don_gia) > 0:
            ChuoiSQL_don_gia = "UPDATE san_pham set don_gia = ? where ma_san_pham = ?"
            execute(ChuoiSQL_don_gia, (don_gia, ma_sp))
            Thong_bao = 'Đã cập nhật'
    if request.form.get("Th_Don_gia_km") != None:
        don_gia_km = request.form.get("Th_Don_gia_km")
        ChuoiSQL_don_gia_km = "UPDATE san_pham set don_gia_khuyen_mai = ? where ma_san_pham = ?"
        execute(ChuoiSQL_don_gia_km, (don_gia_km, ma_sp))
        Thong_bao = 'Đã cập nhật'
    Chuoi_HTML_Chi_tiet = Tao_Chuoi_HTML_QL_Chi_tiet(ma_sp, Thong_bao)
    return render_template('quan_li/chinh_sua_san_pham.html', Chuoi_HTML_Chi_tiet = Markup(Chuoi_HTML_Chi_tiet))

@app.route('/quan-li-hoa-don/da-thanh-toan', methods=['GET', 'POST'])
def HDTT():
    danh_sach = Doc_danh_sach_Hoa_don_Thanh_toan()
    Chuoi_HTML_Hoa_don = Tao_Chuoi_HTML_QL_Hoa_don(danh_sach)
    return render_template('quan_li/hoa_don.html', Chuoi_HTML_Hoa_don = Markup(Chuoi_HTML_Hoa_don))

@app.route('/quan-li-hoa-don/chua-thanh-toan', methods=['GET', 'POST'])
def HDCTT():
    danh_sach = Doc_danh_sach_Hoa_don_chua_Thanh_toan()
    if request.form.get('Huy_hoa_don') != None:
        ma_hoa_don = request.form.get('Huy_hoa_don')
        ChuoiSQL = "UPDATE hoa_don set ma_trang_thai = ? where ma_hoa_don = ?"
        execute(ChuoiSQL, (7, ma_hoa_don))
        danh_sach = Doc_danh_sach_Hoa_don_chua_Thanh_toan()
    if request.form.get('Thanh_toan') != None:
        ma_hoa_don = request.form.get('Thanh_toan')
        ChuoiSQL = "UPDATE hoa_don set ma_trang_thai = ? where ma_hoa_don = ?"
        execute(ChuoiSQL, (6, ma_hoa_don))
        danh_sach = Doc_danh_sach_Hoa_don_chua_Thanh_toan()
    Chuoi_HTML_Hoa_don = Tao_Chuoi_HTML_QL_Hoa_don(danh_sach)
    return render_template('quan_li/hoa_don.html', Chuoi_HTML_Hoa_don = Markup(Chuoi_HTML_Hoa_don))

@app.route('/quan-li-hoa-don/da-huy', methods=['GET', 'POST'])
def HDH():
    danh_sach = Doc_danh_sach_Hoa_don_Huy()
    Chuoi_HTML_Hoa_don = Tao_Chuoi_HTML_QL_Hoa_don(danh_sach)
    return render_template('quan_li/hoa_don.html', Chuoi_HTML_Hoa_don = Markup(Chuoi_HTML_Hoa_don))