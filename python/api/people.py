#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from .base import Base


class People(Base):

    def get_all_(self):
        return requests.get("{base_url}/people/".format(base_url=self.base_url))

    def get_all__headers_conent_type(self):
        return requests.get("{base_url}/people/".format(base_url=self.base_url)).headers["Content-Type"]

    def get_specific_people(self, identifier):
        return requests.get("{base_url}/people/{id}/".format(base_url=self.base_url, id=identifier))

    def get_specific_people_name(self, identifier):
        response_json = self.get_specific_people(identifier).json()
        return response_json["name"]
