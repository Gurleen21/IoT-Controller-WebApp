import streamlit as st
import webbrowser

st.header("My IoT WebApp")

st.subheader("Door")
door_button_unlock=st.button('Unlock',key=1)
if door_button_unlock:
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=1&state=LOW')
door_button_lock=st.button('Lock',key=2)
if door_button_lock: 
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=1&state=HIGH')

st.subheader("Light-1")
light1_button_on=st.button('ON',key=3)
if light1_button_on:
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=2&state=LOW')
light1_button_off=st.button('OFF',key=4)
if light1_button_off:
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=2&state=HIGH')

st.subheader('Light-2')
light2_button_on=st.button('ON',key=5)
if light2_button_on:
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=3&state=LOW')
light2_button_off=st.button('OFF',key=6)
if light2_button_off:
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=3&state=HIGH')

st.subheader('Fan')
fan_button_on=st.button('ON',key=7)
if fan_button_on:
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=4&state=LOW')
fan_button_off=st.button('OFF',key=8)
if fan_button_off:
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=4&state=HIGH')