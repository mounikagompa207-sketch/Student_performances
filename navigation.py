import streamlit as st


def navigation():

    st.sidebar.markdown("## 🔄 Switch Pages")

    pages = {
        "🏠 Home": "pages/home.py",
        "➕ Add Student": "pages/add_student.py",
        "📊 Dashboard": "pages/dashboard.py",
        "🎯 Goal Planner": "pages/goal_planner.py",
        "🤖 Prediction": "pages/prediction.py",
        "📄 Reports": "pages/reports.py",
        "👥 View Students": "pages/view_students.py",
        "✏️ Update/Delete": "pages/update_delete.py",
        "🎤 Voice": "pages/voice.py",
        "😊 Mood": "pages/mood.py",
        "🚪 Logout": "pages/logout.py"
    }


    selected = st.sidebar.selectbox(
        "Go to",
        list(pages.keys())
    )


    if st.sidebar.button("Open Page"):

        st.switch_page(
            pages[selected]
        )