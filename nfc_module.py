import board
import busio
import time
from adafruit_pn532.i2c import PN532_I2C


def inicializar_nfc():
    i2c = busio.I2C(board.SCL, board.SDA)
    pn532 = PN532_I2C(i2c, debug=False)

    ic, ver, rev, support = pn532.firmware_version
    print(f"Found PN532 with firmware version: {ver}.{rev}")

    pn532.SAM_configuration()
    return pn532


def leer_uid(timeout=15):
    pn532 = inicializar_nfc()
    print("Esperando tag para escanear...")

    inicio = time.time()

    while time.time() - inicio < timeout:
        uid = pn532.read_passive_target(timeout=0.5)

        if uid is not None:
            uid_str = ''.join(format(i, '02x') for i in uid)
            print("UID:", uid_str)
            return uid_str

    print("No se detectó ningún tag NFC.")
    return None


def construir_url_koha(uid_str):
    return (
        "https://bibliogestion-admin.bue.edu.ar/"
        f"cgi-bin/koha/catalogue/search.pl?q=barcode:{uid_str}"
    )