import time
from watchdog.observers import Observer
from cataloguer import ArXivPaperCataloguer
import os
from pathlib import Path


## Daemon responsible for watching for arXiv downloads and triggering the rename/move process
class RenameDaemon:
    def __init__(self, source_dir, target_dir) -> None:
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.observer = Observer()

    def watch(self):
        event_handler = ArXivPaperCataloguer(
            target_dir=self.target_dir, on_duplicate="open"
        )
        self.observer.schedule(event_handler, self.source_dir, recursive=True)
        self.observer.start()
        print(f"Daemon is watching {self.source_dir}")
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped.")

        self.observer.join()


def main():
    if not os.environ.get("DOWNLOADS"):
        source_dir = Path(os.environ.get("USERPROFILE")) / Path("Downloads")
    else:
        source_dir = Path(os.environ.get("DOWNLOADS"))
    if not os.environ.get("PAPERS"):
        target_dir = Path(os.environ.get("USERPROFILE")) / Path("ArXiv/Papers")
    else:
        target_dir = Path(os.environ.get("PAPERS"))
    print(f"source_dir: {source_dir}")
    print(f"target_dir: {target_dir}")
    daemon = RenameDaemon(source_dir=source_dir, target_dir=target_dir)
    daemon.watch()


if __name__ == "__main__":
    main()
