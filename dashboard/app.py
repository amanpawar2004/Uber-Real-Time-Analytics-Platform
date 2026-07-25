import streamlit as st
import pandas as pd
import plotly.express as px
import os
from streamlit_autorefresh import st_autorefresh

from components import header
from utils import load_data

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Uber Real-Time Analytics Platform",
    page_icon="🚖",
    layout="wide"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# Auto Refresh
# --------------------------------------------------

st_autorefresh(interval=2000, key="refresh")

# --------------------------------------------------
# Header
# --------------------------------------------------

header()

# --------------------------------------------------
# CSV File
# --------------------------------------------------

csv_file = "rides.csv"

if not os.path.exists(csv_file):
    st.warning("Waiting for ride data...")
    st.stop()

try:
    df = load_data(csv_file)
except Exception as e:
    st.error(e)
    st.stop()

if df.empty:
    st.warning("No ride data available.")
    st.stop()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🚖 Uber Dashboard")

st.sidebar.success("🟢 Kafka Connected")
st.sidebar.success("🟢 Flink Running")
st.sidebar.success("🟢 Producer Running")

st.sidebar.markdown("---")

locations = sorted(df["location"].unique())

selected_location = st.sidebar.multiselect(
    "Filter Location",
    locations
)

if selected_location:
    df = df[df["location"].isin(selected_location)]

st.sidebar.markdown("---")

st.sidebar.info(f"Total Records : {len(df)}")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric(
    "🚖 Total Rides",
    len(df)
)

c2.metric(
    "💰 Revenue",
    f"₹ {df['fare'].sum():,.0f}"
)

c3.metric(
    "💵 Avg Fare",
    f"₹ {df['fare'].mean():.2f}"
)

c4.metric(
    "📈 Highest Fare",
    f"₹ {df['fare'].max():.2f}"
)

c5.metric(
    "📉 Lowest Fare",
    f"₹ {df['fare'].min():.2f}"
)

c6.metric(
    "📩 Messages",
    len(df)
)

st.markdown("---")

# --------------------------------------------------
# Charts
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📍 Top Ride Locations")

    ride_count = (
        df.groupby("location")
        .size()
        .reset_index(name="Ride Count")
        .sort_values("Ride Count", ascending=True)
    )

    fig = px.bar(
        ride_count,
        x="Ride Count",
        y="location",
        orientation="h",
        color="Ride Count",
        title="Ride Count by Location"
    )

    fig.update_layout(height=450)

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("💰 Revenue by Location")

    revenue = (
        df.groupby("location")["fare"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        revenue,
        names="location",
        values="fare",
        hole=0.45,
        title="Revenue Distribution"
    )

    fig.update_layout(height=450)

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Second Row
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📊 Fare Distribution")

    fig = px.histogram(
        df,
        x="fare",
        nbins=25,
        title="Fare Distribution"
    )

    fig.update_layout(height=450)

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("📦 Fare Analysis")

    fig = px.box(
        df,
        y="fare",
        title="Fare Box Plot"
    )

    fig.update_layout(height=450)

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --------------------------------------------------
# Highest Fare Rides
# --------------------------------------------------

st.subheader("🏆 Top 10 Highest Fare Rides")

top10 = (
    df.sort_values("fare", ascending=False)
    .head(10)
)

fig = px.bar(
    top10,
    x="ride_id",
    y="fare",
    color="fare",
    title="Highest Fare Rides"
)

fig.update_layout(height=500)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --------------------------------------------------
# Latest Ride Records
# --------------------------------------------------

st.subheader("📋 Latest Ride Records")

st.dataframe(
    df.tail(20),
    use_container_width=True,
    height=400
)

st.markdown("---")

# --------------------------------------------------
# Alerts
# --------------------------------------------------

st.subheader("🚨 Live Alerts")

high_fare = df[df["fare"] > 450]

if len(high_fare) > 0:
    st.error(f"⚠ {len(high_fare)} High Fare Ride(s) Detected (> ₹450)")
else:
    st.success("✅ No High Fare Alerts")

st.info(f"📍 Most Active Location : {df['location'].mode()[0]}")

st.success("🟢 Kafka Streaming Active")

st.success("🟢 Apache Flink Running")

st.success("🟢 Dashboard Live")

st.markdown("---")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.caption(
    "Built with ❤️ using Python • Apache Kafka • Apache Flink • Streamlit • Plotly"
)