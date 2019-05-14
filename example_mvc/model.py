import pandas as pd

#def cluster(dataset.dataframe)
def cluster():

    def __init__(self):
        self.load()
        self.tidy()

    def load(self):
        self.raw = pd.read_csv("local_data/ex_dm_cluster_demo.csv")

    def tidy(self):
        df = self.raw
        df["academic"] = df["academic"].astype("category")
        df.rename({"Clust_id":"Cluster ID",
                   "academic":"Academic?"}, inplace=True)
        self.data = df

    def schema(self):
        # can probably automate this function if we have a known data structure
        # like pandas.. return data.shortcuts.pandas_schema(self.data)
        return {"Cluster ID": ["str", "not_null", "unique"],
                "Academic?": ["category[2]"]}

#def cluster(dataset.dataframe)
def person():

    def __init__(self):
        self.load()
        self.tidy()

    def load(self):
        self.raw = pd.read_csv("local_data/ex_dm_person_demo.csv")

    def tidy(self):
        df = self.raw
        df[df == "999"] = np.nan
        df["Education"] = df["Education"].str.lower().astype("category")
        df["outcome"] = df["outcome"].astype("category")
        self.data = df

    def schema(self):
        pass
