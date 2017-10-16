#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api.people import People


class TestPeople(object):

    def test_should_get_all__return_200(self):
        response = People().get_all_()
        assert response.status_code == 200

    def test_should_get_person_return_proper_content_type(self):
        content_type = People().get_all__headers_conent_type()
        assert "application/json" == content_type

    def test_should_get_person_with_id_from__return_200(self):
        response = People().get_specific_people(1)
        assert response.status_code == 200

    def test_should_get_person_with_id_from__return_proper_people(self):
        people_name = People().get_specific_people_name(1)
        assert "Luke Skywalker" == people_name
