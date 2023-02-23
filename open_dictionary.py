import pickle

# open the file for reading
with open('macro_city_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    loaded_data = pickle.load(f)
    
with open("no_results.txt", "r") as f:
    result_errors = [line.strip() for line in f.readlines()]

