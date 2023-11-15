import streamlit as st
Score = [30, 50, 40, 60, 80, 70]

st.write("# 시험성적")
st.write("## 이름 조준한")
st.write("### 학번 23115254")

st.line_chart(Score)