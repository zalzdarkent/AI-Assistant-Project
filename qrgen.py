import qrcode
import datetime
import os

def makeQRCode(input_data: str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Membuat nama file berdasarkan timestamp saat ini
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"qr_{current_time}.png"
    file_path = os.path.join("./assets/img/qr-code", file_name)

    img.save(file_path)
    print(f"QR code saved as {file_path}")
