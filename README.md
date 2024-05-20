### Preprocessing and Training


The notebook have all the preprocessing and training of models along with saving weights 

### The trained model is API 

curl -X POST "http://20.42.62.249:8082/internal/sentiment_analysis/analyse/text" \        
  -H "Accept: */*" \
  -H "Content-Type: application/json" \
  -d '{"text":"This is such a bad day"}'

Expected Output 

{
  "sentiment": "NEGATIVE",
  "status": 1
}

### Model Swagger API is live and can be used for testing 

