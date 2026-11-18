
import streamlit as st
import requests

st.set_page_config(
    page_title="Smart Resource Finder",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #080b18, #11152b, #17112b);
    color: #ffffff;
}

h1, h2, h3 {
    color: #ffffff;
}

p, label {
    color: #cbd5e1;
}

.stTextInput input {
    background-color: #1c2340;
    color: white;
    border: 1px solid #5145cd;
    border-radius: 10px;
}

.stButton button {
    background: linear-gradient(90deg, #6d28d9, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 25px;
    font-weight: bold;
}

.stButton button:hover {
    background: linear-gradient(90deg, #7c3aed, #3b82f6);
    color: white;
    border: none;
}

</style>
""", unsafe_allow_html=True)


st.title("🔍 Smart Resource Finder")
st.write("Discover popular GitHub projects easily!")

topic = st.text_input("Enter your project topic")

sort_option = st.selectbox(
    "Sort projects by",
    ["Most Starred", "Most Forked"]
)

if st.button("Search Projects"):

    if topic:

        sort_value = "stars" if sort_option == "Most Starred" else "forks"

        url = "https://api.github.com/search/repositories"

        params = {
            "q": topic,
            "sort": sort_value,
            "per_page": 5
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:

            data = response.json()

            if len(data["items"]) == 0:
                st.warning("No projects found!")

            else:
                for repo in data["items"]:
                    st.subheader("📁 " + repo["name"])
                    st.write(repo["description"])
                    st.write("⭐ Stars:", repo["stargazers_count"])
                    st.write("🍴 Forks:", repo["forks_count"])
                    st.markdown(f"[View on GitHub]({repo['html_url']})")
                    st.divider()

        else:
            st.error("Something went wrong!")

    else:
        st.warning("Please enter a topic first.")
