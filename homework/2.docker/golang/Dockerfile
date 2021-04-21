FROM golang as builder

RUN mkdir /app

COPY . /app

WORKDIR /app
RUN CGO_ENABLED=0 goos=linux goarch=amd64 go build -o server .

FROM scratch

COPY --from=builder /app/server /

EXPOSE 8080
CMD ["/server"]