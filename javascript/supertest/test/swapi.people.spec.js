"use strict";

let People = require('../api/people')
People = new People()

describe('swapi people tests ', function() {

    it('returns a 200 when getting all people', function testAllPeople(done) {
        People.getAllPeople().expect(200, done);
    });

    it('returns proper content type when getting all people', function testAllPeople(done) {
        People.getAllPeopleHeadersContentType().expect('Content-Type', /json/).expect(200, done);
    });

    it('returns a 200 when getting people with id 1', function testAllPeople(done) {
        People.getSpecificPeople(1).expect(200, done);
    });

    it('returns a proper people name when getting people with id 1', function testAllPeople(done) {
        People.getSpecificPeople(1).expect(200, /Luke Skywalker/, done);
    });
});