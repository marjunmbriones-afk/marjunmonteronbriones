import streamlit as st

st.title("📂 Projects Dashboard")

projects = [
    {
        "title": "E-Attendance System",
        "desc": "Tracks student attendance and generates reports automatically.",
        "category": "System",
        "status": "Completed"
    },
    {
        "title": "Story-telling Web App",
        "desc": "A web platform that provides different stories to the viewers.",
        "category": "Web",
        "status": "In Progress"
    },
    {
        "title": "Banking System",
        "desc": "Handles transactions and displays financial analytics.",
        "category": "System",
        "status": "Completed"
    },
]

total = len(projects)
completed = len([p for p in projects if p["status"] == "Completed"])
ongoing = total - completed

col1, col2, col3 = st.columns(3)

col1.metric("📌 Total Projects", total)
col2.metric("✔ Completed", completed)
col3.metric("🚧 Ongoing", ongoing)

st.markdown("---")

categories = ["All", "System", "Web"]
selected = st.selectbox("Filter by Category:", categories)

st.markdown("---")

filtered_projects = [
    p for p in projects
    if selected == "All" or p["category"] == selected
]

for project in filtered_projects:

    st.markdown(f"## 📌 {project['title']}")

    if project["status"] == "Completed":
        st.success("Status: Completed ✔")
    else:
        st.warning("Status: In Progress 🚧")

    st.write(project["desc"])
    st.caption(f"Category: {project['category']}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 View Details", key=f"view_{project['title']}"):
            st.info(f"More details about '{project['title']}' will be added soon.")

    with col2:
        if st.button("❤️ Like", key=f"like_{project['title']}"):
            st.success("Thanks for liking this project! 🚀")

    st.markdown("---")

st.subheader("➕ Add New Project")

with st.form("add_project_form"):
    name = st.text_input("Project Name")
    desc = st.text_area("Project Description")
    category = st.selectbox("Category", ["System", "Web", "Design"])
    status = st.selectbox("Status", ["Completed", "In Progress"])

    submit = st.form_submit_button("Add Project")

    if submit:
        if name and desc:
            st.success(f"✅ Project '{name}' added successfully!")
        else:
            st.error("⚠ Please complete all fields.")