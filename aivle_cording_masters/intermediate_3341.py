# 3341
import statistics as st
a = input()
b = input()
a_c = st.mode(a)
b_c = st.mode(b)
a_count = 0 
b_count = 0 
for i in range(len(a)):
    if a[i] in a_c:
        a_count += 1
        
for i in range(len(b)):
    if b[i] in b_c:
        b_count += 1
    
print(b_count - a_count)