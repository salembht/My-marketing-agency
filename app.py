import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def get_marketing_agency(role, context ,goal):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {"role": "system", "content": f"you are now {role} in my marketing agency give me a plan to what I shoulde do if the markiting need in the bio to make the Objectives "},
            {"role": "user", "content": f">>Bio stats: {context}\n\n>>Objective: {goal}"},
        ]
    )
    return response.choices[0].message.content


# User inputs and model parameters
st.sidebar.header("marketing agency")

context = st.sidebar.text_input(
    "Insert your need",  placeholder="Your needs")
goal = st.sidebar.text_input("What the gool you need to fit:",
                             value="markting gool")

# Main page components
st.title("Markting Agency")
st.subheader("Team manager")
response =get_marketing_agency("Team manager", context, goal)
st.markdown(response)
st.subheader("Creative director")
response =get_marketing_agency("Creative director", context, goal)
st.markdown(response)
st.subheader("Social Media Manager")
response =get_marketing_agency("Social Media Manager", context, goal)
st.markdown(response)
st.subheader("Advertising Officer")
response =get_marketing_agency("Advertising Officer", context, goal)
st.markdown(response)
st.subheader("Content writer")
response =get_marketing_agency("Content writer", context, goal)
st.markdown(response)


