import streamlit as st
import webbrowser

st.header("My IoT WebApp")
door_button=st.radio('Door',['None','Unlock','Lock'])
if door_button == 'Unlock':
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=1&state=LOW')
elif door_button=='Lock': 
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=1&state=HIGH')

light1_button=st.radio('Light-1',['None','ON','OFF'])
if light1_button=='ON':
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=2&state=LOW')
elif light1_button=='OFF':
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=2&state=HIGH')

light2_button=st.radio('Light-2',['None','ON','OFF'])
if light2_button=='ON':
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=3&state=LOW')
elif light2_button=='OFF':
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=3&state=HIGH')

fan_button=st.radio('Fan',['None','ON','OFF'])
if fan_button=='ON':
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=4&state=LOW')
elif fan_button=='OFF':
    webbrowser.open_new_tab('https://cloud.boltiot.com/remote/3f24ffd2-78bf-467d-942e-4a74c9df06f9/digitalWrite?deviceName=BOLT992504&pin=4&state=HIGH')