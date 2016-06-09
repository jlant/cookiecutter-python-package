# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.project_slug}}.{{ cookiecutter.project_slug}}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A short description.

    :authors: {{ cookiecutter.year }} by {{ cookiecutter.full_name }}, see AUTHORS
    :license: CC0 1.0, see LICENSE file for details
"""

def hello(msg="World"):
    """Function that prints a message.

    :param msg: message to say
    :type msg: string
    :returns: string
    :raises: something

    .. note::
       You can note something here.

    .. warning::
       You can warn about something here.

    >>> hello()
    Hello World!
    >>> hello(msg="there")
    Hello there!
    """
    return "Hello {}!".format(msg)
