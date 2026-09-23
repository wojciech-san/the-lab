import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page configuration (must be at the very top)
st.set_page_config(page_title="Personal Life Dashboard", layout="wide", initial_sidebar_state="expanded")

# --- MOCK DATA (for visualization) ---
if 'todos' not in st.session_state:
    st.session_state.todos = pd.DataFrame({
        "Completed": [False, True, False, False],
        "Task": ["Reply to emails", "Gym workout", "Analyze VGLA.DE ETF", "Go grocery shopping"],
        "Priority": ["Medium", "High", "Low", "Medium"]
    })

# --- SIDEBAR - DATA ENTRY ---
with st.sidebar:
    st.title("➕ Add entry")
    
    with st.expander("📝 New Task", expanded=True):
        with st.form("todo_form", clear_on_submit=True):
            new_task = st.text_input("Task description")
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            submit_todo = st.form_submit_button("Save task")
            
    with st.expander("💸 Add Expense"):
        with st.form("expense_form", clear_on_submit=True):
            amount = st.number_input("Amount (PLN)", min_value=0.0, step=10.0)
            category = st.selectbox("Category", ["Food", "Bills", "Entertainment", "Transport"])
            submit_expense = st.form_submit_button("Save expense")

    with st.expander("🏃‍♂️ Activity"):
        with st.form("sport_form", clear_on_submit=True):
            activity = st.selectbox("Type", ["Running", "Cycling", "Swimming"])
            distance = st.number_input("Distance (km)", min_value=0.0)
            submit_sport = st.form_submit_button("Add workout")
            
    st.markdown("---")
    st.subheader("🧠 Braindump")
    st.text_area("Quick notes (saved in the background)", height=150, placeholder="Write down thoughts, ideas...")


# --- MAIN SCREEN ---

# Header and weather (widgets at the top)
head_col1, head_col2 = st.columns([3, 1])
with head_col1:
    st.title(f"Welcome! Today is {datetime.now().strftime('%d.%m.%Y')}")
    st.markdown("*Your personal command center.*")
with head_col2:
    # Simulated weather widget
    st.info("🌤️ **Warsaw:** 18°C, Partly sunny\n\n🌧️ *Possible rain after 5:00 PM*")

st.markdown("---")

# Main three-column layout
col1, col2, col3 = st.columns(3)

# ----------------- COLUMN 1: AGENDA AND ALERTS -----------------
with col1:
    st.header("📅 Today's Agenda")
    st.markdown("""
    * **09:30** - Team meeting (Teams)
    * **13:00** - Lunch with client
    * **18:00** - 🎂 Birthday: Anna
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.header("⚠️ Important Bills")
    # Reminder table
    bills = pd.DataFrame({
        "Bill": ["Electricity", "Rent", "Internet"],
        "Amount": ["150 PLN", "2500 PLN", "70 PLN"],
        "Due": ["Today!", "Tomorrow", "In 4 days"]
    })
    st.dataframe(bills, use_container_width=True, hide_index=True)

# ----------------- COLUMN 2: ACTION (TASKS AND HABITS) -----------------
with col2:
    st.header("✅ Task List")
    # Interactive table for marking tasks as complete
    edited_df = st.data_editor(
        st.session_state.todos,
        column_config={
            "Completed": st.column_config.CheckboxColumn(
                "Completed?", help="Check when completed"
            )
        },
        disabled=["Task", "Priority"], # Text editing is disabled; only checkboxes can be changed
        hide_index=True,
        use_container_width=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.header("🎯 Habit Tracker")
    h_col1, h_col2, h_col3 = st.columns(3)
    with h_col1:
        st.checkbox("💧 2L of water")
    with h_col2:
        st.checkbox("📚 Reading")
    with h_col3:
        st.checkbox("🥦 No sugar")

# ----------------- COLUMN 3: HEALTH AND FINANCES -----------------
with col3:
    st.header("📈 Stocks / ETFs")
    # Use st.metric to display compact change indicators
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.metric(label="VGLA.DE", value="€112.40", delta="1.2% (Today)")
    with m_col2:
        st.metric(label="ETFPZUWORLD", value="108.50 PLN", delta="-0.5% (Today)")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.header("🚴‍♂️ Running Goal (Week)")
    st.progress(60, text="30 km / 50 km (60%)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.header("💰 Weekly Budget")
    st.progress(85, text="Spent: 850 PLN / 1000 PLN")
    if st.button("View expense details"):
        st.toast("The full history from the SQL database would open here!")