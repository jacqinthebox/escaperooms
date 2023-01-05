FROM node:14-alpine

WORKDIR /usr/src/app

#COPY src/frontend/rollup.config.js ./
#COPY src/frontend/package*.json ./
#COPY src/frontend/.env ./
#RUN npm install

#COPY src/frontend/src ./src
#COPY src/frontend/public ./public

COPY rollup.config.js ./
COPY package*.json ./
COPY .env ./
RUN npm install

COPY src ./src
COPY public ./public



RUN npm run-script build

EXPOSE 3000

ENV HOST=0.0.0.0

CMD [ "npm", "start" ]