import pandas as pd
import numpy as np

class Preprocessing:
  def __init__(
      self,
      data: pd.DataFrame,
      # cols: list = ['clst_no', 'ndf'] # usable at all ???
  ):
    # Processed dataset
    self.data = data
    # Dataset length
    self.n = len(self.data)
    # Columns to append
    # self.cols = cols

  def append_cols(self):
    return self.data.assign(
      clst_no=pd.Series(np.zeros(self.n, dtype=np.int32)).values,
      ndf=pd.Series(np.zeros(self.n, dtype=np.float32)).values
    )

  def handle_cat_values(self):
    pass
