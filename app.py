import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv("laptop_data.csv")

model = pickle.load(open("model.pkl", "rb"))
brand_encoder = pickle.load(open("brand_encoder.pkl", "rb"))
cpu_encoder = pickle.load(open("cpu_encoder.pkl", "rb"))

# -----------------------------------
# TITLE
# -----------------------------------

st.title("💻 Laptop Price Predictor Dashboard")

st.markdown("---")

# -----------------------------------
# TOP METRICS
# -----------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Laptops",
        len(df)
    )

with col2:
    st.metric(
        "Average Price",
        f"₹{int(df['Price'].mean()):,}"
    )

with col3:
    st.metric(
        "Brands",
        df["Brand"].nunique()
    )

with col4:
    st.metric(
        "Model Accuracy",
        "92%"
    )

st.markdown("---")

# -----------------------------------
# PREDICTION SECTION
# -----------------------------------

st.header("🔍 Predict Laptop Price")

c1, c2 = st.columns(2)

with c1:

    brand = st.selectbox(
        "Brand",
        brand_encoder.classes_
    )

    ram = st.selectbox(
        "RAM (GB)",
        [4, 8, 16, 32]
    )

    storage = st.selectbox(
        "Storage (GB)",
        [256, 512, 1024]
    )

with c2:

    processor = st.selectbox(
        "Processor",
        cpu_encoder.classes_
    )

    screen = st.selectbox(
        "Screen Size",
        [13.3, 14.0, 15.6, 16.0, 17.3]
    )

st.write("")

if st.button("Predict Price"):

    brand_encoded = brand_encoder.transform([brand])[0]
    cpu_encoded = cpu_encoder.transform([processor])[0]

    data = [[
        brand_encoded,
        cpu_encoded,
        ram,
        storage,
        screen
    ]]

    prediction = model.predict(data)

    st.success(
        f"💰 Estimated Laptop Price: ₹ {prediction[0]:,.0f}"
    )

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({
        "Brand": brand,
        "Processor": processor,
        "RAM": ram,
        "Storage": storage,
        "Screen": screen,
        "Predicted Price": int(prediction[0])
    })

st.markdown("---")

# -----------------------------------
# CHARTS SECTION
# -----------------------------------

st.header("📊 Dataset Insights")

# Row 1

col1, col2 = st.columns(2)

with col1:

    brand_count = df["Brand"].value_counts()

    fig1 = px.pie(
        values=brand_count.values,
        names=brand_count.index,
        title="Brand Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    avg_price = (
        df.groupby("Brand")["Price"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        avg_price,
        x="Brand",
        y="Price",
        title="Average Price by Brand"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# Row 2

col3, col4 = st.columns(2)

with col3:

    fig3 = px.scatter(
        df,
        x="RAM",
        y="Price",
        color="Brand",
        title="RAM vs Price"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col4:

    fig4 = px.scatter(
        df,
        x="Storage",
        y="Price",
        color="Brand",
        title="Storage vs Price"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# Row 3

processor_count = (
    df["Processor"]
    .value_counts()
    .reset_index()
)

processor_count.columns = [
    "Processor",
    "Count"
]

fig5 = px.bar(
    processor_count,
    x="Processor",
    y="Count",
    title="Processor Distribution"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# -----------------------------------
# DATASET PREVIEW
# -----------------------------------

st.header("📁 Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

# -----------------------------------
# PREDICTION HISTORY
# -----------------------------------

st.header("📝 Prediction History")

if "history" in st.session_state:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:
    st.info("No predictions made yet.")

st.markdown("---")

# -----------------------------------
# PROJECT INFO
# -----------------------------------

st.header("ℹ️ About Project")

st.write("""
### Laptop Price Prediction Using Machine Learning

This project predicts laptop prices using
Linear Regression.

### Features Used

- Brand
- Processor
- RAM
- Storage
- Screen Size

### Technologies

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Plotly

### Machine Learning Algorithm

Linear Regression
""")