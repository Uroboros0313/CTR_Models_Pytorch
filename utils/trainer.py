import logging

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class DeepCTRTrainer():
    def __init__(
        self,
        model,
        dataloader,
        criterion,
        optimizer,
        n_epochs,
        device,
        verbose_interval:int=1) -> None:
        
        self.model = model
        self.dataloader = dataloader
        self.criterion = criterion
        self.optimizer = optimizer
        self.n_epochs = n_epochs
        self.device = device
        self.verbose_interval = verbose_interval
    
    def train(self):
        for epoch in range(self.n_epochs):
            self.model.train()
            l_sum = 0.0
            for *inputs, label in self.dataloader.train:
                l = self._train(inputs, label)
                l_sum += l
            
            if (epoch + 1) % self.verbose_interval == 0:
                print("EPOCH {}: TRAIN LOSS: {}".format(epoch + 1, l_sum))
        return self.model
    
    def _inference(self, inputs, label):
        inputs = [input.to(self.device) for input in inputs]
        label = label.to(self.device)
        pred = self.model(*inputs)
        return pred
    
    def _train(self, inputs, label):
        pred = self._inference(inputs, label)
        self.optimizer.zero_grad()
        l = self.criterion(pred, label)
        l.backward()
        self.optimizer.step()
        
        return l.item()

    def evaluate(self, ds_name='valid'):
        loader = getattr(self.dataloader, ds_name)
        
        self.model.eval()
        with torch.no_grad():
            labels = []
            preds = []
            for *inputs, label in loader:
                pred = self._inference(inputs, label)
                preds.append(pred)
                labels.append(label)
                
            preds = torch.cat(preds, dim=0).cpu().numpy()
            labels = torch.cat(labels, dim=0).cpu().numpy()
    