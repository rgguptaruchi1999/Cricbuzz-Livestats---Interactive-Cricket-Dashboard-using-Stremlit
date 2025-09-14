import streamlit as st
import sqlite3
from pathlib import Path
import pandas as pd

# Connect to DB
db_path = Path(__file__).parent / "cricbuzz.db"
conn = sqlite3.connect(db_path)

st.set_page_config(page_title="🏏 Cricbuzz Dashboard", layout="wide")
st.title("🏏 Cricbuzz Live Stats App")
st.write("Welcome to the Cricbuzz analytics demo app!")

# Show Players
st.subheader("👥 Players")
players = pd.read_sql("SELECT * FROM players", conn)
st.dataframe(players)

# Show Teams
st.subheader("🏏 Teams")
teams = pd.read_sql("SELECT * FROM teams", conn)
st.dataframe(teams)

# Show Venues
st.subheader("🏟 Venues")
venues = pd.read_sql("SELECT * FROM venues", conn)
st.dataframe(venues)

conn.close()
