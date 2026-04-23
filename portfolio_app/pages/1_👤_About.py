import streamlit as st

st.title("👤 About Me")

# 🔹 PROFILE HEADER (IMAGE + INTRO)
col1, col2 = st.columns([1, 2])

with col1:
    st.image("portfolio_app/marjun", width=180)

with col2:
    st.markdown("""
    ## 👋 Hello, I'm Marjun M. Briones
    🎓 3rd Year Computer Science Student  
    🏫 DEBESMSCAT  
    💻 Aspiring Developer | 🎨 UI/UX Enthusiast | 🚀 Future Full Stack Developer  
    """)

st.markdown("---")

# 🔹 ABOUT CARD SECTION
st.markdown("## 🧾 Profile Summary")

st.info("""
I am a passionate Computer Science student who enjoys building systems,
designing user-friendly interfaces, and exploring modern technologies.

I aim to improve my programming skills and develop real-world applications
that can help solve problems efficiently.
""")

st.markdown("---")

# 🔹 EDUCATION + GOALS
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎓 Education")
    st.write("📘 Bachelor of Science in Computer Science")
    st.write("🏫 DEBESMSCAT")
    st.write("📍 Philippines")

with col2:
    st.subheader("🎯 Goals")
    st.write("✔ Become a skilled Software Developer")
    st.write("✔ Build real-world applications")
    st.write("✔ Improve UI/UX design skills")
    st.write("✔ Create my own tech projects")

st.markdown("---")

# 🔹 INTERACTIVE INTERESTS
st.subheader("💡 Interests")

interest = st.selectbox(
    "Choose what I love most:",
    ["Programming", "Web Development", "UI/UX Design", "Database Systems", "Artificial Intelligence"]
)

st.success(f"💡 You selected: {interest}")

# 🔹 FUN BUTTON (EXTRA TOUCH)
if st.button("✨ Show Motivation"):
    st.balloons()
    st.success("Keep learning, keep building, and never stop improving! 🚀")
