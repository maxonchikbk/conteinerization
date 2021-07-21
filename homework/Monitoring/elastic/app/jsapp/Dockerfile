FROM node:alpine
WORKDIR /tmp
COPY index.js /tmp
RUN npm install express
RUN npm install elastic-apm-node 
CMD ["node","index.js"]