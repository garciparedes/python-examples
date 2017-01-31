#!/usr/bin/env python

"""
URL: http://docs.graphene-python.org/en/latest/types/enums/
"""

import graphene


class Episode(graphene.Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

    @property
    def description(self):
        if self == Episode.NEWHOPE:
            return 'New Hope Episode'
        return 'Other episode'
