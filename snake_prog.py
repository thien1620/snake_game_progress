import streamlit as st

# Page Configuration
st.set_page_config(page_title="Game Update Progress", page_icon="🎮", layout="centered")

st.title('When is the next Snake Game UPDATE?')

st.link_button("In case you don't know what snake game is, click here to play",'https://thien162013.itch.io/snake-game')

with st.expander('Update 1.0'):
    st.write('Basically everything')
with st.expander('Update 1.1'):
    st.write('Gamemode bugfixes (100%)')
    st.progress(100)
    st.write('Some Small modifications(100%)')
    st.progress(100)
    st.success('Update 1.1 realeased!')
with st.expander('Update 1.2'):
    st.write('Achievements system (100%)')
    st.progress(100)
    st.write('Pause menu (100%)')
    st.progress(100)
    st.write('New gamemode (0%)')
    st.progress(0)
    st.info("Note: Doing quick progress by finshing the pause menu. Will continue to the new game mode soon. :)")

