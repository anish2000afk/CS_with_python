import statistics as st

v = [7, 8, 8, 11, 7, 7]
m1 = st.mean(v)
m2 = st.mode(v)  # most frequent; remember to rearrange
m3 = st.median(v)  # most central values
print(m1, m2, m3)
