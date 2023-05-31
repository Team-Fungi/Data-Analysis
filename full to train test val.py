import pandas as pd

# Opening csv file as pandas
df = pd.read_csv('Taxonomy_99_5%_noambi.csv')

# Splitting data into 6:2:2 - Train:Test:Validation
train = df.sample(frac=0.6) # Train has 62 193 sequences
rest_40percent = df.drop(train.index)
test = rest_40percent.sample(frac=0.5) # Test has 20 730 sequences
validation = rest_40percent.drop(test.index) # Validation has 20 730 sequences

# Saving data in new csv files
train.to_csv('Train_5%_noambi.csv', index=None)
test.to_csv('Test_5%_noambi.csv', index=None)
validation.to_csv('Validation_5%_noambi.csv', index=None)
