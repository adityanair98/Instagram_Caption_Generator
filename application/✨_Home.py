import streamlit as st
import pandas as pd
from pathlib import Path


# Function to store the user data to a CSV file
def save_user_data(first_name, last_name, email, phone):
    """Function to store the user data to a CSV file"""
    csv_file = Path("./user_data/user_data.csv")
    # Check if the file exists and create a DataFrame accordingly
    if csv_file.exists():
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(
            columns=["First Name", "Last Name", "Email", "Phone Number"])

    # Add and save new user data
    new_data = {"First Name": first_name, "Last Name": last_name,
                "Email": email, "Phone Number": phone}
    df = df.append(new_data, ignore_index=True)
    df.to_csv(csv_file, index=False)


def main():
    # Define Streamlit configurations
    st.set_page_config(page_title="Instamuse", page_icon=":camera:",
                       initial_sidebar_state='auto')

    # Sidebar configuration
    with st.sidebar:
        st.image('insta.png')
        st.title("InstaMuse")
        st.subheader("Welcome to InstaMuse, the ultimate tool for turning\
        your snapshots into social media sensations!")
        st.write("Start turning heads with your posts.\
                 Use InstaMuse now and watch your likes soar!")

    # Title
    st.markdown("""
    <style>
    .title-font {
        font-size: 50px;
        font-weight: bold;
        font-family: 'Helvetica', sans-serif; /* You can change the\
                font-family */
        color: #FF573D; /* Color for the title */
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h1 class="title-font">The Worlds Best Instagram Caption\
                Generator</h1>', unsafe_allow_html=True)

    # Subheader
    st.write("""### Transform your online presence—join InstaMuse to create \
        innovative captions that increase likes and enhance your visibility.\
        """)

    # Gif
    st.image('insta.gif')

    # Why us?
    st.subheader('Why InstaMuse?')
    st.write("""
    - 🎨 **Creativity at your fingertips:** Generate unique captions that\
             stand out.
    - ⏳ **Save time:** Stop spending hours trying to write the perfect caption.
    - 🚀 **Boost engagement:** Captions crafted to keep your audience engaged.
    - 💸 **Free to use:** Get access to our technology preview at no cost.
    """)

    # Success Stories
    st.subheader('Success Stories')
    cols = st.columns(2)
    with cols[0]:
        st.image('insta_post.png')
    with cols[1]:
        st.write("")
        st.write("")
        st.write('"InstaMuse helped us reach a wider audience. \
                 Our engagement rates have never been higher!" \
                 - CR')
        st.write("")
        st.write('"Thanks to InstaMuse, our posts now resonate better \
                 with our audience, bringing more likes and comments \
                 than ever before." - LJ')
        st.write("")
        st.write('"The creative captions we developed with InstaMuse \
                 have not only increased likes but also built lasting \
                 connections with our followers." - MK')

    # Sign up section
    st.subheader('Sign up here for priority access')
    st.write('Enter your details below to get early access to our innovative\
             caption generator.')

    # Form to collect user details
    with st.form(key='user_details_form'):
        cols = st.columns(2)
        with cols[0]:
            first_name = st.text_input("First Name")
            email = st.text_input("Email", help="We'll never share your email\
                                  with anyone else.")
        with cols[1]:
            last_name = st.text_input("Last Name")
            phone = st.text_input("Phone Number", help="We'll never share your\
                                  number with anyone else.")
        submit_button = st.form_submit_button("Start Using InstaMuse")

        if submit_button:
            if first_name and last_name and email and phone:
                save_user_data(first_name, last_name, email, phone)
                st.success("Thank you for signing up! We will be in\
                           touch soon.")
            else:
                st.error("Please fill in all the fields.")


if __name__ == "__main__":
    main()
