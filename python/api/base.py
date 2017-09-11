#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Base(object):
    def __init__(self):
        self.base_url = "https://swapi.co/api"

    def get_base_url(self):
        return self.base_url
