import streamlit as st
from utils import generate_xiaohongshu

st.header("小红书文案AI写作助手~ 📝")

with st.sidebar:
    openai_api_key = st.text_input("请输入API密钥：", type="password")

subject = st.text_input("主题")
submit = st.button("开始写作")

if submit:
    if not openai_api_key:
        st.info("请输入你的API密钥")
        st.stop()
    if not subject:
        st.info("请输入生成内容的主题")
        st.stop()

    with st.spinner("AI正在思考中，请稍等..."):
        result = generate_xiaohongshu(subject, openai_api_key)
    st.divider()
    column1, column2 = st.columns(2)
    with column1:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### 小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### 小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### 小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### 小红书标题5")
        st.write(result.titles[4])
    with column2:
        st.markdown("##### 小红书正文")
        st.write(result.content)