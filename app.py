import streamlit as st
import pandas as pd


# Page Config

st.set_page_config(page_title=" RailAI Smart Scheduler", page_icon="🚆")

st.title("🚆RailAI Smart Scheduler")


# Session State (to store trains)

if "trains" not in st.session_state:
    st.session_state.trains = [
    {"train_no": "12001", "name": "Shatabdi Express", "source": "Delhi", "destination": "Chandigarh", "departure": "06:00", "arrival": "09:30"},
    {"train_no": "12002", "name": "Shatabdi Express", "source": "Chandigarh", "destination": "Delhi", "departure": "17:00", "arrival": "20:30"},

    {"train_no": "12951", "name": "Rajdhani Express", "source": "Mumbai", "destination": "Delhi", "departure": "16:30", "arrival": "08:00"},
    {"train_no": "12952", "name": "Rajdhani Express", "source": "Delhi", "destination": "Mumbai", "departure": "16:55", "arrival": "08:35"},

    {"train_no": "12311", "name": "Howrah Mail", "source": "Delhi", "destination": "Kolkata", "departure": "21:00", "arrival": "10:00"},
    {"train_no": "12312", "name": "Howrah Mail", "source": "Kolkata", "destination": "Delhi", "departure": "19:40", "arrival": "08:15"},

    {"train_no": "12627", "name": "Karnataka Express", "source": "Bangalore", "destination": "Delhi", "departure": "19:20", "arrival": "10:30"},
    {"train_no": "12628", "name": "Karnataka Express", "source": "Delhi", "destination": "Bangalore", "departure": "20:00", "arrival": "11:30"},

    {"train_no": "12137", "name": "Punjab Mail", "source": "Mumbai", "destination": "Firozpur", "departure": "19:35", "arrival": "07:45"},
    {"train_no": "12138", "name": "Punjab Mail", "source": "Firozpur", "destination": "Mumbai", "departure": "21:40", "arrival": "10:30"},

    {"train_no": "12259", "name": "Duronto Express", "source": "Delhi", "destination": "Sealdah", "departure": "19:55", "arrival": "10:40"},
    {"train_no": "12260", "name": "Duronto Express", "source": "Sealdah", "destination": "Delhi", "departure": "13:45", "arrival": "06:35"},

    {"train_no": "12423", "name": "Dibrugarh Rajdhani", "source": "Delhi", "destination": "Dibrugarh", "departure": "21:25", "arrival": "07:40"},
    {"train_no": "12424", "name": "Dibrugarh Rajdhani", "source": "Dibrugarh", "destination": "Delhi", "departure": "20:35", "arrival": "06:20"},

    {"train_no": "12615", "name": "Grand Trunk Express", "source": "Chennai", "destination": "Delhi", "departure": "18:40", "arrival": "06:55"},
    {"train_no": "12616", "name": "Grand Trunk Express", "source": "Delhi", "destination": "Chennai", "departure": "18:10", "arrival": "06:35"},

    {"train_no": "12801", "name": "Purushottam Express", "source": "Puri", "destination": "Delhi", "departure": "21:30", "arrival": "07:00"},
    {"train_no": "12802", "name": "Purushottam Express", "source": "Delhi", "destination": "Puri", "departure": "22:15", "arrival": "06:00"},

    {"train_no": "11057", "name": "Amritsar Express", "source": "Mumbai", "destination": "Amritsar", "departure": "23:00", "arrival": "13:30"},
    {"train_no": "11058", "name": "Amritsar Express", "source": "Amritsar", "destination": "Mumbai", "departure": "08:30", "arrival": "23:20"},

    {"train_no": "12555", "name": "Gorakhdham Express", "source": "Delhi", "destination": "Gorakhpur", "departure": "20:10", "arrival": "09:50"},
    {"train_no": "12556", "name": "Gorakhdham Express", "source": "Gorakhpur", "destination": "Delhi", "departure": "16:35", "arrival": "05:30"},

    {"train_no": "12217", "name": "Kerala Sampark Kranti", "source": "Chandigarh", "destination": "Kochi", "departure": "06:50", "arrival": "15:15"},
    {"train_no": "12218", "name": "Kerala Sampark Kranti", "source": "Kochi", "destination": "Chandigarh", "departure": "12:00", "arrival": "20:00"},

    {"train_no": "12925", "name": "Paschim Express", "source": "Mumbai", "destination": "Amritsar", "departure": "11:25", "arrival": "19:20"},
    {"train_no": "12926", "name": "Paschim Express", "source": "Amritsar", "destination": "Mumbai", "departure": "08:10", "arrival": "15:50"},

    {"train_no": "12459", "name": "Shiv Ganga Express", "source": "Varanasi", "destination": "Delhi", "departure": "20:00", "arrival": "08:10"},
    {"train_no": "12460", "name": "Shiv Ganga Express", "source": "Delhi", "destination": "Varanasi", "departure": "18:55", "arrival": "07:20"},

    {"train_no": "12723", "name": "Telangana Express", "source": "Hyderabad", "destination": "Delhi", "departure": "06:00", "arrival": "07:00"},
    {"train_no": "12724", "name": "Telangana Express", "source": "Delhi", "destination": "Hyderabad", "departure": "15:00", "arrival": "16:30"}
]
# Convert to DataFrame
df = pd.DataFrame(st.session_state.trains)


# Sidebar Menu

menu = st.sidebar.selectbox("Menu", [
    "Show All Trains",
    "Search Train",
    "Search by Train Number",
    "Add Train",
    "Delete Train",
    "Sort Trains"
])


# Show All Trains

if menu == "Show All Trains":
    st.subheader("🚆 Available Trains")
    st.dataframe(df)


# Search Train (Source → Destination)

elif menu == "Search Train":
    st.subheader("🔍 Search Train")

    src = st.text_input("Enter Source")
    dest = st.text_input("Enter Destination")

    if st.button("Search"):
        result = df[
            (df["source"].str.lower() == src.lower()) &
            (df["destination"].str.lower() == dest.lower())
        ]

        if not result.empty:
            st.success("✅ Trains Found")
            st.dataframe(result)
        else:
            st.error("❌ No trains found")


# Search by Train Number

elif menu == "Search by Train Number":
    st.subheader("🔎 Search by Train Number")

    num = st.text_input("Enter Train Number")

    if st.button("Search"):
        result = df[df["train_no"] == num]

        if not result.empty:
            st.success("✅ Train Found")
            st.dataframe(result)
        else:
            st.error("❌ Train not found")

# Add Train

elif menu == "Add Train":
    st.subheader("➕ Add New Train")

    train_no = st.text_input("Train Number")
    name = st.text_input("Train Name")
    source = st.text_input("Source")
    destination = st.text_input("Destination")
    departure = st.text_input("Departure Time (HH:MM)")
    arrival = st.text_input("Arrival Time (HH:MM)")

    if st.button("Add Train"):
        st.session_state.trains.append({
            "train_no": train_no,
            "name": name,
            "source": source,
            "destination": destination,
            "departure": departure,
            "arrival": arrival
        })
        st.success("✅ Train Added Successfully")


# Delete Train

elif menu == "Delete Train":
    st.subheader("❌ Delete Train")

    num = st.text_input("Enter Train Number to Delete")

    if st.button("Delete"):
        original_len = len(st.session_state.trains)
        st.session_state.trains = [
            t for t in st.session_state.trains if t["train_no"] != num
        ]

        if len(st.session_state.trains) < original_len:
            st.success("✅ Train Deleted")
        else:
            st.error("❌ Train not found")


# Sort Trains

elif menu == "Sort Trains":
    st.subheader("⏰ Sort by Departure Time")

    sorted_df = df.sort_values(by="departure")
    st.dataframe(sorted_df)
