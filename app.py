import streamlit as st
import matplotlib.pyplot as plt
from sliding_window import sliding_window_max
import random

st.title("📊 Sliding Window Maximum Visualizer")

prices = [random.randint(10, 100) for _ in range(20)]
window_size = st.slider("Window size", 1, 10, 3)

result = sliding_window_max(prices, window_size)

fig, ax = plt.subplots()
ax.plot(range(len(prices)), prices, label='Stock Prices', marker='o')
ax.plot(range(window_size - 1, len(prices)), result, label='Sliding Max', marker='x')
ax.legend()

st.pyplot(fig)
 