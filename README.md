### Preprocessing and Training


The notebook has all the preprocessing, dataset analysis, training of models along with saving weights. 

### The trained model API is live 

curl -X POST "http://20.42.62.249:8082/internal/sentiment_analysis/analyse/text" \        
  -H "Accept: */*" \
  -H "Content-Type: application/json" \
  -d '{"text":"This is such a bad day"}'

Expected Output 

{
  "sentiment": "NEGATIVE",
  "status": 1
}



