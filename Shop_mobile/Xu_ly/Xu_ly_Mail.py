from Shop_mobile import app
from flask_mail import Mail, Message
from datetime import datetime

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testmailpython513@gmail.com'
app.config['MAIL_PASSWORD'] = 'T_H*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def GuiMailGopY(ten, email_nguoi_gui, ly_do, noi_dung):
    msg = Message('Góp Ý', sender = 'testmailpython513@gmail.com', recipients = ['quythanh.33.91@gmail.com'])
    Noi_dung_mail = 'Họ tên: <b>' + ten + '</b>'
    Noi_dung_mail += '</br>Email: <b>' + email_nguoi_gui + '</b>'
    Noi_dung_mail += '</br>Lý do: <b>' + ly_do + '</b>'
    Noi_dung_mail += '</br>Nội dung: ' + noi_dung
    mail.body = Noi_dung_mail
    msg.html = mail.body
    mail.send(msg)
    Thong_bao = '<h3>Đã gửi</h3>'
    return Thong_bao

def PhanHoiGopY(ten, email):
    msg = Message('Phản hồi góp ý', sender = 'testmailpython513@gmail.com', recipients = [email])
    Noi_dung_mail = 'Shop Mobile xin chân thành cảm ơn góp ý của <b>' + ten + '</b>.<br>Chúng tôi sẽ luôn cố gắng hết mình để quý khách hàng có thể cảm thấy hài lòng nhất có thể.'
    mail.body = Noi_dung_mail
    msg.html = mail.body
    mail.send(msg)

def Phan_hoi_dat_hang(khach_hang):
    thoi_gian = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = Message('Test mail', sender = 'testmailpython513@gmail.com', recipients = [khach_hang["email"]])
    Noi_dung_mail = 'Kính chào '+ khach_hang["ho_ten"] + ',<br>Chúng tôi đã nhận đơn hàng đặt của bạn lúc ' + thoi_gian
    Noi_dung_mail += '<br>Chúng tôi sẽ giao hàng trong 24h.<br>Chân thành cảm ơn quý khách. Chúc quý khách một ngày tốt lành.'
    mail.body = Noi_dung_mail
    msg.html = mail.body
    mail.send(msg)
    
