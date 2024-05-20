### Preprocessing and Training


The notebooks has all the preprocessing, dataset analysis, training of models along with saving weights. 

There are 4 notebooks
1. notebook_without_training_cleanup - This notebook takes in the dataset without the neutral class and trains models on top with some analysis.
2. notebook_with_common_words_based_cleanup - This notebook analyses common words and their presence in the dataset then trains the model on top.
3. notebook_with_training_data_filtering - This notebook dives deeper into the presence of neutral sentences and then train the model.
4. notebook_with_bert_glove_embeddings - This notebook trains bert model along with glove embeddings. 

Best Performance with the models - notebook_with_training_data_filtering

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

### The swagger code is entirely Dockerized

