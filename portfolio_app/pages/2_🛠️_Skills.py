import streamlit as st

st.title("🛠️ Skills Dashboard")


technical_skills = {
    "Python": 75,
    "JavaScript": 30,
    "PHP": 25
}

design_skills = {
    "UI/UX Design": 85,
    "Canva": 90
}

tools = ["GitHub", "VS Code", "Streamlit"]


st.markdown("## 💻 Technical Skills")

for skill, level in technical_skills.items():
    st.write(f"**{skill}**")
    st.progress(level)

st.markdown("---")


st.markdown("## 🎨 Design Skills")

for skill, level in design_skills.items():
    st.write(f"**{skill}**")
    st.progress(level)

st.markdown("---")


st.markdown("## ⚙️ Tools & Technologies")

col1, col2, col3 = st.columns(3)

for i, tool in enumerate(tools):
    if i % 3 == 0:
        col1.success(tool)
    elif i % 3 == 1:
        col2.success(tool)
    else:
        col3.success(tool)

st.markdown("---")

# 🔹 AUTO SKILL SCORE CALCULATION
all_skills = list(technical_skills.values()) + list(design_skills.values())
average = sum(all_skills) / len(all_skills)

st.markdown("## 📊 Overall Skill Rating")

st.progress(int(average))

st.info(f"Average Skill Level: {average:.1f}%")

if average >= 80:
    st.success("🔥 Excellent Developer Potential")
elif average >= 60:
    st.info("👍 Good Progress, Keep Improving")
else:
    st.warning("📈 Needs More Practice")

st.markdown("---")


st.markdown("## 🚀 Developer Mindset")

st.info("""
Consistent practice, real-world projects, and continuous learning
are the keys to becoming a successful developer.
""")