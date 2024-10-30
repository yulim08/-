import streamlit as st
import pandas as pd
import os

# 앱 제목
st.title("학교 건의사항 제출하기")

# 파일 경로 지정
file_path = 'suggestions.csv'

# 건의사항 입력 폼
with st.form("suggestion_form"):
    name = st.text_input("이름")
    suggestion = st.text_area("건의사항")
    submitted = st.form_submit_button("제출")

    if submitted:
        # 데이터 저장 (예: CSV 파일)
        data = {'Name': name, 'Suggestion': suggestion}
        df = pd.DataFrame([data])

        # 파일에 저장
        df.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)

        st.success("건의사항이 제출되었습니다!")

# 제출된 건의사항 보기
st.subheader("제출된 건의사항")
try:
    suggestions_df = pd.read_csv(file_path, names=['Name', 'Suggestion'])
    st.write(suggestions_df)

 # 삭제할 건의사항 및 이름 선택
    suggestion_to_delete = st.selectbox("삭제할 건의사항 선택", suggestions_df['Suggestion'].tolist())
    name_to_delete = suggestions_df[suggestions_df['Suggestion'] == suggestion_to_delete]['Name'].values[0]

    if st.button("삭제"):
        # 선택한 건의사항 삭제
        suggestions_df = suggestions_df[suggestions_df['Suggestion'] != suggestion_to_delete]
        suggestions_df.to_csv(file_path, index=False, header=True)  # 업데이트된 데이터 저장
        st.success("건의사항이 삭제되었습니다!")
        st.experimental_rerun()  # 페이지 새로 고침


     # 답글 작성
    reply_for = st.selectbox("답글을 달 건의사항 선택", suggestions_df['Suggestion'].tolist())
    reply_text = st.text_area("답글 입력")

    if st.button("답글 달기"):
        # 답글 추가
        suggestions_df.loc[suggestions_df['Suggestion'] == reply_for, 'Reply'] = reply_text
        suggestions_df.to_csv(file_path, index=False, header=True)  # 업데이트된 데이터 저장
        st.success("답글이 달렸습니다!")
        st.experimental_rerun()  # 페이지 새로 고침

except FileNotFoundError:
    st.write("아직 제출된 건의사항이 없습니다.")

