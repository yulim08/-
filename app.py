import streamlit as st
import pandas as pd

# 앱 제목
st.title("학교 건의사항 제출하기")

# 건의사항 입력 폼
with st.form("suggestion_form"):
    name = st.text_input("이름")
    email = st.text_input("이메일")
    suggestion = st.text_area("건의사항")
    submitted = st.form_submit_button("제출")

    if submitted:
        # 데이터 저장 (예: CSV 파일)
        data = {'Name': name, 'Email': email, 'Suggestion': suggestion}
        df = pd.DataFrame([data])

        # 파일에 저장
        df.to_csv('suggestions.csv', mode='a', header=False, index=False)

        st.success("건의사항이 제출되었습니다!")

# 제출된 건의사항 보기
st.subheader("제출된 건의사항")
try:
    suggestions_df = pd.read_csv('suggestions.csv', names=['Name', 'Email', 'Suggestion'])
    st.write(suggestions_df)
except FileNotFoundError:
    st.write("아직 제출된 건의사항이 없습니다.")
