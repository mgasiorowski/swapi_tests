#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api.peoples import Peoples


class TestPeoples(object):

    def test_should_get_all_peoples_return_200(self):
        response = Peoples().get_all_peoples()
        assert response.status_code == 200

    def test_should_get_personreturn_proper_content_type(self):
        content_type = Peoples().get_all_peoples_headers_conent_type()
        assert "application/json" == content_type

    def test_should_get_person_with_id_from_peoples_return_200(self):
        response = Peoples().get_specific_people(1)
        assert response.status_code == 200

    def test_should_get_person_with_id_from_peoples_return_proper_people(self):
        people_name = Peoples().get_specific_people_name(1)
        assert "Luke Skywalker" == people_name
