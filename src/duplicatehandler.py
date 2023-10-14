import os


class DuplicateHandler:
    def __init__(self, on_duplicate) -> None:
        self.case = on_duplicate

    def handle_duplicate(self, path, new_path):
        if self.case == "open":
            os.system(f"rm -rf {path}")
            os.system(f'start "" /max "{new_path}"')
        if self.case == "ignore":
            pass
        if self.case == "prune":
            os.system(f"rm -rf {path}")
