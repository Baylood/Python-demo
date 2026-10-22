# import streamlit as st

# name = st.text_input("Enter your name")
# if name:
#     st.write(f"The name is: {name.title()}")

# age = st.number_input("age", min_value=1, max_value=110)

# if age:
#     st.write(f"your age is {age} years old.")

# information = st.text_area("write here your info")

# if information:
#     if len(information) > 50:
#         st.warning("your info more than 50")
#     elif len(information) < 50:
#         st.error("your info less than 50")
#     else:
#         st.success("your info is exactly 50 characters")


# # import streamlit as st

# answer = st.selectbox(
#     "select your program", ["python", "java script", "react", "typescript"]
# )
# if answer:
#     st.write(f"your answer is: {answer}")

# # import streamlit as st

# gender = st.radio("select your sex", ["Male", "Female"])

# if gender:
#     st.write(f"you are a {gender}")

# # import streamlit as st
# answer = st.checkbox("do you  like python")

# if answer:
#     st.write("I agree")

# st.title("Old title")  # This line will not run

import streamlit as st

right, center, left = st.columns([1, 3, 1])
with center:
    st.title("Abdalla's Workshop")
    with st.form("Register"):
        name = st.text_input("Name")
        st.text_input("Email")
        st.selectbox(
            "Track", ["Python", "React", "JavaScript", "Ai Course", "Html and Css"]
        )

        clicked = st.form_submit_button("Register", type="primary")
    if clicked:
        st.success(f"Welcome abroad {name}")
