from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="UX Insight Dashboard", page_icon="📊", layout="wide")
st.title("Dashboard Insight Pengalaman Pengguna")
st.caption("Study kasus HCI: memahami kepuasan dan kemudahan penggunaan aplikasi.")

df = pd.read_csv(Path(__file__).parent / "data" / "user_feedback.csv")
st.sidebar.header("Filter")
platforms = st.sidebar.multiselect("Platform", sorted(df["platform"].unique()), default=sorted(df["platform"].unique()))
filtered = df[df["platform"].isin(platforms)]

c1, c2, c3 = st.columns(3)
c1.metric("Jumlah responden", len(filtered))
c2.metric("Rata-rata kepuasan", f"{filtered['satisfaction'].mean():.2f}/5" if len(filtered) else "—")
c3.metric("Rata-rata kemudahan", f"{filtered['ease_of_use'].mean():.2f}/5" if len(filtered) else "—")

if filtered.empty:
    st.info("Pilih setidaknya satu platform.")
else:
    left, right = st.columns(2)
    with left:
        fig = px.histogram(filtered, x="satisfaction", color="platform", barmode="group",
                           title="Distribusi skor kepuasan", nbins=5)
        st.plotly_chart(fig, use_container_width=True)
    with right:
        fig = px.scatter(filtered, x="ease_of_use", y="satisfaction", color="platform",
                         hover_data=["respondent_id"], title="Kemudahan vs kepuasan")
        st.plotly_chart(fig, use_container_width=True)
    st.subheader("Data yang ditampilkan")
    st.dataframe(filtered, use_container_width=True)

st.markdown("**Prinsip HCI:** label jelas, filter terlihat, ringkasan metrik di atas, dan grafik memiliki judul.")
