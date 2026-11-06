"""Convierte un link o cualquier texto en un código QR (PNG).

Uso:
    python generar_qr.py                      -> pide el link/texto por consola
    python generar_qr.py https://ejemplo.com  -> genera qr.png
    python generar_qr.py Hola, esto es un texto -o mi_qr.png

Requiere: pip install "qrcode[pil]"
"""
import argparse
import sys

try:
    import qrcode
except ImportError:
    sys.exit('Falta la librería. Instálala con:  pip install "qrcode[pil]"')


def generar_qr(link: str, salida: str = "qr.png") -> str:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(salida)
    return salida


def main():
    parser = argparse.ArgumentParser(description="Convierte un link o texto en un QR")
    parser.add_argument("contenido", nargs="*", help="Link o texto a convertir")
    parser.add_argument("-o", "--output", default="qr.png", help="Archivo de salida (default: qr.png)")
    args = parser.parse_args()

    contenido = " ".join(args.contenido) or input("Pega el link o texto: ").strip()
    if not contenido:
        sys.exit("No ingresaste nada.")

    archivo = generar_qr(contenido, args.output)
    print(f"QR generado: {archivo}")


if __name__ == "__main__":
    main()
