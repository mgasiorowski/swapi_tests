#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import requests


class Peoples(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/default.ini")
        self.base_url = self.config["DEFAULT"]["base_url"]

    def get_all_peoples(self):
        return requests.get("{base_url}/people/".format(base_url=self.base_url))

    def get_all_peoples_headers_conent_type(self):
        return requests.get("{base_url}/people/".format(base_url=self.base_url)).headers["Content-Type"]

    def get_specific_people(self, identifier):
        return requests.get("{base_url}/people/{id}/".format(base_url=self.base_url, id=identifier))

    def get_specific_people_name(self, identifier):
        response_json = self.get_specific_people(identifier).json()
        return response_json["name"]
