import streamlit as st

# Define bus stop lists
bus_1_stops = [1, 3, 6, 7, 9, 12, 14, 17, 19, 20, 23, 25, 27, 28, 30]
bus_2_stops = [1, 2, 8, 10, 12, 16, 19, 23, 27, 29, 30]
bus_3_stops = [1, 3, 9, 11, 14, 15, 18, 21, 24, 26, 28, 30]

# Define bus speeds in mph
bus_speeds = {
    'Bus 1': 22,
    'Bus 2': 30,
    'Bus 3': 25,
}

# Create a function to calculate ETA
def calculate_eta(destination):
    eta_data = {}
    for bus, stops in zip(bus_speeds.keys(), [bus_1_stops, bus_2_stops, bus_3_stops]):
        if destination in stops:
            distance = abs(stops.index(destination) - stops.index(stops[0]))
            speed = bus_speeds[bus]
            eta = distance / speed
            eta_data[bus] = eta
    return eta_data

st.title('Bus ETA and Best Bus Checker')

# User input for the bus stop
# destination = st.text_input('Enter your destination bus stop:') ##
destination = st.selectbox('Select a destination from 1 to 30', list(range(1, 31)))
show_traffic = st.checkbox('Show Traffic Info')

# Calculate ETA for each bus
eta_data = calculate_eta(int(destination))

# Determine the best bus based on ETA to the destination
best_bus = None
min_eta = float('inf')

for bus, eta in eta_data.items():
    if eta < min_eta:
        best_bus = bus
        min_eta = eta

# Display ETA for each bus
st.subheader('Bus Arrival Times:')
for bus, eta in eta_data.items():
    st.write(f'{bus}: ETA {eta:.2f} minutes')

# Display the best bus to the destination
if best_bus:
    st.subheader(f'Best Bus to Stop {destination}: {best_bus}')
else:
    st.subheader(f'No bus is currently heading to Stop {destination}.')

# Display traffic or breakdown information (simulated)
if show_traffic:
    st.subheader('Traffic Information:')
    st.write("No traffic incidents reported.")
else:
    st.subheader('Bus Breakdown Information:')
    st.write("No bus breakdowns reported.")

# Add a footer
st.write('Bhushan\'s MLH transport hacks submission')
