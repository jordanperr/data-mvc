import pandas as pd

#@view.console
def describe(out, dfs):
    for name, df in dfs:
        out.println("{}".format(name))
        out.println("--------------------")
        out.println("{}".format(df.describe()))
        out.println("\n\n")
