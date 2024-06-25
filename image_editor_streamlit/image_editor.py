import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
from PIL.ImageFilter import *
from io import BytesIO

# Function to load and apply CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS file
load_css("E:\streamlit_projects\style1.css")

# Title and Header
st.markdown("<h1>IMAGE EDITOR</h1>", unsafe_allow_html=True)
st.markdown("---")

# Image Upload
image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)

    info.markdown("<h2>Image Information</h2>", unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)
    
    # Resizing
    st.markdown("<h2>Resize Image</h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)
    
    # Rotation
    st.markdown("<h2>Rotate Image</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree", min_value=0, max_value=360, step=1)
    
    # Filter
    st.markdown("<h2>Apply Filter</h2>", unsafe_allow_html=True)
    filters = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss", "Smooth", "Contour", "Sharpen", "Edge Enhance"))
    
    # Background Color
    st.markdown("<h2>Background Color</h2>", unsafe_allow_html=True)
    bg_color = st.color_picker("Pick a background color", "#FFFFFF")
    
    # Color Transformation
    st.markdown("<h2>Color Transformation</h2>", unsafe_allow_html=True)
    color_transform = st.selectbox("Color Transformation", options=("None", "Grayscale", "Sepia", "Invert"))
    
    # Submit Button
    s_btn = st.button("Submit")
    
    if s_btn:
        # Resize and Rotate
        edited = img.resize((width, height)).rotate(degree)
        
        # Apply Filter
        filtered = edited
        if filters != "None":
            if filters == "Blur":
                filtered = edited.filter(BLUR)
            elif filters == "Detail":
                filtered = edited.filter(DETAIL)
            elif filters == "Emboss":
                filtered = edited.filter(EMBOSS)
            elif filters == "Smooth":
                filtered = edited.filter(SMOOTH)
            elif filters == "Contour":
                filtered = edited.filter(CONTOUR)
            elif filters == "Sharpen":
                filtered = edited.filter(SHARPEN)
            elif filters == "Edge Enhance":
                filtered = edited.filter(EDGE_ENHANCE)
        
        # Apply Background Color
        if filtered.mode in ("RGBA", "LA") or (filtered.mode == "P" and "transparency" in filtered.info):
            background = Image.new("RGBA", filtered.size, bg_color)
            filtered = Image.alpha_composite(background, filtered.convert("RGBA"))
        
        # Apply Color Transformation
        if color_transform == "Grayscale":
            filtered = ImageOps.grayscale(filtered)
        elif color_transform == "Sepia":
            sepia = ImageEnhance.Color(filtered).enhance(0.3)
            filtered = ImageOps.colorize(sepia.convert("L"), "#704214", "#C0C090")
        elif color_transform == "Invert":
            filtered = ImageOps.invert(filtered.convert("RGB"))
        
        # Display the filtered image
        st.image(filtered)
        
        # Format selection for saving the edited image
        st.markdown("<h2>Download Image</h2>", unsafe_allow_html=True)
        format_options = st.selectbox("Select Image Format", options=("PNG", "JPEG", "BMP", "GIF", "TIFF"))
        
        # Convert the image to the selected format and provide a download button
        buf = BytesIO()
        filtered.save(buf, format=format_options)
        byte_im = buf
