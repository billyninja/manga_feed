from datetime import datetime
from converters.base import BaseConverter


class Image:
    def __init__(self, ref, width, height):
        self.ref = ref
        self.width = width
        self.height = height


class Page:
    def __init__(self, number, image):
        self.number = number
        self.image = image


class Chapter:
    def __init__(self, number, name, pages, date_added=None):
        self.number = number
        self.name = name
        self.pages = pages
        self.date_added = date_added or datetime.today()


class Genre:
    """docstring for Genre"""

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Author:
    """docstring for Author"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Title:
    def __init__(self, name, description, authors, genres, chapters):
        self.name = name
        self.description = description
        self.authors = authors
        self.genres = genres
        self.chapters = chapters


class Package:
    """docstring for Package"""

    def __init__(self, title, converter, request_time, request_ip):

        if converter is not BaseConverter:
            raise TypeError("converter param must inherit BaseConverter")

        self.title = title
        self.converter = converter
        self.request_time = request_time
        self.request_ip = request_ip


class ChaptersPackage(Package):
    """docstring for ChaptersPackage"""

    def __init__(self,
                 title,
                 chapters,
                 output_format,
                 request_time,
                 request_ip):
        super(ChaptersPackage, self).__init__()
        self.chapters = chapters
