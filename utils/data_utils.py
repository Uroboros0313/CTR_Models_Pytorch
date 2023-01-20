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
    
    return train, test
    
    
class DataTable():
    def __init__(
        self,
        train_set,
        test_set=None,
        metadata=None) -> None:
        
        self.train_set = train_set
        self.test_set = test_set
        
        if metadata == None:
            self.__infer_metadata(train_set, )
        else:
            self.metadata = metadata
    
    def preprocess_data(
        self,
        num_scale='minmax',
        cat_enc='label',
        num_fill_method='mean',
        cat_fill_val='<UNKNOWN>'):
        '''
        1.缺失值填充
        2.标准化
        3.标签编码
        4.补充metadata
        '''
        
    def __fill_null(self):
        pass
    
    def __encode(self):
        pass
    
    @staticmethod
    def label_encoder(series):
        ss_vals = series.unique()
        ss_lbs = list(range(len(ss_vals)))
        val2lb = dict(zip(ss_vals, ss_lbs))
        lb2val = dict(zip(ss_lbs, ss_vals))
        
        series = series.map(val2lb)
        return series, val2lb, lb2val
        
    @staticmethod
    def minmax_scaler(series):
        ss_min = series.min()
        ss_max = series.max()
        series = (series - ss_min) / (ss_max - ss_min)
        return series, ss_min, ss_max
    
    @staticmethod
    def standard_scaler(series):
        ss_mean = series.mean()
        ss_std = series.std()
        series = (series - ss_mean) / ss_std
        return series, ss_mean, ss_std

    
    def __infer_metadata(self, df:pd.DataFrame, dataset=None)->Dict[str, List]:
        '''
        区分类别型数据与数值型数据
        '''
        num_cols = df.select_dtypes(include='number').columns.to_list()
        cat_cols = df.select_dtypes(include=object).columns.to_list()
            
        for n_col in num_cols:
            if df[n_col].nunique() < len(df) * 0.01:
                num_cols.remove(n_col)
                cat_cols.append(cat_cols)
        
        self.metadata = {'num_cols': num_cols, 'cat_cols': cat_cols}
        


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

    

    
class DataCenter():
    pass

