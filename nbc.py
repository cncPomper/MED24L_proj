import pandas as pd
import numpy as np

class NBC:
  def __init__(
      self,
      data: pd.DataFrame,
      k: int,
      l: int # zamienić na p???
  ):
    self.data = data
    # Algorithm parameter
    self.k = k
    # Coś
    self.l = l
    # Number of objects
    self.n = len(self.data)
    # Noise set
    self.noise_set = []
    # Distances of each object to other objects
    self.distances = []
    # KNB values for each object
    self.knb_count = np.zeros(self.n, dtype=np.int32)
    # Reverse KNB values for each object
    self.rev_knb_count = np.zeros(self.n, dtype=np.int32)
    # Neighbours
    self.neighbours = []
    # Cluster numbers for noise
    self.clst_no = np.full(self.n, -99)


  #
  # Some documentation
  #
  def minkowski_dist(self, X, Y, p: int) -> float:
    return np.power(np.sum(np.power(np.abs(x - y), p) for x, y in zip(X, Y)), 1/p)

  def update_knb(self):
    pass

  def update_rev_knb(self):
    pass

  def calc_ndf(knb: int, rev_knb: int):
    return rev_knb/knb

  def sum_noise(self):
    for p in self.data:
      if p.clst_no == 0:
        self.noise_set.append(p)

  #
  def calc_dists(
    self,
    data: pd.DataFrame
  ):
    self.distances = [
      [(i, (self.minkowski_dist(y, x, self.l))) for i, x in data.iterrows()] for j, y in data.iterrows()
    ]


  def cluster(self):
    for obj in self.data:

      self.update_knb()
      self.update_rev_knb()

      obj.ndf = self.calc_ndf(self.knb_count, self.rev_knb_count)

      if obj.clst_no != 0 or obj.ndf < 1:
        continue

      # label new cluster
      obj.clst_no = self.cluster_count

      # Init DPset <- Todo



