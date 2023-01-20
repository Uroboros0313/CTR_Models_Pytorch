# -*- encoding: utf-8 -*-
#@File    :   data_utils.py
#@Time    :   2023/01/20 07:25:54
#@Author  :   Li Suchi 
#@Email   :   lsuchi@126.com

from typing import List, Dict
from pathlib import Path
from itertools import product

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


def manual_feature_cross(df:pd.DataFrame, cross_pairs:List=[])->pd.DataFrame:
    '''
    WideDeep论文中的手动特征交叉
    '''
    for c1_name, c2_name in cross_pairs:
        ss1, ss2 = df[c1_name], df[c2_name]
        c1 = ss1.unique()
        c2 = ss2.unique()
        
        combs = list(product(c1, c2))
        combs_id = range(len(combs))
        map_ = dict(zip(combs, combs_id))
        ss_comb = pd.Series(zip(ss1, ss2)).map(map_)
        df = pd.concat([df, pd.get_dummies(ss_comb, prefix=f"CP_{c1_name}_{c2_name}")], axis=1)
    
    return df


def preprocess_data():
    '''
    1.缺失值填充
    2.标准化
    3.标签编码
    4.补充metadata
    '''
    pass

    
def _infer_metadata(df:pd.DataFrame, dataset=None)->Dict[str, List]:
    '''
    区分类别型数据与数值型数据
    '''
    if dataset == None:
        num_cols = df.select_dtypes(include='number').columns.to_list()
        cat_cols = df.select_dtypes(include=object).columns.to_list()
        
        for n_col in num_cols:
            if df[n_col].nunique() < len(df) * 0.05:
                num_cols.remove(n_col)
                cat_cols.append(cat_cols)
                
    elif dataset == 'criteo':
        cols = df.columns
        num_cols = cols[df.columns.str.startswith('I')].to_list()
        cat_cols = cols[df.columns.str.startswith('C')].to_list()
        
    else:
        pass
    
    metadata = {'num_cols': num_cols, 'cat_cols': cat_cols}
    
    return metadata
    
class DataCenter():
    pass

