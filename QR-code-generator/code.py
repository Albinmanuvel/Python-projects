import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

text = input("Enter the text or URL to generate a QR code: ")
filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")

generate_qr_code(text, filename)