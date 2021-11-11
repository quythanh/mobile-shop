from flask import Markup, url_for
import json
import sqlite3
from Shop_mobile.Xu_ly.Xu_ly_Database import *

def Tao_chuoi_HTML_San_pham(danh_sach):
    Chuoi_HTML = '<div class="row">'
    for sp in danh_sach:
        Chuoi_HTML += '<div class="col-md-4">'
        Chuoi_hinh = '<img style="width:380px;height:400px" src="' + url_for('static', filename = 'images/san_pham/' + Lay_url_img(sp["ma_san_pham"])) + '" class="img-responsive" alt="" />'
        Chuoi_HTML_SP = '''
            <p>
                <center>
                    <a href="/san-pham/'''+ str(sp["ma_san_pham"]) + '''" type="button" class="btn btn-info">'''+ sp["ten_san_pham"] +'''</a></br></br>
                    Giá bán: ''' + "{:,}".format(int(sp["don_gia"])).replace(",",".") + ''' đ
                </center>
            </p>
        '''
        Chuoi_HTML += Chuoi_hinh
        Chuoi_HTML += Chuoi_HTML_SP
        Chuoi_HTML += '</div>'
    Chuoi_HTML += '</div>'
    if Chuoi_HTML == '<div class="row"></div>':
        return '<center><h5>Hiện không có hàng</h5></center>'
    else:
        return Chuoi_HTML

def Tao_Chuoi_HTML_Chi_tiet(ma_sp):
    sp = Lay_san_pham_theo_ma(ma_sp)
    Chuoi_HTML = ''
    Chuoi_Ten = '''
    <div class="col-md-12">
        <h2>''' + sp["ten_san_pham"] + '''</h2>
        <hr width="100%" align="left" />
    </div>
    '''
    Chuoi_hinh = '<img src="' + url_for('static', filename = 'images/san_pham/' + Lay_url_img(ma_sp)) + '" class="img-responsive" alt="" /></br>'
    Chuoi_HTML += Chuoi_Ten
    Chuoi_HTML += '<div class="col-md-6">' + Chuoi_hinh + '</div>'
    Chuoi_HTML += '<div class="col-md-6">'
    if sp["mo_ta_tom_tat"] != '':
        Chuoi_HTML += '<b>Mô tả: </b>' + sp["mo_ta_tom_tat"] + '</br>'
    if int(sp["don_gia_khuyen_mai"]) != 0:
        Chuoi_HTML += '<b>Đơn giá: </b>' + "{:,}".format(int(sp["don_gia"])).replace(",",".") + ' đ</br><b>Đơn giá khuyến mãi: </b>' + "{:,}".format(int(sp["don_gia_khuyen_mai"])).replace(",",".") + ' đ</br>'
    else:
        Chuoi_HTML += '<b>Đơn giá: </b>' + "{:,}".format(int(sp["don_gia"])).replace(",",".") + ' đ</br>'
    Chuoi_HTML += '<b>Lượt xem: </b>' + str(sp["so_luot_xem"]) + '</br>'
    Chuoi_HTML += '<b>Lượt đặt mua: </b>' + str(sp["so_luot_dat_mua"]) + '</br>'
    Chuoi_HTML += '<hr width="100%" align="left" /><form method="POST">'
    Chuoi_Dat_mua = '<h4><b>Đặt mua</b></h4></br><b>Số lượng: </b> &nbsp;'
    Chuoi_so_luong_mua = '<input name="Th_So_luong" type="number" required min="1" spellcheck="false" autocomplete="off" value="1"/></br></br>'
    Chuoi_button = '<button type="submit" class="btn btn-warning">Thêm vào giỏ hàng</button>'
    Chuoi_HTML += Chuoi_Dat_mua
    Chuoi_HTML += Chuoi_so_luong_mua
    Chuoi_HTML +=  Chuoi_button +'</form></div>'

    Chuoi_Thong_so = '<div class="col-md-12"><h3>Thông số kỹ thuật</h3></br>' + sp["mo_ta"] + '</div>'
    Chuoi_HTML += Chuoi_Thong_so
    return Chuoi_HTML

def Tao_chuoi_HTML_Dien_thoai():
    dsdt = Doc_danh_sach_Dien_thoai()
    hang_sx = Doc_danh_sach_hang_san_xuat()
    Chuoi_HTML = '<div class="feature">'
    for hsx in hang_sx:
        dsdt_hien_thi = []
        Chuoi_HTML += '<div class="breadcrumbs"><h4>' + hsx["ten_hang_san_xuat"] + '</h4></div><div class="container">'
        for dt in dsdt:
            if dt["ma_hang_san_xuat"] == hsx["ma_hang_san_xuat"]:
                dsdt_hien_thi.append(dt)
        Chuoi_HTML += Tao_chuoi_HTML_San_pham(dsdt_hien_thi) + '</div>'
    Chuoi_HTML += '</div>'
    return Chuoi_HTML

def Tao_chuoi_HTML_Gio_hang(ds):
    if ds == []:
        return '<div class="breadcrumbs"><h4>Giỏ hàng</h4></div><center><h5>Bạn chưa thêm hàng</h5></center>'
    else:
        Chuoi_HTML = '<div class="breadcrumbs"><h4>Giỏ hàng</h4></div><div class="container"><div class="row">'
        Chuoi_tong_cong = 0
        for sp in ds:
            Chuoi_HTML += '<div class="col-md-4">'
            Chuoi_hinh = '<img style="width:190px;height:200px" src="' + url_for('static', filename='images/san_pham/' + Lay_url_img(sp['ma_san_pham'])) + '" class="img-responsive" alt="" />'
            Chuoi_HTML += Chuoi_hinh
            Chuoi_HTML += '</div><div class="col-md-8">'
            if int(sp["don_gia_khuyen_mai"]) == 0:
                Chuoi_don_gia = int(sp["so_luong"]) * int(sp["don_gia"])
            else:
                Chuoi_don_gia = int(sp["so_luong"]) * int(sp["don_gia_khuyen_mai"])
            Chuoi_thong_tin = '<b>Tên sản phẩm: </b>' + sp["ten_san_pham"] + '</br><b>Số lượng mua: </b>' + sp["so_luong"] + '</br><b>Tổng cộng: </b>' + "{:,}".format(Chuoi_don_gia).replace(",",".") + 'đ</br>'
            Chuoi_HTML += Chuoi_thong_tin
            Chuoi_HTML += '</div><hr width="100%" align="left" />'
            Chuoi_tong_cong += Chuoi_don_gia
        Chuoi_HTML += '<hr width="100%" align="left" />'
        Chuoi_HTML += '<form method="POST"><div class="col-md-12" style="font-size:30px"><b>Tổng số tiền phải thanh toán: </b>' + "{:,}".format(Chuoi_tong_cong).replace(",",".") + 'đ <button type="submit">Xuất hoá đơn</button></div></form>'
        Chuoi_HTML += '</div></div>'
        return Chuoi_HTML

def Tao_chuoi_HTML_Hoa_don(ds_hoa_don):
    if ds_hoa_don == []:
        return '<div class="breadcrumbs"><h4>Hoá đơn</h4></div><center><h5>Chưa có hoá đơn</h5></center>'
    else:
        Chuoi_HTML = ''
        for hoa_don in ds_hoa_don:
            Chuoi_HTML += '<div class="breadcrumbs"><h4>Hoá đơn ' + str(ds_hoa_don.index(hoa_don) + 1) + '</h4></div><div class="container"><div class="row">'
            Chuoi_HTML += '<div class="col-md-12">'
            Chuoi_hoa_don = '<b>Ngày đặt: </b>' + hoa_don["ngay_dat"] + '</br><hr width="100%" align="left"/>'
            Chuoi_CT_Hoa_don = ''
            CT_Hoa_don = Lay_CT_Hoa_don(hoa_don["ma_hoa_don"])
            for ct in CT_Hoa_don:
                sp = Lay_san_pham_theo_ma(ct["ma_san_pham"])
                Chuoi_CT_Hoa_don += '<b>Tên sản phẩm: </b>' + sp["ten_san_pham"] + '</br>'
                Chuoi_CT_Hoa_don += '<b>Số lượng: </b>' + str(ct["so_luong"]) + '</br>'
                Chuoi_CT_Hoa_don += '<b>Đơn giá: </b>' + "{:,}".format(int(ct["don_gia"])).replace(",",".") + 'đ</br>'
                Chuoi_CT_Hoa_don += '<hr width="100%" align="left"/>'
            Chuoi_hoa_don += Chuoi_CT_Hoa_don
            Chuoi_hoa_don += '<b>Tổng cộng: </b>' + "{:,}".format(int(hoa_don["tong_tien"])).replace(",",".") + 'đ</br>'
            Chuoi_hoa_don += '<b>Tình trạng hoá đơn: </b>' + Doc_tinh_trang_Hoa_don(hoa_don["ma_trang_thai"])
            if hoa_don["ma_trang_thai"] == 5:
                Chuoi_hoa_don += '<form method="POST"><button class="btn btn-danger" type="submit" name="Ma_hoa_don" value=' + str(hoa_don["ma_hoa_don"]) + '>Huỷ hoá đơn</button></form>'
            Chuoi_HTML += Chuoi_hoa_don
            Chuoi_HTML += '</div></div></div>'
        return Chuoi_HTML

############################## QUẢN LÍ #########################################
def Tao_chuoi_HTML_SP_QL(danh_sach):
    Chuoi_HTML = '<div class="row">'
    for sp in danh_sach:
        Chuoi_HTML += '<div class="col-md-4">'
        Chuoi_hinh = '<img style="width:380px;height:400px" src="' + url_for('static', filename = 'images/san_pham/' + Lay_url_img(sp["ma_san_pham"])) + '" class="img-responsive" alt="" />'
        Chuoi_HTML_SP = '''
            <p>
                <center>
                    <a href="/quan-li/san-pham/'''+ str(sp["ma_san_pham"]) + '''" type="button" class="btn btn-info">'''+ sp["ten_san_pham"] +'''</a></br></br>
                    Giá bán: ''' + "{:,}".format(int(sp["don_gia"])).replace(",",".") + ''' đ
                </center>
            </p>
        '''
        Chuoi_HTML += Chuoi_hinh
        Chuoi_HTML += Chuoi_HTML_SP
        Chuoi_HTML += '</div>'
    Chuoi_HTML += '</div>'
    if Chuoi_HTML == '<div class="row"></div>':
        return '<center><h5>Hiện không có hàng</h5></center>'
    else:
        return Chuoi_HTML

def Tao_Chuoi_HTML_QL_Chi_tiet(ma_sp, Thong_bao):
    sp = Lay_san_pham_theo_ma(ma_sp)
    Chuoi_HTML = ''
    Chuoi_Ten = '''
    <div class="col-md-12">
        <h2>''' + sp["ten_san_pham"] + '''</h2>
        <hr width="100%" align="left" />
    </div>
    '''
    Chuoi_hinh = '<img src="' + url_for('static', filename = 'images/san_pham/' + Lay_url_img(ma_sp)) + '" class="img-responsive" alt="" /></br>'
    Chuoi_HTML += Chuoi_Ten
    Chuoi_HTML += '<div class="col-md-6">' + Chuoi_hinh + '</div>'
    Chuoi_HTML += '<div class="col-md-6">'
    if sp["mo_ta_tom_tat"] != '':
        Chuoi_HTML += '<b>Mô tả: </b>' + sp["mo_ta_tom_tat"] + '</br>'
    if int(sp["don_gia_khuyen_mai"]) != 0:
        Chuoi_HTML += '<b>Đơn giá: </b>' + "{:,}".format(int(sp["don_gia"])).replace(",",".") + ' đ</br><b>Đơn giá khuyến mãi: </b>' + "{:,}".format(int(sp["don_gia_khuyen_mai"])).replace(",",".") + ' đ</br>'
    else:
        Chuoi_HTML += '<b>Đơn giá: </b>' + "{:,}".format(int(sp["don_gia"])).replace(",",".") + ' đ</br>'
    Chuoi_HTML += '<b>Lượt xem: </b>' + str(sp["so_luot_xem"]) + '</br>'
    Chuoi_HTML += '<b>Lượt đặt mua: </b>' + str(sp["so_luot_dat_mua"]) + '</br>'
    Chuoi_HTML += '<hr width="100%" align="left" /><form method="POST">'
    Chuoi_Chinh_sua = '<h4><b>Chỉnh sửa</b></h4></br>'
    Chuoi_Sua_ten = '<b>Tên: </b> &nbsp;<input style="width:100%" name="Th_ten" type="text" spellcheck="false" autocomplete="off"/></br></br>'
    Chuoi_Don_gia = '<b>Đơn giá: </b> &nbsp;<input name="Th_Don_gia" type="number" min="0" spellcheck="false" autocomplete="off" value="0"/></br></br>'
    Chuoi_Don_gia_km = '<b>Đơn giá khuyến mãi: </b> &nbsp;<input name="Th_Don_gia_km" type="number" min="0" spellcheck="false" autocomplete="off" value="0"/></br></br>'
    Chuoi_mo_ta_tom_tat = '<b>Mô tả tóm tắt: </b> &nbsp;<input style="width:100%" name="Th_mttt" type="text" spellcheck="false" autocomplete="off"/></br></br>'
    Chuoi_thong_so = '<b>Thông số kĩ thuật: </b> &nbsp;<input style="width:100%" name="Th_tskt" type="text" spellcheck="false" autocomplete="off"/></br></br>'
    Chuoi_button = '<button type="submit" class="btn btn-warning">Xác nhận</button>'
    Chuoi_Chinh_sua += Chuoi_Sua_ten + Chuoi_Don_gia + Chuoi_Don_gia_km + Chuoi_mo_ta_tom_tat + Chuoi_thong_so
    Chuoi_HTML += Chuoi_Chinh_sua
    Chuoi_HTML +=  Chuoi_button +'</form></br>' + Thong_bao + '</div>'
    Chuoi_Thong_so = '<div class="col-md-12"><h3>Thông số kỹ thuật</h3></br>' + sp["mo_ta"] + '</div>'
    Chuoi_HTML += Chuoi_Thong_so
    return Chuoi_HTML

def Tao_Chuoi_HTML_QL_Hoa_don(ds_hoa_don):
    if ds_hoa_don == []:
        return '<div class="breadcrumbs"><h4>Hoá đơn</h4></div><center><h5>Chưa có hoá đơn</h5></center>'
    else:
        Chuoi_HTML = ''
        for hoa_don in ds_hoa_don:
            Chuoi_HTML += '<div class="breadcrumbs"><h4>Hoá đơn ' + str(ds_hoa_don.index(hoa_don) + 1) + '</h4></div><div class="container"><div class="row">'
            Chuoi_HTML += '<div class="col-md-12">'
            Chuoi_hoa_don = '<b>Ngày đặt: </b>' + hoa_don["ngay_dat"] + '</br>'
            Chuoi_hoa_don+= '<b>Khách hàng: </b>' + Lay_thong_tin_nguoi_dung(hoa_don["ten_dang_nhap"])["ho_ten"] + '</br><hr width="100%" align="left"/>'
            Chuoi_CT_Hoa_don = ''
            CT_Hoa_don = Lay_CT_Hoa_don(hoa_don["ma_hoa_don"])
            for ct in CT_Hoa_don:
                sp = Lay_san_pham_theo_ma(ct["ma_san_pham"])
                Chuoi_CT_Hoa_don += '<b>Tên sản phẩm: </b>' + sp["ten_san_pham"] + '</br>'
                Chuoi_CT_Hoa_don += '<b>Số lượng: </b>' + str(ct["so_luong"]) + '</br>'
                Chuoi_CT_Hoa_don += '<b>Đơn giá: </b>' + "{:,}".format(int(ct["don_gia"])).replace(",",".") + 'đ</br>'
                Chuoi_CT_Hoa_don += '<hr width="100%" align="left"/>'
            Chuoi_hoa_don += Chuoi_CT_Hoa_don
            Chuoi_hoa_don += '<b>Tổng cộng: </b>' + "{:,}".format(int(hoa_don["tong_tien"])).replace(",",".") + 'đ</br>'
            Chuoi_hoa_don += '<b>Tình trạng hoá đơn: </b>' + Doc_tinh_trang_Hoa_don(hoa_don["ma_trang_thai"])
            if hoa_don["ma_trang_thai"] == 5:
                Chuoi_hoa_don += '<form method="POST"><button type="submit" class="btn btn-danger" name="Huy_hoa_don" value=' + str(hoa_don["ma_hoa_don"]) + '>Huỷ hoá đơn</button> &nbsp; <button class="btn btn-success" type="submit" name="Thanh_toan" value=' + str(hoa_don["ma_hoa_don"]) + '>Đã thanh toán</button></form>'
            Chuoi_HTML += Chuoi_hoa_don
            Chuoi_HTML += '</div></div></div>'
        return Chuoi_HTML