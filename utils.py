# 檔案名稱：utils.py
import streamlit as st

def get_gmap_link(query, mode="transit"):
    # mode: driving (開車), walking (走路), transit (大眾運輸)
    base_url = "https://www.google.com/maps/dir/?api=1"
    return f"{base_url}&destination={query}&travelmode={mode}"
