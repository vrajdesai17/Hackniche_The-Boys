import streamlit as st 
import time
import pickle
from pathlib import Path
from st_on_hover_tabs import on_hover_tabs
import streamlit_authenticator as stauth

# Authentication
names = ["Peter Parker"]
usernames = ["fc-solutions"]

# Load Hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {
        "usernames":{
            usernames[0]:{
                "name":names[0],
                "password":hashed_passwords[0]
                }          
            }
        }


authenticator = stauth.Authenticate(credentials,"sales_dashboard","abcdef",cookie_expiry_days=0)
name,authentication_status,username = authenticator.login("Fuel Cycle","main")
# st.set_page_config(layout="wide")
if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:

    # st.set_page_config(layout="wide")

    st.header("Custom tab component for on-hover navigation bar")
    st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


    with st.sidebar:
        tabs = on_hover_tabs(tabName=['Dashboard', 'Money', 'Economy'], 
                            iconName=['dashboard', 'money', 'economy'], default_choice=0)

    if tabs =='Budget':
        st.title("Budgeting")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Expense Tracking':
        st.title("Track your Expense")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Portfolio':
        st.title("Portfolio Management")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Financial goal setting':
        st.title("Portfolio Management")
        st.write('Name of option is {}'.format(tabs))

# df = pd.read_csv('')
# df['date'] = pd.to_datetime(df['date'])

# def plot_animation(df):
#     lines = alt.Chart(df).mark_line().encode(
#        x=alt.X('date:T', axis=alt.Axis(title='date')),
#        y=alt.Y('value:Q',axis=alt.Axis(title='value')),
#      ).properties(
#        width=600,
#        height=300
#      ) 
#     return lines

# N = df.shape[0] # number of elements in the dataframe
# burst = 6       # number of elements (months) to add to the plot
# size = burst     # size of the current dataset
# line_plot = st.altair_chart(lines)
# start_btn = st.button('Start')

# if start_btn:
#    for i in range(1,N):
#       step_df = df.iloc[0:size]
#       lines = plot_animation(step_df)
#       line_plot = line_plot.altair_chart(lines)
#       size = i + burst
#       if size >= N: 
#          size = N - 1
#       time.sleep(0.1)