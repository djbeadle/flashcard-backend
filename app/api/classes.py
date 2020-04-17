import random

class Flashcard:
    """
        title str: The short, primary description of this card
        description str: A description of a few sentences or several paragraphs describing 
    """
    def __init__(self, title: str, description: str, source: str="", image_url: str="", tags: str="", id=None):
        self.id = None if id is None else id # Don't know this value until we insert into SQLite
        self.title = title
        self.description = description
        self.source = source
        self.image_url = image_url
        self.tags = tags
        
