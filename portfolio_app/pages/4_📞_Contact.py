import streamlit as st
import os

st.title("📞 Contact Me")

# ================= PROFILE HEADER =================
col1, col2 = st.columns([1, 2])

with col1:
    # Image path
    img_path = "portfolio_app/profile.jpg"

    if os.path.exists(img_path):
        st.image(img_path, width=180)
    else:
        st.warning("⚠ Image not found")

with col2:
    st.markdown("""
    ## 👋 Hello, I'm Marjun M. Briones  
    🎓 3rd Year Computer Science Student  
    🏫 DEBESMSCAT  
    💻 Aspiring Developer | 🎨 UI/UX Enthusiast | 🚀 Future Full Stack Developer  
    """)

st.markdown("---")

# ================= INTRO =================
st.markdown("""
### 💬 Let's Connect
If you have any questions, project ideas, or collaboration offers,
feel free to reach out.
""")

st.markdown("---")

# ================= CONTACT STYLE =================
st.markdown(
    """
    <style>
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #0e1117;
        border: 1px solid #262730;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================= CONTACT SECTION =================
col1, col2 = st.columns(2)

# -------- CONTACT FORM --------
with col1:
    st.markdown("## 💬 Send a Message")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit = st.form_submit_button("🚀 Send Message")

        if submit:
            if name and email and message:
                st.success("✅ Message sent successfully!")
                st.balloons()
            else:
                st.error("⚠ Please complete all fields.")

# -------- CONTACT INFO --------
with col2:
    st.markdown("## 📌 Contact Info")

    st.info("""
📍 Location: Philippines  
📧 Email: marjunmbriones@.com  
📱 Phone: +63 9297193032 
""")

    st.markdown("### 🌐 Social Links")

    st.link_button("🐙 GitHub", "https://github.com/marjunmbriones-afk")
    st.link_button("📘 Facebook", "https://facebook.com/marjunmbriones16")
    st.link_button("📧 Email Me", "mailto:marjunmbriones.com")

st.markdown("---")

# ================= FOOTER =================
st.markdown(
    """
    <div style="text-align:center; color:gray;">
        🚀 Built with Streamlit | © 2026 Marjun Briones Portfolio
    </div>
    """,
    unsafe_allow_html=True
)

