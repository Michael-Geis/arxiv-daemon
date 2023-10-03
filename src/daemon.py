import time
from watchdog.observers import Observer
from cataloguer import ArXivPaperCataloguer
import config

SOURCE_DIR = config.SOURCE_DIR
TARGET_DIR = config.TARGET_DIR


## Daemon responsible for watching for arXiv downloads and triggering the rename/move process
class RenameDaemon:
    def __init__(self, source_dir=SOURCE_DIR) -> None:
        self.source_dir = source_dir
        self.observer = Observer()

    def watch(self):
        event_handler = ArXivPaperCataloguer(target_dir=TARGET_DIR)
        self.observer.schedule(event_handler, self.source_dir, recursive=True)
        self.observer.start()
        print("Daemon is watching...")
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped.")

        self.observer.join()


def main():
    daemon = RenameDaemon()
    daemon.watch()


if __name__ == "__main__":
    main()
