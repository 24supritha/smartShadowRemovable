import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Smart Document Shadow Removal", page_icon="📄", layout="wide")

def remove_shadows(image_rgb):
    """Estimate uneven illumination and normalize it to reduce document shadows."""
    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab)

    # Estimate the slowly changing background illumination.
    kernel_size = max(31, (min(image.shape[:2]) // 8) | 1)
    if kernel_size % 2 == 0:
        kernel_size += 1
    background = cv2.medianBlur(l_channel, kernel_size)

    # Normalize illumination while avoiding division by zero.
    background = np.maximum(background, 1)
    normalized = cv2.divide(l_channel, background, scale=255)
    normalized = cv2.normalize(normalized, None, 0, 255, cv2.NORM_MINMAX)

    # Improve text contrast and reconstruct a color image.
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(normalized)
    result_lab = cv2.merge((enhanced, a_channel, b_channel))
    result = cv2.cvtColor(result_lab, cv2.COLOR_LAB2RGB)
    return result

st.title("📄 Smart Document Shadow Removal")
st.write("Upload a document image to reduce uneven shadows and improve readability.")
st.info("For best results, use a clear photo of a page with visible shadows.")

uploaded = st.file_uploader("Choose a document image", type=["png", "jpg", "jpeg", "bmp"])

if uploaded:
    try:
        pil_image = Image.open(uploaded).convert("RGB")
        original = np.array(pil_image)
        with st.spinner("Removing shadows..."):
            processed = remove_shadows(original)

        left, right = st.columns(2)
        with left:
            st.subheader("Original Image")
            st.image(original, use_container_width=True)
        with right:
            st.subheader("Processed Image")
            st.image(processed, use_container_width=True)

        output = BytesIO()
        Image.fromarray(processed).save(output, format="PNG")
        st.download_button(
            "⬇️ Download cleaned document",
            data=output.getvalue(),
            file_name="shadow_removed_document.png",
            mime="image/png"
        )
    except Exception as exc:
        st.error(f"Could not process this image: {exc}")
else:
    st.caption("Supported formats: PNG, JPG, JPEG and BMP.")
