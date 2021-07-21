package main

import (
	"context"
	"log"
	"net/http"
	"time"

	"github.com/go-chi/chi/v5"
	"go.elastic.co/apm"
)

func main() {

	r := chi.NewRouter()
	r.Use(Middleware())
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		span, ctx := apm.StartSpan(r.Context(), "RootHandler", "Request")
		defer span.End()

		processingRequest(ctx)
		_, err := w.Write([]byte("root."))
		if err != nil {
			log.Println(err)
		}
	})
	log.Fatal(http.ListenAndServe(":8080", r))
}

func processingRequest(ctx context.Context) {
	span, ctx := apm.StartSpan(ctx, "processingRequest", "custom")
	defer span.End()

	// time sleep simulate some processing time
	time.Sleep(15 * time.Millisecond)
	return
}

