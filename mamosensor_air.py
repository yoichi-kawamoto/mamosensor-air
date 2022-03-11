import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

files = glob.glob("*.csv")
format = ".png"
pd.set_option("display.max_rows", 4000)
exceed = 0

for file in files:
    try:
        df = pd.read_csv(file, header=0, index_col=[4], parse_dates=[4], names=("IMEI", "CO₂", "Temperature", "Humidity", "Date"))
        file_name = file[0:7].replace("-", "年") + "月_" + file[22:-4]
        if df["CO₂"].max() >= 1000:
            print("\n"*exceed, file_name)
            print(df[["CO₂"]][df["CO₂"] >= 1000])
            exceed = 1
        df.drop("IMEI", axis=1).plot(subplots=True, figsize=(12, 12), grid=True, sharex=False)
        axes = plt.gcf().get_axes()
        for axis in axes:
            axis.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
            axis.xaxis.set_major_locator(mdates.DayLocator(interval=2))
            axis.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
            axis.grid(which="minor", axis="x", color="lightgray", linestyle="--", linewidth=1)
            xmin, xmax = axis.get_xlim()
            axis.set_xlim(xmin + 0.5, xmax - 0.5)
        plt.savefig(file_name + format)
        plt.close()
    except:
        pass
