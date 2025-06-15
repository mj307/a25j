import streamlit as st
from PIL import Image, ImageDraw
import streamlit.components.v1 as components

st.set_page_config(page_title="Father’s Day Tribute", layout="centered")

def add_rounded_corners(im, radius=40):
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
    im.putalpha(alpha)
    return im

st.title("Happy Father’s Day, Dad!! 💙")


st.markdown("### Music while you scroll")
components.iframe(
    "https://open.spotify.com/embed/playlist/4cbOOH6OUutN9KHDHQRYw1?utm_source=generator",
    height=300,
    width=700,
)


st.markdown("### Day 1: The Beginning of Dadhood")

img1 = Image.open("one.png").resize((350, 350))
img1 = add_rounded_corners(img1, radius=40)

img2 = Image.open("annoyed.png").resize((350, 350))
img2 = add_rounded_corners(img2, radius=40)

col1, col2 = st.columns(2)
with col1:
    st.image(img1, caption="#FirstPicTogether")
with col2:
    st.image(img2, caption="That moment when you realize you won't be having a peaceful night for a while")


st.markdown("<h3 style='text-align:center; color:#4A90E2;'>📸 Memories Over the Years</h3>", unsafe_allow_html=True)

if "carousel_index" not in st.session_state:
    st.session_state.carousel_index = 0

carousel_images = [
    "c1.png",
    "c2.png",
    "c3.png",
    "c4.png",
    "c5.png",
    "c6.png"
]


with st.container():
    prev_col, img_col, next_col = st.columns([1, 3, 1])

    with prev_col:
        prev_clicked = st.button("← Prev")

    with next_col:
        next_clicked = st.button("Next →")

    if prev_clicked:
        st.session_state.carousel_index = (st.session_state.carousel_index - 1) % len(carousel_images)
    if next_clicked:
        st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(carousel_images)


    current_image_path = carousel_images[st.session_state.carousel_index]
    img = Image.open(current_image_path).resize((350, 350))
    img = add_rounded_corners(img, radius=40)

    with img_col:
        st.image(img, caption=f"Love you!")

tuscany_box = """
<div style="
    background-color: #FCD299;
    padding: 25px;
    border-radius: 15px;
    margin-top: 40px;
    color: #333333;
    font-size: 16px;
    line-height: 1.7;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
">
    <strong>I imagine your day will be filled with plenty of driving, as always</strong>, but I’m virtually sending you a plate of aloo tikki, chole, and a cold beer to go with it.<br><br>
    Ever since I was little, I’ve always felt the immense love behind everything you do for me. Whether it was buying me the 72-pack of crayons when everyone else had just 12 to encourage my creativity, or picking up the jumbo size of anything from Costco the moment I mentioned I liked it, you’ve always made me feel seen and cared for.<br><br>
    I notice your dedication every single day. The way you work so hard, often without recognition, is something I find deeply inspiring. Thank you for teaching me, not just through your words, but through your actions.<br><br>
    You may not always realize it, but when you say something, it sticks. Years ago, you used to yell at me for not taking notes. Now, it’s the first thing I do whenever I’m learning something new or sitting in a meeting. I carry your lessons with me, quietly but constantly.<br><br>
    Thank you for everything you do. I’m so incredibly lucky to have you. You make my world brighter, and I love you more than words can say.
</div>
"""

st.markdown(tuscany_box, unsafe_allow_html=True)