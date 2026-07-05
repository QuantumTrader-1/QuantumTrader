import threading
import time

from core.config import SCANNER_INTERVAL


class ScannerService:

    def __init__(self, engine, callback):

        self.engine = engine
        self.callback = callback

        self.running = False
        self.thread = None

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.run,
            daemon=True,
        )

        self.thread.start()

    def stop(self):

        self.running = False

    def run(self):

        while self.running:

            self.engine.scan_market()

            self.callback()

            time.sleep(SCANNER_INTERVAL)