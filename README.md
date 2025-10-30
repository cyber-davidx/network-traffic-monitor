# Network Traffic Monitor

Simple, local network traffic monitor built with Python and Streamlit.  
Shows upload/download speeds, total bytes, and active connections. Designed for learning and small-lab use — not for production.

---

## Project overview

**Objective:** Build an interactive tool that shows your machine's network I/O in (near) real time using `psutil` for stats and `streamlit` for the UI.

**What it teaches:**
- Reading system metrics with `psutil`
- Basic Streamlit UI (title, metrics, charts, sidebar)
- Persisting state across Streamlit reruns with `st.session_state`
- Converting cumulative counters into speeds (bytes/sec)
- Simple data visualization with `pandas` + `st.line_chart`

---

## Features
- Select interface (Overall or specific NIC)
- Upload / Download speeds (B/s)
- Total bytes sent / received since boot
- Short history buffer and live chart of recent samples
- Active remote IPs table (top peers)
- Simple Live toggle (manual or autorefresh optional)

---

## Files in this repo
- `app.py` — main Streamlit app (single-file version; run this)
- `requirements.txt` — (optional) pinned dependencies
- `README.md` — this file
- `venv/` — local virtual environment **(do not commit to GitHub)**

If you split helpers, you may also see:
- `utils.py` — helper functions (optional)

---

## Quick setup (macOS / Linux / Git Bash)

Open a terminal then:

```bash
# 1. go to your projects folder
cd ~/Documents/coding/network_traffic_monitor

# 2. create virtual env (only once)
python3 -m venv venv

# 3. activate venv
source venv/bin/activate

# 4. install packages
pip install streamlit psutil pandas

# optionally save deps
pip freeze > requirements.txt

# 5. run app
streamlit run app.py
