# -*- coding: utf-8 -*-
import sys
sys.path += ['../..',
             '..',
             '../converters',
             '../tests']

from manga_feed.classes import *
from hashlib import md5
from random import randint

N_TITLES = 500
AVG_CHAPTERS = 50
AVG_PAGES = 20


def blob(prefix='', blob_length=32):
    if blob_length > 32:
        raise ValueError("Must be less than 32!")

    r_bytes = bytes(randint(0, 10000))

    return '%s%s' % (prefix, md5(r_bytes).hexdigest())


class ObjectFactory:
    """docstring for ObjectFactory"""

    def __init__(self, target_class):

        self.target_class = target_class
        self.built_objects = []

    def create_n(self, qty):
        built_objects = []

        for i in range(1, qty + 1):
            built_objects.append(
                self._create(i)  # Forcing specialization!
            )
            print("%s: %d" % (self.target_class, i))

        return built_objects


class ImageFactory(ObjectFactory):

    def _create(self, number):
        return Image(
            width=600,
            height=1200,
            ref='asdqew.com/pages/%s' % blob()
        )


class PageFactory(ObjectFactory):

    def _create(self, number):
        return Page(
            image=ImageFactory(Image)._create(1),
            number=number
        )


class ChapterFactory(ObjectFactory):

    def _create(self, number):
        return Chapter(
            name=blob('chapter_name', 8),
            pages=PageFactory(Page).create_n(AVG_PAGES),
            number=number
        )


class GenreFactory(ObjectFactory):

    def _create(self, number):
        return Genre(
            name=blob('genre_name_', 4),
            description=blob('genre_description_', 4),
        )


class AuthorFactory(ObjectFactory):

    def _create(self, number):
        return Author(
            first_name=blob('author_fn_', 16),
            last_name=blob('author_ln_', 16),
        )


class TitleFactory(ObjectFactory):

    def _create(self, number):
        return Title(
            name=blob('manga_title_', 16),
            description=blob('manga_description_'),
            authors=AuthorFactory(Author).create_n(2),  # fixme, get from pool
            genres=GenreFactory(Genre).create_n(5),  # fixme, get from pool
            chapters=ChapterFactory(Chapter).create_n(AVG_CHAPTERS),
        )

if __name__ == '__main__':
    print('Populating world')
    results = TitleFactory(Title).create_n(N_TITLES)
    print('Finished')
