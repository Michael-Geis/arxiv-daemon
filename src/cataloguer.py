import arxiv
from watchdog.events import FileSystemEventHandler
import regex
from pathlib import Path
from cleantext import clean


## Event handler class which recieves any 'FileCreated' event in config.SOURCE_DIR
class ArXivPaperCataloguer(FileSystemEventHandler):
    def __init__(self, target_dir):
        super().__init__()
        self.target_dir = target_dir

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
        if event.is_directory:
            return None

        path = Path(event.src_path)
        id = self.is_arxiv(
            path
        )  ## Checks if new file is an arXiv paper, if so returns its id

        if not id:
            return None

        new_name = self.get_file_name(
            id
        )  ## Retrieves metadata and formats new filename
        new_path = Path(self.target_dir) / Path(new_name)
        path.rename(new_path)

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

        return self.format_file_name(title, authors)

    def format_file_name(self, title, authors):
        """Returns formatted filename from the title and list of authors. Isolated step containing the naming logic.

        Args:
            title: title of the article returned by arXiv API query.
            authors: list of authors of the article returned by arXiv API query.

        Returns:
            string in the form desired_file_name.pdf.
        """
        clean_title = clean(
            title, fix_unicode=True, to_ascii=True, lower=True, no_punct=True
        ).replace(" ", "-")
        lower_last_names = [name.split(" ")[-1].lower() for name in authors]
        author_preamble = "-".join(lower_last_names[:3])
        new_file_name = author_preamble + "-" + clean_title + ".pdf"

        return new_file_name
