import streamlit as st
import time

st title("visualisasi sorting")


col1, col2= st.columns(2)
algo= col1.selectbox("pilih algoritma", ["bubble sort", "selection sort", "insertion sort"])
user_input = col2.text_input("input data(pisahkan koma)", "85,60,92,88")


if algo == "bubble sort":
    st.info("**bubble sort**: membandingkan elemen bersebelahan & menukarnya jika salah satu urutan elemen terbesar'menggelembung' ke akhir.")
elif  algo == "selection sort":
    st.info("**selection sort**: memilih elemen terkecil dari bagian yang belum terurut, lalu menukarnya ke posisi paling depan.")
elif algo == "insertion sort":
    st.info("**insertion sort**:bekerja seperti mengurutkan kartu; menyisipkan elemen satu persatu ke posisi yang tepat di bgain yang sudah terurut.")


try:
    data=[int(x.strip()) for x in user_input.split(",") if x.strip()]
except ValueError:
    st.error("gagal! pastikan anda hanya memasukkan angka.")
    st.stop()


chart = st.empty()
chart.bar_chart(data)


if st.button("mulai urutkan", type="primary"):
    n = len(data)

    if algo == "bubble sort":
        for i in range(n):
            for j in range (0, n - i - 1):
                if data [j] > data [j + 1]:
                    data(j), data [j+1]= data[j + 1], data[j]
                    chart.bar_chart(data)
                    time.sleep(0.2)

    elif algo == "selection sort":
        for i in range(n):
            min_idx == i
            for j in range(i + 1, n):
                if data[j] < data [min_idx]:
                    min_idx=j
            data[i], data[min_idx] =[min_idx], data[i]

            chart.bar_chart(data)
            time.sleep(0.2)
    elif algo == "insertion sort":
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data [j] > key:
                data[j+1]= data [j]
                j -=1
                chart.bar_chart(data)
                time.sleep(0.2)
            data[j + 1]=key
            chart.bar_chart(data)
            time.sleep(0.2)
    
    st.succes(f"sorting selesai: {data}")

            
