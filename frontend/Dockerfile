FROM node:16-alpine

WORKDIR /app
COPY package.json yarn.lock /app/
RUN yarn install

EXPOSE 8080
CMD ["yarn", "run", "serve"]
