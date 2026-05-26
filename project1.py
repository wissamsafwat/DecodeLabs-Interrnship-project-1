import pandas as pd


df = pd.read_excel("data_set.xlsx")

print("--- Dataset Structure ---")
print(df.info())

print("\n--- Missing Values Count ---")
print(df.isnull().sum())

mode_coupon = df['CouponCode'].mode()[0]
df['CouponCode'] = df['CouponCode'].fillna(mode_coupon)

print("--- printfing after fix ---")
print(df.isnull().sum())

duplicate_cnt = df.duplicated(subset=['OrderID']).sum()
if duplicate_cnt > 0:
    df.drop_duplicates(subset=['OrderID'], inplace=True , keep="first")
print(f"--- duplicates found = {duplicate_cnt}---")

df['Date'] = pd.to_datetime(df['Date'] , errors='coerce').dt.strftime('%Y-%m-%d')

print("--- fixed date foramt ---")
print(df['Date'].head())
print(df['Date'].tail())

df.to_excel("cleaned data set.xlsx", index=False)