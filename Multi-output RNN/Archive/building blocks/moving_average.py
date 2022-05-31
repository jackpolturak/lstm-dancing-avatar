from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt



main_df = pd.DataFrame()
dataset = "/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Pose data/CSVs/data.csv"
df = pd.read_csv(dataset)

if len(main_df) == 0:
    main_df = df
else:
    main_df = main_df.join(df)


rolling = main_df.rolling(window=5)
rolling_mean = rolling.mean()
rolling_mean.dropna(inplace=True)
print(rolling_mean.head(10))
print(main_df.head(10))

rolling_mean.to_csv("/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Multi-output RNN/movin g_av_csv/data.csv")



plt.title("Applying a Moving Average Filter to Features")
plt.xlabel("Frame number")
plt.ylabel(" Joint position")

plt.plot(main_df['LEFT_WRIST_y'], label="Left wrist y")
plt.plot(rolling_mean['LEFT_WRIST_y'], label="Left wrist y with moving average filter")
plt.legend()
plt.show()