import streamlit as st

# Set page config
st.set_page_config(page_title="Mini Netflix Demo", layout="wide")

# Header section
st.markdown("""
    <h1 style='text-align: center; color: red;'>Mini Netflix</h1>
    <p style='text-align: center;'>Watch your favourite movies and shows</p>
""", unsafe_allow_html=True)

# Search bar
search = st.text_input("Search for movies...", "")

st.write("---")

# Fake movie data
movies = [
    {"title": "Stranger Things", "img": "https://i.imgur.com/5Z6w8C9.jpg"},
    {"title": "Money Heist", "img": "https://i.imgur.com/VDfB8Qz.jpg"},
    {"title": "Wednesday", "img": "https://i.imgur.com/Wv1Fcss.jpg"},
    {"title": "The Witcher", "img": "https://i.imgur.com/gE4n6Q2.jpg"},
    {"title": "Dark", "img": "https://i.imgur.com/rjqVcYJ.jpg"},
    {"title": "Lucifer", "img": "https://i.imgur.com/nzXJ4wS.jpg"},
]

# Filter movies by search
if search:
    movies = [m for m in movies if search.lower() in m["title"].lower()]

# Display movies as a grid
cols = st.columns(3)

for index, movie in enumerate(movies):
    with cols[index % 3]:
        st.image(movie["img"], use_column_width=True)
        st.write(f"### {movie['title']}")
        st.button("Play", key=movie["title"])

# Footer
st.write("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
