import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("World Cities — Home")
st.markdown(
    """
    Welcome to the World Cities Streamlit app.
    
    This page serves as the entry point. Click the button below to open the app page (app.py) located in the `pages/` folder.
    """
)

def go_to_page(page_name: str):
    # Preferred: use query params to switch Streamlit pages (page name is usually the file name capitalized, e.g. "App")
    try:
        st.experimental_set_query_params(page=page_name)
        st.experimental_rerun()
    except Exception:
        # Fallback: show a link that sets the query param in the URL
        app_link = f"?page={quote(page_name)}"
        st.markdown(f"[Open {page_name}]({app_link})")

if st.button("Open App"):
    # Try the page name Streamlit will display for pages/app.py (usually "App")
    go_to_page("App")

# Always provide a manual link as a fallback for users or Streamlit versions that behave differently
st.markdown("If the button doesn't work, open the app page from the sidebar or click the link below:")
st.markdown("[Open App](?page=App)")
