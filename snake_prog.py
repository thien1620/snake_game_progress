import streamlit as st

# Page Configuration
st.set_page_config(page_title="Game Update Progress", page_icon="🎮", layout="centered")

st.title('When is the next Snake Game UPDATE?')

st.link_button("Play update 1.2 right now!",'https://thien162013.itch.io/snake-game')

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
    st.write('New menu screen (100%)')
    st.progress(100)
    st.write('Update 1.2.1 - Added some tweaks to achievements page')
    st.success("Update 1.2 is realeased!")
    st.balloons()
with st.expander('Update 1.3'):
    st.write("Menu logic enhancements (50%)")
    st.progress(50)
    st.write('Snake customization (0%)')
    st.progress(0)
    st.write('Background customization (0%)')
    st.progress(0)
    st.info('Paused development because of studing. Wii come back to development next week.')
