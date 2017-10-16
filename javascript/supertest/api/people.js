"use strict";

let request = require('supertest')

let Base = require('./base');

class People extends Base {
    constructor() {
        super();
    }

    getAllPeople() {
        return request(this.baseUrl).get("/people/");
    }

    getAllPeopleHeadersContentType() {
        return request(this.baseUrl).get("/people/")
    }

    getSpecificPeople(identifier) {
        return request(this.baseUrl).get("/people/" + identifier + "/")
    }
}

module.exports = People;