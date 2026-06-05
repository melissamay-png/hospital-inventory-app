import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hospital Inventory AI Agent", layout="wide")

st.title("🏥 Hospital Inventory AI Agent")
st.write("This app checks hospital inventory levels and flags items that need replenishment.")

# Load Excel data
try:
    inventory_df = pd.read_excel("Hospital Inventory.xlsx")
    st.dataframe(inventory_df)

    # Identify low-stock items
    low_stock = inventory_df[inventory_df["Quantity"] < inventory_df["Reorder Level"]]

    st.subheader("⚠️ Low Stock Items")
    if not low_stock.empty:
        st.table(low_stock)
        st.success(f"{len(low_stock)} items need to be reordered.")
    else:
        st.info("All items are sufficiently stocked!")

    # Summary
    st.subheader("📊 Summary")
    st.write(f"Total Inventory Items: {len(inventory_df)}")
    st.write(f"Items Needing Reorder: {len(low_stock)}")

except FileNotFoundError:
    st.error("Excel file not found. Please make sure 'Hospital Inventory.xlsx' is in the same folder.")
except Exception as e:
    st.error(f"An error occurred: {e}")
