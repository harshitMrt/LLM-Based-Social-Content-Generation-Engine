import streamlit as st
import streamlit.components.v1 as components
import html
import streamlit.components.v1 as components
import html

from few_shots import FewShotsPost
from post_generator import generate_post

# Page config (VERY IMPORTANT – put at top)
st.set_page_config(
    page_title="Social Post Generator",
    page_icon="💼",
    layout="centered"
)

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    # ---------- HERO SECTION ----------
    st.markdown(
        """
        <h1 style='text-align:center;'>🚀 LinkedIn Post Generator</h1>
        <p style='text-align:center; color: gray;'>
        Create high-quality LinkedIn posts using AI in seconds
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    fs = FewShotsPost()

    # ---------- INPUT CARD ----------
    with st.container():
        st.markdown(
            """
            <div style="
                background-color:#0E1117;
                padding:25px;
                border-radius:15px;
                box-shadow:0 4px 20px rgba(0,0,0,0.2);
            ">
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            selected_tag = st.selectbox(
                "📝 Topic",
                options=fs.get_tags()
            )

        with col2:
            selected_length = st.selectbox(
                "📏 Length",
                options=length_options
            )

        with col3:
            selected_language = st.selectbox(
                "🌐 Language",
                options=language_options
            )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- GENERATE BUTTON ----------
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

    with col_btn2:
        generate_clicked = st.button(
            "✨ Generate Post",
            use_container_width=True
        )

    # ---------- OUTPUT ----------
    if generate_clicked:
        with st.spinner("✍️ Crafting your LinkedIn post..."):
            post = generate_post(
                selected_tag,
                selected_length,
                selected_language
            )

        post = html.escape(str(post))

        st.markdown("### 📄 Generated Post")

        components.html(
            f"""
            <div style="
                width:100%;
                box-sizing:border-box;
            ">
                <textarea id="postBox" style="
                    width:100%;
                    height:360px;
                    padding:16px;
                    font-size:15px;
                    border-radius:10px;
                    background:#111827;
                    color:white;
                    border:1px solid #374151;
                    resize:none;
                    white-space:pre-wrap;
                    line-height:1.6;
                    box-sizing:border-box;
                ">{post}</textarea>

                <div style="
                    display:flex;
                    justify-content:center;
                    margin-top:16px;
                ">
                    <button onclick="navigator.clipboard.writeText(document.getElementById('postBox').value)"
                    style="
                        padding:10px 18px;
                        border-radius:8px;
                        border:none;
                        background:#3B82F6;
                        color:white;
                        cursor:pointer;
                        font-size:14px;
                        font-weight:600;
                    ">
                    📋 Copy Post
                    </button>
                </div>
            </div>
            """,
            height=460,  # 🔑 KEY FIX: enough height for all content
        )

        st.success("✅ Post generated successfully! Ready to post on LinkedIn 🚀")
    # ---------- FOOTER ----------
    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit & LLMs</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()