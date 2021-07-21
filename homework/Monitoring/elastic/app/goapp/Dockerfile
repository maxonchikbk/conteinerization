FROM golang:1.16 as builder
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN go get go.elastic.co/apm
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o server .

FROM scratch
COPY --from=builder /app/server /

CMD ["/server"]
