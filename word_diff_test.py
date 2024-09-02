import torch
from transformers import BertModel, BertTokenizer

class BERTRegressor(torch.nn.Module):
    def __init__(self, bert_model):
        super(BERTRegressor, self).__init__()
        self.bert = bert_model
        self.dropout = torch.nn.Dropout(0.3)
        self.linear = torch.nn.Linear(768, 1)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        output = outputs.pooler_output
        output = self.dropout(output)
        return self.linear(output)
    
bert_model = BertModel.from_pretrained('bert-base-uncased')

model = BERTRegressor(bert_model)

model.load_state_dict(torch.load('bert_regressor.pt'))

model.eval()

# Example word
new_word = "linguistic"
'''
Big - Enormous
Happy - Euphoric
Sad - Melancholy
Funny - Hilarious
'''

# Tokenize the word
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
encoding = tokenizer.encode_plus(
    new_word,
    add_special_tokens=True,
    max_length=10,
    padding='max_length',
    return_attention_mask=True,
    return_tensors='pt',
    truncation=True
)

input_ids = encoding['input_ids']
attention_mask = encoding['attention_mask']

# Make prediction
with torch.no_grad():
    prediction = model(input_ids, attention_mask)
    print(f"Predicted difficulty score: {prediction.item():.4f}")
