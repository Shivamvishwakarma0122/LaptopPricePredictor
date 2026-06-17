import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("laptop_data.csv")

brand_encoder = LabelEncoder()
cpu_encoder = LabelEncoder()

df["Brand"] = brand_encoder.fit_transform(df["Brand"])
df["Processor"] = cpu_encoder.fit_transform(df["Processor"])

X = df[
    [
        "Brand",
        "Processor",
        "RAM",
        "Storage",
        "ScreenSize"
    ]
]

y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, pred))

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(brand_encoder, open("brand_encoder.pkl", "wb"))
pickle.dump(cpu_encoder, open("cpu_encoder.pkl", "wb"))

print("Model Saved Successfully")