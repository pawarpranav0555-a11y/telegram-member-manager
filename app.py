import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Telegram Member Manager",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Telegram Member Manager")
st.caption("937 Contacts | Consent & Join Tracking")

file = st.file_uploader("Upload contacts CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.success(f"एकूण {len(df)} नोंदी अपलोड झाल्या.")

    column = st.selectbox("Mobile number column निवडा", df.columns)

    df["Consent Confirmed"] = False
    df["Telegram Joined"] = False
    df["Notes"] = ""

    st.subheader("Contact Records")
    edited = st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic"
    )

    st.download_button(
        "⬇️ Download Updated CSV",
        edited.to_csv(index=False).encode("utf-8"),
        "telegram_member_tracker.csv",
        "text/csv"
    )

    st.metric("Total Contacts", len(edited))
    st.metric(
        "Consent Confirmed",
        int(edited["Consent Confirmed"].sum())
    )
    st.metric(
        "Joined Channel",
        int(edited["Telegram Joined"].sum())
    )
else:
    st.info("सुरुवात करण्यासाठी आपली CSV फाइल अपलोड करा.")
