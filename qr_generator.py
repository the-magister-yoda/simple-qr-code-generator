import argparse
import qrcode


def generate_qr_code(data, filename="qr_code.png", size=10, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

def main():
    parser = argparse.ArgumentParser(
        description="Генератор QR-кодов из текста или ссылки"
    )

    parser.add_argument("data", help="Текст или ссылка, которые нужно закодировать")
    parser.add_argument(
        "-o", "--output", default="qr_code.png",
        help="Имя выходного файла по умолчанию (qr_code.png)"
    )
    parser.add_argument(
        "-s", "--size", type=int, default=10,
        help="Размер ячеек QR кода"
    )
    parser.add_argument(
        "-b", "--border", type=int, default=4,
        help="Толщина границы QR кода"
    )

    args = parser.parse_args()

    saved_file = generate_qr_code(args.data, args.output, args.size, args.border)
    print(f"QR-код успешно создан и сохранён как {saved_file}")

if __name__ == "__main__":
    main()