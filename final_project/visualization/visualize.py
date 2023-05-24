import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In the beginning, this was a cell in a notebook. But now it has been converted into a script in order to work more efficient (modular and granular)

def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
        data=df, #this will be a parameter when creating the graph
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")




# Creating another function for plotting a different graph
def latam_global_context(df: pd.DataFrame):
    sns.barplot(
        data=df,
        x="value",
        y="country_region",
        palette=df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context")