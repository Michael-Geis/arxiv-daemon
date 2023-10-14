import arxiv
import time
from watchdog.events import FileSystemEventHandler
import regex
from pathlib import Path
from namelogic import format_file_name
from duplicatehandler import DuplicateHandler


## Event handler class which recieves any 'FileCreated' event in config.SOURCE_DIR
class ArXivPaperCataloguer(FileSystemEventHandler):
    def __init__(self, target_dir, on_duplicate):
        super().__init__()
        self.target_dir = target_dir
        self.duplicate_handler = DuplicateHandler(on_duplicate)

    def on_created(self, event):
        """Processed triggered by a new file appearing in SOURCE_DIR.

        Args:
            event: watchdog.events.FileCreated object representing a new file in config.SOURCE_DIR.

        Returns:
            None if the file name does not match one of two possible regex expressions for arXiv
            id numbers. If the file name does match an arXiv id, the function queries the arxiv API
            for the paper metadata based on this id, creates the new file name and moves it to
            the config.TARGET_DIR.
        """
        time.sleep(1)
        if event.is_directory:
            return None

        path = Path(event.src_path)
        id = self.is_arxiv(
            path
        )  ## Checks if new file is an arXiv paper, if so returns its id

        if not id:
            return None
        else:
            new_name = self.get_file_name(
                id
            )  ## Retrieves metadata and formats new filename
            new_path = Path(self.target_dir) / Path(new_name)
            try:
                path.rename(new_path)
            except FileExistsError:
                self.duplicate_handler.handle_duplicate(path=path, new_path=new_path)

    def is_arxiv(self, path):
        """Determines if a path represents a downloaded pdf of an arXiv paper.

        Args:
            path: pathlib Path object representing the path of the file to be evaluated.

        Returns:
            str: The unique arXiv id number of the paper if the file is an arXiv download. If not, returns None.
        """
        file_name = str(path.stem)
        pattern = r"\d{4}\.\d{4,5}"
        if regex.match(pattern, file_name):
            return file_name

    def get_file_name(self, id):
        """Returns formatted filename based on arXiv id.

        Args:
            id: arXiv id number.

        Returns:
            file name in the form name.pdf where 'name' is a string determined by the paper metadata (see self.format_file_name).
        """
        search = arxiv.Search(id_list=[id])
        result = next(search.results())

        title = result.title
        authors = [author.name for author in result.authors]

        return format_file_name(title, authors)
