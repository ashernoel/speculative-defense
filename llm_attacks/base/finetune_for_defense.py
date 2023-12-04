import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import pandas as pd
import torch.nn as nn

class CustomDataset(Dataset):
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        self.tokenizer = AutoTokenizer.from_pretrained("/n/home10/anoel/vicuna-7b-v1.3")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data.iloc[idx]
        inputs = self.tokenizer(item['output'], padding='max_length', truncation=True, return_tensors="pt")
        label = 1 if item['label'] == 'UNSAFE' else 0
        return inputs.input_ids.squeeze(0), torch.tensor(label)

class VicunaPEFT(nn.Module):
    def __init__(self, model_path):
        super(VicunaPEFT, self).__init__()
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=2)

    def forward(self, input_ids):
        return self.model(input_ids)

def train(model, dataloader, optimizer, criterion):
    model.train()
    for input_ids, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(input_ids)
        loss = criterion(outputs.logits, labels)
        loss.backward()
        optimizer.step()

def main():
    dataset = CustomDataset('/n/home10/anoel/llm-attacks/experiments/malicious_output_dataset.csv')
    dataloader = DataLoader(dataset, batch_size=8, shuffle=True)
    
    model = VicunaPEFT("/n/home10/anoel/vicuna-7b-v1.3")
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5) 
    criterion = nn.CrossEntropyLoss()

    epochs = 3  # Adjust as needed
    for epoch in range(epochs):
        train(model, dataloader, optimizer, criterion)

    # Save the fine-tuned model
    model.save_pretrained('/n/home10/anoel/vicuna-7b-v1.3/vicuna-tuned')

if __name__ == "__main__":
    main()
