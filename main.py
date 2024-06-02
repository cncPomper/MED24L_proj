from preprocessing import Preprocessing
import pandas as pd
from scipy.io.arff import loadarff
import json

def load_data(config_file):
  with open(config_file, 'r') as f:
    config = json.load(f)

  dataset_path = config['dataset_path']
  format = dataset_path.split(".")[-1]

  if format == 'arff':
    data = loadarff(dataset_path)
    data = pd.DataFrame(data[0])
  elif format == 'csv':
    data = pd.read_csv(dataset_path)
  else:
    raise ValueError("Bad file format. Only csv and arff file formats are accepted")

  return data

def main():
  # data = pd.read_csv(dataset_path)

  data = load_data('config.json')

  # Data preprocessing
  data = Preprocessing(data)
  data = data.append_cols()

  print(data)

if __name__ == '__main__':
  main()