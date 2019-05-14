import pandas as pd

from model import cluster, person
from view import describe

def exploratory_analysis():
    describe({"Cluster DF":cluster,
              "Person DF": person})
