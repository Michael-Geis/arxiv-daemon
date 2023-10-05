import time
from watchdog.observers import Observer
from cataloguer import ArXivPaperCataloguer
from ui import search_for_file_path
import config


## Daemon responsible for watching for arXiv downloads and triggering the rename/move process
class RenameDaemon:
    def __init__(self, source_dir, target_dir) -> None:
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.observer = Observer()

    def watch(self):
        event_handler = ArXivPaperCataloguer(target_dir=self.target_dir)
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
    # # Make sure we have set directories
    if config.SET_DIRS_AT_RUNTIME:
        source_dir = search_for_file_path(prompt="Select your downloads directory.")
        target_dir = search_for_file_path(
            prompt="Select the directory you want to save your papers in."
        )
    else:
        source_dir = config.SOURCE_DIR
        target_dir = config.TARGET_DIR
    daemon = RenameDaemon(source_dir=source_dir, target_dir=target_dir)
    daemon.watch()


if __name__ == "__main__":
    main()
