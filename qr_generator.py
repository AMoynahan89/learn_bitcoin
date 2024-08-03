import os
import qrcode


def bit_uri(address, amount=None, label=None, message=None):
    qr_in = f"bitcoin:{address}"
    data = {
        "amount": amount,
        "label": label,
        "message": message
    }

    count = 0
    for key in data:
        if data[key] == None:
            continue
        count += 1

        if count == 1:
            qr_in = qr_in + f"?{key}={data[key]}"
            continue
        elif count > 1:
            qr_in = qr_in + f"&{key}={data[key]}"

    return qr_in


def make_qr(bit_uri):
    # Instantiate QR generator with desired parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Insert URI formatted data
    print(bit_uri)
    qr.add_data(bit_uri)
    qr.make(fit=True)

    # Generate styled qr image
    img = qr.make_image(back_color=(255, 165, 0), fill_color=(41, 39, 39))
    return img


def save_qr(qr_img, img_name):
    # Get current directory and assign path to "file"
    my_dir = os.getcwd()
    path = f"{my_dir}/static/images/{img_name}.png"
    qr_img.save(path)






"""
URI format
bitcoin:<address>[?amount=<amount>][?label=<label>][?message=<message>]
bitcoin:175tWpb8K1S7NmH4Zx6rewF9WQrcZv245W?amount=50&label=Luke-Jr&message=Donation%20for%20project%20xyz
"""
