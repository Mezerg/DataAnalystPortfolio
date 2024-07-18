import pandas as pd
import streamlit as st

with open('assets/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Shop Sales Analysis')

# Load data
df = pd.read_csv('data/data.csv', index_col=0)
sub = df.groupby('Product')['Quantity Sold'].sum()
sub2 = df.groupby('Product')['Quantity Sold'].agg(['median', 'mean'])
top_quantity_product = sub.max()
average_quantity_product = sub.mean()
median_quantity_product = sub.median()
st.write(
    """
    ## Quantity Sold by Product
    """
)

# Diplay_data_1
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Quantity Sold", top_quantity_product, sub.idxmax())

with col2:
    st.metric("Average Quantity Sold", average_quantity_product)


with col3:
    st.metric("Median Quantity Sold", median_quantity_product)

st.bar_chart(sub)

st.write("## Mean and Median Chart of Quantity Sold by Product") 
# Display_data_2
chart_type = st.selectbox(
    "Select Chart Type",
    ["Line ", "Bar",])

if chart_type == 'Bar':
    st.bar_chart(
        sub2, color=["#001975", "#429ef5"]  # Optional
    )
else:
    st.line_chart(
        sub2, color=["#FF0000", "#0000FF"]  # Optional
    )

# sub_dropped = df.drop(columns=['Price'])

st.write('## Total Profit of Each Product')
st.bar_chart(df.groupby('Product')['Price'].sum())
st.write("## Data Table (Top 10)")
st.write(df.head(10))
