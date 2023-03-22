import pickle

# open the file for reading
with open('macro_and_housing_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    loaded_data = pickle.load(f)
    
with open("clean_no_results.txt", "r") as f:
    result_errors = [line.strip() for line in f.readlines()]

