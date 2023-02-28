import streamlit as st
import sqlite3



conn=sqlite3.connect("시설관리.db")



시설명=st.text_input("시설명")
선택지=['전기','기계']
문제발생=st.selectbox('항목', 선택지)
if 문제발생==선택지[0]:
    전기선택지=['전기시설문제없냐','전구나간거없냐']
    전기문제발생=st.selectbox('항목', 전기선택지)
elif 문제발생==선택지[1]:
    기계선택지=['기계설비괜찮냐','냉난방문제없냐']
    기계문제발생=st.selectbox('항목', 기계선택지)



date=st.date_input('점검날짜') 
제출=st.button('제출')
if 제출==1:
    st.write("제출됨")

with conn:
    cur=conn.cursor()
    sql = "insert into 시설관리(시설명,내용,날짜) values(?,?,?)"
    if 제출==1:
        cur.execute(sql, (시설명, 문제발생, date))
    conn.commit()
st.write(시설명)
st.write(date)
st.write(제출)
view=[100,150,30]
st.write('# 유튭 조회수')
st.write('## 유튭 조회수')

st.bar_chart(view) 