request = require('supertest')

let Base = require('./base');

class Peoples extends Base {
    constructor() {
        super();
    }

    getAllPeoples() {
        return request(this.baseUrl).get("/people/");
    }

    getAllPeoplesHeadersContentType() {
        return request(this.baseUrl).get("/people/")
    }

    getSpecificPeople(identifier) {
        return request(this.baseUrl).get("/people/" + identifier + "/")
    }
}

module.exports = Peoples;