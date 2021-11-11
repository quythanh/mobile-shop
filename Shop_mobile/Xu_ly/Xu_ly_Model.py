from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask_mysqldb import MySQLdb

Base = declarative_base()

class Hang_san_xuat(Base):
    __tablename__ = 'hang_san_xuat'

    ma_hang_san_xuat =  Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ten_hang_san_xuat = Column(String(250), nullable=False)
    thu_tu = Column(Integer, nullable=False)

class Loai_san_pham(Base):
    __tablename__ = 'loai_san_pham'

    ma_the_loai =  Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ten_loai = Column(String(250), nullable=False)
    mo_ta = Column(String(500))

class San_pham(Base):
    __tablename__ = 'san_pham'

    ma_san_pham = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ma_code = Column(String(50), nullable=False)
    ma_hang_san_xuat = Column(Integer, ForeignKey('hang_san_xuat.ma_hang_san_xuat'))
    ma_the_loai = Column(Integer, ForeignKey('loai_san_pham.ma_the_loai'))
    ten_san_pham = Column(String(250), nullable=False)
    don_gia = Column(Float(10, 0), nullable=False)
    don_gia_khuyen_mai = Column(Float(10, 0), nullable=False)
    mo_ta_tom_tat = Column(String(500), nullable=False)
    mo_ta = Column(Text, nullable=False)
    so_luot_xem = Column(Integer, nullable=False)
    so_luot_dat_mua = Column(Integer, nullable=False)
    ma_trang_thai = Column(Integer, nullable=False)
    ngay_tao = Column(Date, nullable=False)
    ngay_cap_nhat = Column(Date, nullable=False)
    url_video = Column(String(300), nullable=False)

class Nguoi_dung(Base):
    __tablename__ = 'nguoi_dung'

    ten_dang_nhap = Column(String(120), nullable=False, primary_key=True)
    mat_khau = Column(String(50), nullable=False)
    ho_ten = Column(String(120), nullable=False)
    email = Column(String(120))
    dien_thoai = Column(String(12))
    ma_trang_thai = Column(Integer, nullable=False)

class Trang_thai(Base):
    __tablename__ = 'trang_thai'

    ma_trang_thai = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ten_trang_thai = Column(String(250), nullable=False)
    nhom_trang_thai = Column(String(50), nullable=False)

class Khach_hang(Base):
    __tablename__ = 'khach_hang'

    ma_khach_hang = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ten_khach_hang = Column(String(100), nullable=False)
    phai = Column(Integer)
    email = Column(String(50), nullable=False)
    dia_chi = Column(String(100), nullable=False)
    dien_thoai = Column(String(20), nullable=False)
    ghi_chu = Column(String(200), nullable=False)

class Hoa_don(Base):
    __tablename__ = 'hoa_don'

    ma_hoa_don = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ma_khach_hang = Column(Integer, ForeignKey('khach_hang.ma_khach_hang'))
    ngay_dat = Column(Date, nullable=False)
    tong_tien = Column(Float, nullable=False)
    tien_dat_coc = Column(Float, nullable=False)
    con_lai = Column(Float, nullable=False)
    hinh_thuc_thanh_toan = Column(String(100), nullable=False)
    ghi_chu = Column(String(200), nullable=False)

class CT_hoa_don(Base):
    __tablename__ = 'ct_hoa_don'

    ma_hoa_don = Column(Integer, ForeignKey('hoa_don.ma_hoa_don'), primary_key=True)
    ma_san_pham = Column(Integer, ForeignKey('san_pham.ma_san_pham'))
    so_luong = Column(Integer, nullable=False)
    don_gia = Column(Float, nullable=False)

class Hinh_san_pham(Base):
    __tablename__ = 'hinh_san_pham'

    ma_hinh = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ma_san_pham = Column(Integer, ForeignKey('san_pham.ma_san_pham'))
    hinh = Column(String(250), nullable=False)
    thumbnail = Column(Integer, nullable=False)#

class Binh_luan(Base):
    __tablename__ = 'binh_luan'

    ip = Column(String(20), nullable=False, primary_key=True)
    ma_san_pham = Column(Integer, ForeignKey('san_pham.ma_san_pham'))
    ho_ten = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    noi_dung = Column(String(200), nullable=False)
    ngay_dang = Column(Date, nullable=False)
    active = Column(Integer, nullable=False)

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable = False)
    last_name = Column(String(100), nullable = False)
    # ma_loai_nguoi_dung = Column(Integer, ForeignKey('bs_loai_nguoi_dung.ma_loai_nguoi_dung')) 
    # loai_nguoi_dung = relationship(bs_loai_nguoi_dung, backref=('user'))
    login = Column(String(80), unique=True, nullable = False)
    email = Column(String(120))
    password = Column(String(64), nullable = False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.last_name

# sqlite
engine = create_engine('sqlite:///Shop_mobile/Du_lieu/qlsanpham.sqlite?check_same_thread=False')

# # MySQL
# engine = create_engine('mysql://root@localhost/dien_thoai_db')

Base.metadata.create_all(engine)
