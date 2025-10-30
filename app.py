import time
import streamlit as st
import psutil


st.title('Network Traffic Monitor')

if 'prev_counters' not in st.session_state:
    st.session_state.prev_counters = psutil.net_io_counters()
    st.session_state.prev_time = time.time()
    st.session_state.up_bps = 0.0
    st.session_state.down_bps = 0.0

cur = psutil.net_io_counters()
now = time.time()

elasped = now - st.session_state.prev_time
if elasped <= 0:
    elasped = 0.1


cur_bytes_sent = cur.bytes_sent
cur_bytes_recv = cur.bytes_recv
prev_bytes_sent = st.session_state.prev_counters.bytes_sent
prev_bytes_recv = st.session_state.prev_counters.bytes_recv

delta_sent = cur_bytes_sent - prev_bytes_sent
delta_recv = cur_bytes_recv - prev_bytes_recv


up_bps = max(0.0, delta_sent / elasped)
down_bps = max(0.0, delta_recv / elasped)


st.session_state.up_bps = up_bps
st.session_state.down_bps = down_bps
st.session_state.prev_counters = cur
st.session_state.prev_time = now


st.write('upload', f'{up_bps:2f}B/s')
st.write('download', f'[down_bps:2f]B/s')

time.sleep(1)
st.rerun
