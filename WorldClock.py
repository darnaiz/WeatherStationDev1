import network
import urequests

class WorldClock:
    url = "https://webelectronica.com.ar/utils/getdt.php"
    dateTime = [1900,1,1,0,0,0,0,0]
    net = ""
    pwd = ""

    def __init__(self, SSID, PASSWORD):
        net = SSID
        pwd = PASSWORD

    def getDateTime(self):
        _sta_if = network.WLAN(network.STA_IF)     # instancia el objeto -sta_if- para controlar la interfaz STA
        if not _sta_if.isconnected():              # si no existe conexión...
            _sta_if.active(True)                       # activa el interfaz STA del ESP32
            _sta_if.connect(SSID, PASSWORD)            # inicia la conexión con el AP
            print("Conectando a la red", SSID +"...")
            while not _sta_if.isconnected():           # ...si no se ha establecido la conexión...
                pass                                  # ...repite el bucle...
        print("WC: Configuración de red (IP/netmask/gw/DNS):", _sta_if.ifconfig())
        print("WC: Recuperando información...")
        
        _resp = urequests.get(self.url)
        print(_resp.status_code)
        print(_resp.text)
        if (_resp.status_code == 200):
            dateTime = _resp.text
        _sta_if.disconnect()
        _sta_if.active(False)
        
