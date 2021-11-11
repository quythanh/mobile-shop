import json
import sqlite3

Thu_muc_Du_lieu = "Shop_mobile/Du_lieu/qlsanpham.sqlite"

######################## XỬ LÝ DATABASE ########################
#################### INSERT, UPDATE, DELETE ####################

def execute(chuoiSQL, btdk=()):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    cursor=conn.execute(chuoiSQL, btdk)
    conn.commit()
    conn.close()
    return cursor.rowcount

######################## ĐỌC DỮ LIỆU ########################

def Chuyen_du_lieu_json(cursor):
    list_sp = []
    for sp in cursor:
        sp_dict = {}
        sp_dict["ma_san_pham"] = sp[0]
        sp_dict["ma_code"] = sp[1]
        sp_dict["ma_hang_san_xuat"] = sp[2]
        sp_dict["ma_the_loai"] = sp[3]
        sp_dict["ten_san_pham"] = sp[4]
        sp_dict["don_gia"] = sp[5]
        sp_dict["don_gia_khuyen_mai"] = sp[6]
        sp_dict["mo_ta_tom_tat"] = sp[7]
        sp_dict["mo_ta"] = sp[8]
        sp_dict["so_luot_xem"] = sp[9]
        sp_dict["so_luot_dat_mua"] = sp[10]
        sp_dict["ma_trang_thai"] = sp[11]
        sp_dict["ngay_tao"] = sp[12]
        sp_dict["ngay_cap_nhat"] = sp[13]
        list_sp.append(sp_dict)
    return list_sp

def Doc_danh_sach(Chuoi_SQL):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    cursor = conn.execute(Chuoi_SQL)
    list_sp = Chuyen_du_lieu_json(cursor)
    conn.commit()
    conn.close()
    return list_sp

def Doc_danh_sach_sp():
    Chuoi_SQL = "SELECT * from san_pham"
    list_sp = Doc_danh_sach(Chuoi_SQL)
    return list_sp

def Doc_danh_sach_ipad():
    Chuoi_SQL = "SELECT * from san_pham where ma_the_loai = 2 and ma_hang_san_xuat = 7"
    list_ipad = Doc_danh_sach(Chuoi_SQL)
    return list_ipad

def Doc_danh_sach_tablet_samsung():
    Chuoi_SQL = "SELECT * from san_pham where ma_the_loai = 2 and ma_hang_san_xuat = 2"
    list_ss = Doc_danh_sach(Chuoi_SQL)
    return list_ss

def Doc_danh_sach_tablet_khac():
    Chuoi_SQL = "SELECT * from san_pham where ma_the_loai = 2 and ma_hang_san_xuat not in (2, 7)"
    list_tablet = Doc_danh_sach(Chuoi_SQL)
    return list_tablet

def Doc_danh_sach_Cap_sac():
    Chuoi_SQL = "SELECT * from san_pham where ma_the_loai = 3"
    list_cap_sac = Doc_danh_sach(Chuoi_SQL)
    return list_cap_sac

def Doc_danh_sach_Op_lung():
    Chuoi_SQL = "SELECT * from san_pham where ma_the_loai = 4"
    list_op = Doc_danh_sach(Chuoi_SQL)
    return list_op

def Doc_danh_sach_Tai_nghe():
    Chuoi_SQL = "SELECT * from san_pham where ma_the_loai = 5"
    list_Tai_nghe = Doc_danh_sach(Chuoi_SQL)
    return list_Tai_nghe

def Doc_danh_sach_Phu_kien_khac():
    Chuoi_SQL = "SELECT * from san_pham where ma_the_loai = 6"
    list_pk = Doc_danh_sach(Chuoi_SQL)
    return list_pk

def Doc_danh_sach_Xem_nhieu_nhat():
    Chuoi_SQL = "SELECT * FROM san_pham ORDER BY so_luot_xem DESC LIMIT 5"
    lst = Doc_danh_sach(Chuoi_SQL)
    return lst

def Doc_danh_sach_Mua_nhieu_nhat():
    Chuoi_SQL = "SELECT * FROM san_pham ORDER BY so_luot_dat_mua DESC LIMIT 5"
    lst = Doc_danh_sach(Chuoi_SQL)
    return lst

def Doc_danh_sach_Moi_cap_nhat():
    Chuoi_SQL = "SELECT * FROM san_pham ORDER BY ngay_cap_nhat DESC LIMIT 5"
    lst = Doc_danh_sach(Chuoi_SQL)
    return lst

def Doc_danh_sach_Dien_thoai():
    Chuoi_SQL = "SELECT * FROM san_pham WHERE ma_the_loai = 1 ORDER BY ma_hang_san_xuat"
    lst = Doc_danh_sach(Chuoi_SQL)
    return lst

def Doc_danh_sach_hang_san_xuat():
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    cursor = conn.execute("SELECT * from hang_san_xuat")
    lst = []
    for hsx in cursor:
        hsx_dict = {}
        hsx_dict["ma_hang_san_xuat"] = hsx[0]
        hsx_dict["ten_hang_san_xuat"] = hsx[1]
        lst.append(hsx_dict)
    return lst

def Doc_danh_sach_Hoa_don(ten_dang_nhap):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from hoa_don where ten_dang_nhap ="
    ChuoiSQL += "'" + str(ten_dang_nhap) + "'" 
    cursor = conn.execute(ChuoiSQL)
    lst = []
    for hoa_don in cursor:
        hd_dict = {}
        hd_dict["ma_hoa_don"] = hoa_don[0]
        hd_dict["ten_dang_nhap"] = hoa_don[1]
        hd_dict["ngay_dat"] = hoa_don[2]
        hd_dict["tong_tien"] = hoa_don[3]
        hd_dict["hinh_thuc_thanh_toan"] = hoa_don[4]
        hd_dict["ma_trang_thai"] = hoa_don[5]
        lst.append(hd_dict)
    conn.commit()
    conn.close()
    return lst

def Doc_danh_sach_Hoa_don_Thanh_toan():
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from hoa_don where ma_trang_thai = 6"
    cursor = conn.execute(ChuoiSQL)
    lst = []
    for hoa_don in cursor:
        hd_dict = {}
        hd_dict["ma_hoa_don"] = hoa_don[0]
        hd_dict["ten_dang_nhap"] = hoa_don[1]
        hd_dict["ngay_dat"] = hoa_don[2]
        hd_dict["tong_tien"] = hoa_don[3]
        hd_dict["hinh_thuc_thanh_toan"] = hoa_don[4]
        hd_dict["ma_trang_thai"] = hoa_don[5]
        lst.append(hd_dict)
    conn.commit()
    conn.close()
    return lst

def Doc_danh_sach_Hoa_don_chua_Thanh_toan():
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from hoa_don where ma_trang_thai = 5"
    cursor = conn.execute(ChuoiSQL)
    lst = []
    for hoa_don in cursor:
        hd_dict = {}
        hd_dict["ma_hoa_don"] = hoa_don[0]
        hd_dict["ten_dang_nhap"] = hoa_don[1]
        hd_dict["ngay_dat"] = hoa_don[2]
        hd_dict["tong_tien"] = hoa_don[3]
        hd_dict["hinh_thuc_thanh_toan"] = hoa_don[4]
        hd_dict["ma_trang_thai"] = hoa_don[5]
        lst.append(hd_dict)
    conn.commit()
    conn.close()
    return lst

def Doc_danh_sach_Hoa_don_Huy():
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from hoa_don where ma_trang_thai = 7"
    cursor = conn.execute(ChuoiSQL)
    lst = []
    for hoa_don in cursor:
        hd_dict = {}
        hd_dict["ma_hoa_don"] = hoa_don[0]
        hd_dict["ten_dang_nhap"] = hoa_don[1]
        hd_dict["ngay_dat"] = hoa_don[2]
        hd_dict["tong_tien"] = hoa_don[3]
        hd_dict["hinh_thuc_thanh_toan"] = hoa_don[4]
        hd_dict["ma_trang_thai"] = hoa_don[5]
        lst.append(hd_dict)
    conn.commit()
    conn.close()
    return lst

######################## LẤY THÔNG TIN ########################

def Lay_url_img(ma_sp):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT hinh from hinh_san_pham where ma_san_pham =" + str(ma_sp)
    cursor = conn.execute(ChuoiSQL)
    hinh = cursor.fetchone()
    conn.commit()
    conn.close()
    return hinh[0]

def Lay_san_pham_theo_ma(ma_sp):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from san_pham where ma_san_pham ="
    ChuoiSQL += str(ma_sp)
    cursor = conn.execute(ChuoiSQL)
    sp_dict = Chuyen_du_lieu_json(cursor)
    conn.commit()
    conn.close()
    return sp_dict[0]

def Tim_kiem(Chuoi_tim_kiem):
    ChuoiSQL = "SELECT * from san_pham where ten_san_pham like"
    ChuoiSQL += "'%" + Chuoi_tim_kiem + "%'"
    lst = Doc_danh_sach(ChuoiSQL)
    return lst

def Kiem_tra_tai_khoan(Ten_dang_nhap):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from nguoi_dung where ten_dang_nhap = "
    ChuoiSQL += "'" + str(Ten_dang_nhap) + "'"
    cursor = conn.execute(ChuoiSQL)
    lst = []
    for item in cursor:
        lst.append(item)
    conn.commit()
    conn.close()
    if len(lst) == 1:
        return False # Tài khoản đã tồn tại
    else:
        return True # Tài khoản không tồn tại

def Lay_thong_tin_nguoi_dung(ten_dang_nhap):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from nguoi_dung where ten_dang_nhap = "
    ChuoiSQL += "'" + str(ten_dang_nhap) + "'"
    cursor = conn.execute(ChuoiSQL)
    lst = []
    for Khach_hang in cursor:
        Khach_hang_dict = {}
        Khach_hang_dict["ho_ten"] = Khach_hang[0]
        Khach_hang_dict["ten_dang_nhap"] = Khach_hang[1]
        Khach_hang_dict["mat_khau"] = Khach_hang[2]
        Khach_hang_dict["gioi_tinh"] = Khach_hang[3]
        Khach_hang_dict["ngay_sinh"] = Khach_hang[4]
        Khach_hang_dict["dia_chi"] = Khach_hang[5]
        Khach_hang_dict["dien_thoai"] = Khach_hang[6]
        Khach_hang_dict["email"] = Khach_hang[7]
        Khach_hang_dict["ma_trang_thai"] = Khach_hang[8]
        lst.append(Khach_hang_dict)
    conn.commit()
    conn.close()
    return lst[0]

def Lay_CT_Hoa_don(ma_hoa_don):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from ct_hoa_don where ma_hoa_don = " + str(ma_hoa_don)
    cursor = conn.execute(ChuoiSQL)
    lst = []
    for ct in cursor:
        ct_dict = {}
        ct_dict["ma_hoa_don"] = ct[0]
        ct_dict["ma_san_pham"] = ct[1]
        ct_dict["so_luong"] = ct[2]
        ct_dict["don_gia"] = ct[3]
        lst.append(ct_dict)
    conn.commit()
    conn.close()
    return lst

def Doc_tinh_trang_Hoa_don(ma_trang_thai):
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT ten_trang_thai from trang_thai where ma_trang_thai = " + str(ma_trang_thai)
    cursor = conn.execute(ChuoiSQL)
    tt = ''
    for trang_thai in cursor:
        tt = trang_thai[0]
    conn.commit()
    conn.close()    
    return tt

def Dem_hoa_don():
    conn = sqlite3.connect(Thu_muc_Du_lieu)
    ChuoiSQL = "SELECT * from hoa_don"
    cursor = conn.execute(ChuoiSQL)
    dong = []
    for item in cursor:
        dong.append(item[0])
    return max(dong)