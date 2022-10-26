# Share wifi name e password as QR code
# by Busyman.Inc

# pip install wifi_qrcode_generator

import wifi_qrcode_generator as qr

qr.wifi_qrcode('wifiName', False, 'WPA', 'Password')
