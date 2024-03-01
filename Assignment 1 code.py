import pandas as pd
## Import training data
train= pd.read_csv('train.csv')
print(train.head(5))
##BEFORE ANY INSPECTION: split in train (70%) // validation (20%) // test set (10%)
train_end = int(0.70*len(train)) ##calculates the index number for the splits
val_end = train_end + int(0.20*len(train))
train_df = train[:train_end]
validation_df = train[train_end:val_end]
test_df =  train[val_end:]
print(len(train_df))
print(len(validation_df))
print(len(test_df))
##preprocessing on train (and validation?) set

##missing values in train
MV_count = train_df.isnull().sum()
##print(MV_count)
columns_with_MV = MV_count[MV_count>0]
print(columns_with_MV)