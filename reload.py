import pickle

with open('scanned_sequence.pkl', 'rb') as file:
    scanned_sequence = pickle.load(file)
pickle.dump(scanned_sequence, open('scanned_sequence.pkl', 'wb'))