import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000", back_color="#FF6F61")
    img.save("jubemiGithub.png")
    print('DONE !')


generate_qrcode("https://github.com/Jubemi-Anthony")