# -*- encoding: utf-8 -*-
#@File    :   data_utils.py
#@Time    :   2023/01/20 07:25:54
#@Author  :   Li Suchi 
#@Email   :   lsuchi@126.com

from pathlib import Path

import pandas as pd
import numpy as np

def load_data(data_dir:Path, dataset:str='criteo'):
    if not isinstance(data_dir, Path):
        data_dir = Path(data_dir)
    
    if dataset == 'criteo':
        train = pd.read_csv(data_dir / 'train.csv')
        test = pd.read_csv(data_dir / 'test_csv')
        
    elif dataset == 'ml-1m':
        pass
    elif dataset == 'ml-100k':
        pass

def preprocess_data():
    pass
    
def _type_infer():
    pass

class DataCenter():
    pass

