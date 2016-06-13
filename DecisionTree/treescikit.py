import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV

df = pd.read_csv('../LearnMLwithsciKit/DecisionTree/data/ad.data.csv', header=None, low_memory=False)

#if __name__ == '__main__':
#    df = pd.read_csv('data/ad.data', header=None)
#    explanatory_variable_columns = set(df.columns.values)
#    response_variable_column =
