import streamlit as st
st.set_page_config(page_title='Trac nghiem tinh canh', page_icon=':question:', layout='wide')
st.title('Hay chon mot con vat ban yeu thich')
col1, col2, col3, col4, col5 = st.columns(5)

Personality = {'Con meo': 'Lua chon nay cho thay ban van chua san sang bat dau voi cong viec, ban khao khat duoc nghi ngoi.', 
'Con cho':'Ban cam nhan duoc su ho tro nhiet tinh cua ban be va vi the nen san sang giai quyet moi van de xay ra.', 
'Con su tu': 'Co the thay ban la mot nguoi voi ve ngoai noi bat. Ban thu hut moi nguoi bang ve ngoai hoang nhoang.',
'Con ngua': 'Co ve nhu ban dang bi han che boi mot thu gi do lam cho ban khong cam thay duoc tu do.',
'Thien nga': 'Hien tai ban dang co mot khoang thoi gian vui ve, ngot ngao, hay co gan tan huong.'}

with col1:
    b1 = st.button('Con meo')
with col2:
    b2 = st.button('Con cho')
with col3:
    b3 = st.button('Con su tu')
with col4:
    b4 = st.button('Con ngua')
with col5:
    b5 = st.button('Thien nga')

if b1:
    with st.expander('Con meo'):
        st.write(Personality['Con meo'])
if b2:
    with st.expander('Con cho'):
        st.write(Personality['Con cho'])
if b3:
    with st.expander('Con su tu'):
        st.write(Personality['Con su tu'])
if b4:
    with st.expander('Con ngua'):
        st.write(Personality['Con ngua'])
if b5:
    with st.expander('Thien nga'):
        st.write(Personality['Thien nga'])

with st.sidebar:
    st.title('Trac nghiem tinh cach')
    if b1:
        st.write('Con vat ma ban chon la con meo')
    if b2:
        st.write('Con vat ma ban chon la con cho')
    if b3:
        st.write('Con vat ma ban chon la con su tu')
    if b4:
        st.write('Con vat ma ban chon la con ngua')
    if b5:
        st.write('Con vat ma ban chon la con thien nga')


