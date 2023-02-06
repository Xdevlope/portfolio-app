# import
from pathlib import Path
import requests
from bokeh.models.widgets import Div
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#  path setting
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# GENERAL SETTINGS
PAGE_TITLE = "Portfolio| Mehdi Ridmani"
PAGE_ICON = ":wave:"
NAME = "Mehdi Ridmani"
DESCRIPTION = """
Full stack , WordPress Developer.
"""
EMAIL = "mehdiridmani@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mehdi-ridmani-109284248/",
    "GitHub": "https://github.com/EL-Mehdiri",
    "Instagram": "https://www.instagram.com/mehdi_ridmani/",
}


st.set_page_config(page_title=PAGE_TITLE,
                   page_icon=PAGE_ICON,   layout="wide",)

# load css, pdf, profil pic

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # st.download_button(
    #     label="Download Resume",
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime="application/octet-stream",
    # )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages
            - Python, JavaScript, HTML, CSS
            Frameworks
            - Tailwind, Bootstrap
            Databases
            - MySQL,
            Hosting & Cloud
            - Streamlit Cloud 😉
            Miscellaneous
            - Git, Github,
             """
        )

    with col2:
        st_lottie(
            load_lottieurl(
                "https://assets7.lottiefiles.com/packages/lf20_rRHO95QOkl.json"),
            height=500,
        )
# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("PRODUCT MANAGEMENT SYSTEM")
        st.write(
            "")
        if st.button('Enter App', key="ews_enter"):
            # New tab or window
            js = "window.open('https://el-mehdiri.github.io/PRODUCT-MANAGEMENT-SYSTEM/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="ews_github"):
            st.write('Github opens in new browser tab')
            # New tab or window
            js = "window.open('https://github.com/EL-Mehdiri/PRODUCT-MANAGEMENT-SYSTEM')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col2:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Iphone landing page")
        st.write(
            "")
        if st.button('Enter App', key="gee_enter"):
            # New tab or window
            js = "window.open('https://el-mehdiri.github.io/Iphone-landing-page/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="gee_github"):
            st.write('Github opens in new browser tab')
            # New tab or window
            js = "window.open('https://github.com/EL-Mehdiri/Iphone-landing-page')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col3:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("X-O GAME")
        st.write(
            "")
        if st.button('Enter App', key="cbw_enter"):
            # New tab or window
            js = "window.open('https://el-mehdiri.github.io/X-O_GAME/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="ccw_github"):
            st.write('Github opens in new browser tab')
            # New tab or window
            js = "window.open('https://github.com/EL-Mehdiri/X-O_GAME')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Check Internet Connection")
        st.write("")
        if st.button('Enter App', key="ess_enter"):
            # New tab or window
            js = "window.open('https://el-mehdiri.github.io/Check-Internet-Connection/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="qrc_github"):
            st.write('Github opens in new browser tab')
            # New tab or window
            js = "window.open('https://github.com/EL-Mehdiri/Check-Internet-Connection')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col5:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Landing Page")
        st.write("website made with HTML/css.")
        if st.button('Enter App', key="eas_enter"):
            # New tab or window
            js = "window.open('https://el-mehdiri.github.io/Omnifood-1-main/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="spw_github"):
            st.write('Github opens in new browser tab')
            # New tab or window
            js = "window.open('https://github.com/EL-Mehdiri/Omnifood-1-main')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col6:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Clock")
        st.write("")
        if st.button('Github', key="bpw_github"):
            # New tab or window
            js = "window.open('https://github.com/EL-Mehdiri/Clockjs')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


# --- CONTACT ---
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Contact</h2>",
                unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/805cc992f02da35ae356f2451ece18be" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)


with st.container():
    for i in range(8):
        st.write("##")
    # st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.caption('Made in 2023 with ❤, _By_ :blue[MEHDI RIDMANI]')
    st.write("---")
