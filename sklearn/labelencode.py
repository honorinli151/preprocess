import logging
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

def encoder_gen(X, x_train):
    '''Calcaulate the LabelEncoder and OneHotEncoder of given X and x_train
    Args: 
        X: the whole dataset
        x_train: the train part of X
    Return:
        le: LabelEncoder of X
        enc: OneHotEncoder of x_train
    Raise:
    '''
    le = LabelEncoder()
    enc = OneHotEncoder(handle_unknown='ignore')
    le.fit(X)
    logging.info('LabelEncoder done.')
    x_train = le.transform(x_train)
    enc.fit(x_train.reshape(-1, 1))
    logging.info('OneHotEncoder done.')
    return le, enc

def encode(encoder, x):
    '''Calculate the OneHotEncoder of a set x
    Args: 
        x: a part of X in encoder_gen function
        encoder: [le, enc]
    Return:
        the OneHot representation of x
    Raise:
    '''
    return encoder[1].transform(encoder[0].transform(x).reshape(-1, 1))

for i, cat in enumerate(cat_cols):
    logging.info('encoding %s ...' % cat, end='')

    encoders[i] = OneHotEncoder.fit(market_train.loc[train_indices, cat].astype(str).unique().tolist)
    market_train[cat] = encode(encoders[i], market_train[cat])
    logging.info('Done.')