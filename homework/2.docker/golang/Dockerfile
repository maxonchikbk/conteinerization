from golang as builder
run mkdir /app
copy ./app
workdir /app
run cgo_enabled=0 goos=linux goarch=amd64 go build -o server .

from scratch
copy --from=builder /app/server /
expose 8080
cmd ["/server"]
