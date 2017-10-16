let Peoples = require('../api/peoples')
Peoples = new Peoples()

describe('swapi peoples tests ', function() {

    it('returns a 200 when getting all peoples', function testAllPeoples(done) {
        Peoples.getAllPeoples().expect(200, done);
    });

    it('returns proper content type when getting all peoples', function testAllPeoples(done) {
        Peoples.getAllPeoplesHeadersContentType().expect('Content-Type', /json/).expect(200, done);
    });

    it('returns a 200 when getting people with id 1', function testAllPeoples(done) {
        Peoples.getSpecificPeople(1).expect(200, done);
    });

    it('returns a proper people name when getting people with id 1', function testAllPeoples(done) {
        Peoples.getSpecificPeople(1)
            .expect(200, /Luke Skywalker/, done);
    });
});