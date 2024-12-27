import streamlit as st

available_classes = [
    "Toán", "Lý", "Hóa", "Văn", "Anh", "Sinh", "Tin học", "Thể dục", "Sử", "Địa"
]

schedule = {
    "Thứ Hai": ["", "", "", "", "", "", ""],
    "Thứ Ba": ["", "", "", "", "", "", ""],
    "Thứ Tư": ["", "", "", "", "", "", ""],
    "Thứ Năm": ["", "", "", "", "", "", ""],
    "Thứ Sáu": ["", "", "", "", "", "", ""],
}

st.title("Quản Lý Thời Khóa Biểu")

selected_day = st.selectbox("Chọn ngày trong tuần:", list(schedule.keys()))

st.write(f"### Cập nhật thời khóa biểu cho {selected_day}")

for i in range(7):
    schedule[selected_day][i] = st.selectbox(
        f"Chọn môn học cho Tiết {i + 1}:",
        [""] + available_classes, 
        index=0 if schedule[selected_day][i] == "" else available_classes.index(schedule[selected_day][i]) + 1  
    )

st.write(f"### Thời khóa biểu cho {selected_day}:")
classes = schedule[selected_day]
for idx, subject in enumerate(classes, start=1):
    st.write(f"- Tiết {idx}: {subject if subject else 'Chưa chọn'}")

if st.button("Lưu thời khóa biểu"):
    st.success(f"Thời khóa biểu cho {selected_day} đã được lưu thành công!")

if st.checkbox("Hiển thị toàn bộ thời khóa biểu"):
    st.write("### Toàn bộ thời khóa biểu:")
    for day, subjects in schedule.items():
        st.write(f"#### {day}:")
        for idx, subject in enumerate(subjects, start=1):
            st.write(f"- Tiết {idx}: {subject if subject else 'Chưa chọn'}")

def create_schedule_file(schedule_data):
    schedule_text = ""
    for day, subjects in schedule_data.items():
        schedule_text += f"{day}:\n"
        for idx, subject in enumerate(subjects, start=1):
            schedule_text += f"  Tiết {idx}: {subject if subject else 'Chưa chọn'}\n"
        schedule_text += "\n"

    return schedule_text.encode("utf-8")

if st.button("Tải xuống thời khóa biểu"):
    schedule_file = create_schedule_file(schedule)
    st.download_button(
        label="Tải xuống file thời khóa biểu",
        data=schedule_file,
        file_name="thoi_khoa_bieu.txt",
        mime="text/plain"
    )
