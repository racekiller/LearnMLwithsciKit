import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


if __name__ == '__main__':
    df = pd.read_csv('~/Documents/GitHub/LearnMLwithsciKit/DecisionTree/data/ad.data.csv', header=None, low_memory=False)
    # The set command will give us the number or columns in an array
    explanatory_variable_columns = set(df.columns.values)
    # The len will give us the length of the dataframe, this way we can
    # substract and get the number of coumns we want
    response_variable_column = df[len(df.columns.values) - 1]
    # The last column describes the targets, here we remove the last column
    # to get only the data except the target
    explanatory_variable_columns.remove(len(df.columns.values) - 1)
    # Assign to y the target and convert the text to an integer
    y = [1 if e == 'ad.' else 0 for e in response_variable_column]
    # The X are the features
    X = df[list(explanatory_variable_columns)]
    X.replace(to_replace=' *\?', value=-1, regex=True, inplace=True)
    # split the data to train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # pipeline = Pipeline([('clf', DecisionTreeClassifier(criterion='entropy'))
    #                     ])
    # parameters = {
    #     'clf__max_depth': (150, 155, 160),
    #     'clf__min_samples_split': (1, 2, 3),
    #     'clf__min_samples_leaf': (1, 2, 3)
    # }

    pipeline = Pipeline([('clf', RandomForestClassifier(criterion='entropy'))
                        ])
    parameters = {
        'clf__n_estimators': (5, 10, 20, 50),
        'clf__max_depth': (50, 150, 250),
        'clf__min_samples_split': (1, 2, 3),
        'clf__min_samples_leaf': (1, 2, 3)
    }

    grid_search = GridSearchCV(pipeline, parameters, n_jobs = -1,
        verbose = 1, scoring='f1')
    grid_search.fit(X_train, y_train)
    print ('Best score: %0.3f' % grid_search.best_score_)
    print ('Best parameters set:')
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print ('\t%s: %r' % (param_name, best_parameters[param_name]))

    predictions=grid_search.predict(X_test)
    print (classification_report(y_test, predictions))

