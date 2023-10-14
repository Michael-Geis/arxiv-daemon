from cleantext import clean


def format_file_name(title, authors):
    """Returns formatted filename from the title and list of authors. Isolated step containing the naming logic.

    Args:
        title: title of the article returned by arXiv API query.
        authors: list of authors of the article returned by arXiv API query.

    Returns:
        string in the form desired_file_name.pdf.
    """
    ## Remove illegal characters from title, switch to lowercase, transliterate to ASCII
    clean_title = (
        clean(
            title,
            fix_unicode=True,
            to_ascii=True,
            lower=True,
        )
        .replace(" ", "-")
        .replace("?", "")
        .replace(":", "")
        .replace("*", "star")
        .replace("/", "")
        .replace("\\", "")
    )
    ## Get the last names of the last three authors and join them with '-'
    first_three_authors = authors[:3]
    lower_last_names = [name.split(" ")[-1].lower() for name in first_three_authors]
    author_preamble = "-".join(lower_last_names)

    ## Join author list to cleaned title string
    new_file_name = author_preamble + "-" + clean_title + ".pdf"

    return new_file_name
