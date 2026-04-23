import streamlit as st
import os

st.set_page_config(page_title="Home", layout="wide")

col1, col2 = st.columns([1, 2])

with col1:
    # ✅ FIXED PATH (IMPORTANT)
    img_path = "portfolio_app/jun.jpg"

    if os.path.exists(img_path):
        st.image(img_path, width=180)
    else:
        st.warning("⚠ Image not found. Check file path.")

with col2:
    st.markdown("""
    # 👋 Hi, I'm Marjun M. Briones  
    ### 💻 Aspiring Developer | 🎨 UI/UX Enthusiast | 🚀 Future Full Stack Developer  

    I love building simple, useful, and user-friendly systems using Python and Streamlit.
    """)

st.markdown("---")

st.markdown("## ✨ About Me")

st.info("""
I am a Computer Science student passionate about technology, problem-solving,
and creating digital solutions that make life easier.
""")

col1, col2, col3 = st.columns(3)

col1.metric("💼 Projects", "5+")
col2.metric("🧠 Skills", "10+")
col3.metric("📚 Learning", "Daily")

st.markdown("---")

st.markdown("## 🚀 What I Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("💻 Programming\n\nBuilding systems using Python")

with col2:
    st.success("🎨 UI/UX Design\n\nDesigning clean interfaces")

with col3:
    st.success("🌐 Web Apps\n\nCreating Streamlit applications")

st.markdown("---")

st.markdown("## 🔗 Connect With Me")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🐙 GitHub", "https://github.com/marjunmbriones-afk")

with col2:
    st.link_button("📘 Facebook", "https://www.facebook.com/marjunmbriones16")

with col3:
    st.link_button("📧 Email", "mailto:marjunmbriones@gmail.com")

st.markdown("---")
st.markdown("---")
