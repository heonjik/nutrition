import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import torch
from transformers import BertTokenizer
from torch.utils.data import DataLoader, TensorDataset
from transformers import BertForSequenceClassification
from transformers import AdamW
from tqdm import tqdm # For progress bars

df = pd.read_csv('WordDifficulty.csv')

# Categorize into "simple" and "difficult" words.
simple_word_list = df.loc[df['I_Zscore'] <= 0]
diff_word_list = df.loc[df['I_Zscore'] > 0]

def main():
    # Split the data into training and testing sets
    indicies = np.arange(len(df))
    indices_train, indices_test = train_test_split(indicies, test_size=0.3, random_state=42)
    df_train = df.iloc[indices_train]
    df_test = df.iloc[indices_test]

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Tokenize the text
    df_train = df_train.dropna()    # filter nan values
    words = df_train['Word']
    words = words.to_list() # Convert the series to a list

    encodings = tokenizer(
        words,
        truncation=True,
        padding=True,
        return_tensors="pt"
    )

    # Create the dataset
    labels = torch.tensor(df_train['I_Zscore'].values)
    input_ids = encodings['input_ids']
    attention_mask = encodings['attention_mask']
    train_dataset = TensorDataset(input_ids, attention_mask, labels)
    print(train_dataset)

    # Create the DataLoader
    dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)

    # Load the BERT model
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

    # Define the optimizer
    optimizer = AdamW(model.parameters(), lr=1e-5)

    # Training loop
    model.train()
    for epoch in range(3):
        loop = tqdm(dataloader, leave=True)
        for batch in loop:
            index_id, mask, score = batch
            index_id = index_id.int()
            mask = mask.int()
            
            optimizer.zero_grad()
            
            outputs = model(input_ids=index_id, attention_mask=mask, labels=score)
            print(outputs.size(), labels.size())
            
            loss = outputs.loss
            loss.backward() # Backward pass

            optimizer.step()    # Update weights

            loop.set_description(f"Epoch {epoch}")  # Print loss
            loop.set_postfix(loss=loss.item())

if __name__=='__main__':
    main()