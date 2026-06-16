def extract_title(markdown):
    md_title = "# "
    if len(markdown) <= 2:
        raise ValueError(f"text too short to be a title: {markdown}")
    if markdown.startswith(md_title):
        return markdown[len(md_title):].strip()
    else:
        raise ValueError(f"not a valid md title: {markdown}")