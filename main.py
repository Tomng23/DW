import streamlit as st

friends = []

st.title("Quản lý bạn thân")

name = st.text_input("Nhập tên bạn thân:")
info = st.text_area("Nhập thông tin về bạn thân:")
if st.button("Lưu"):
    if name and info:
        friends.append({"name": name, "info": info})
        st.success(f"Đã lưu thông tin của {name}.")
    else:
        st.error("Vui lòng nhập đầy đủ thông tin.")

if friends:
    st.subheader("Chọn tên để xem thông tin:")
    selected_name = st.selectbox("Bạn thân:", [friend["name"] for friend in friends])
    if selected_name:
        selected_friend = next(friend for friend in friends if friend["name"] == selected_name)
        st.write(f"**Thông tin của {selected_name}:**")
        st.write(selected_friend["info"])
else:
    st.write("Chưa có bạn thân nào được lưu.")
#testing