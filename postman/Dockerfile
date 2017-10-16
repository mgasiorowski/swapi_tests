FROM node:4.2.3

RUN mkdir /app
WORKDIR /app
COPY package.json /app/
RUN npm install
COPY . /app
ENTRYPOINT ["npm", "run", "test-all"]