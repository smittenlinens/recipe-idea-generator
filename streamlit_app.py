import streamlit as st
from PIL import Image
import requests

def main():
    st.header("Jovyn's First Pet Project")
    st.markdown("Recipe Idea Generator and Fridge Inventory Management App")
    text_input = st.text_input("Enter a food item in your fridge that you want a recipe idea of.")
    if text_input == "chicken":
        return st.write(["Chicken Burrito Wrap", 
        "Japanese Cream Pasta", 
        "Pesto Chicken Toastie", 
        "Oyakodon"])
    image = Image.open("fridge-organization.jpg")
    st.image(image, caption = 'Generating recipe ideas')

if __name__ == "__main__":
    main()