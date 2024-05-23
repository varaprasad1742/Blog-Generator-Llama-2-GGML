import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


st.set_page_config(page_title="Blog Generator", page_icon="📖",layout="centered",initial_sidebar_state="collapsed")

st.header("Blog Generator 📝")


input_topic = st.text_input("Enter the topic of your blog")

row1=st.columns(2)
row2,=st.columns(1)
row3, = st.columns(1)

with row1[0]:
    no_words = st.slider("Select the number of words", 100, 4000, 300)

with row1[1]:
    no_paragraphs = st.text_input("Enter the number of paragraphs")

with row2:
    blog_for = st.text_input("For whom you are writing this blog, eg: students, professionals, reasearchers etc")

writing_styles = (
    "Narrative",
    "Descriptive",
    "Expository",
    "Persuasive",
    "Opinionated",
    "Analytical",
    "Informative",
    "Interview-style",
    "Comparative",
    "Humorous",
    "Reflective",
    "Listicle",
    "Interactive",
    "Round-up",
    "Storytelling"
)

with row3:
    blog_style = st.selectbox("Style of the blog: ",writing_styles,index=0)

submit = st.button("Generate Blog")

llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q6_K.bin",model_type="llama",config={"temperature":0.5})

def generate_blog(input_topic,no_words,no_paragraphs,blog_for,blog_style):
    

    #prompt
    template = """Write a blog for {blog_for} on the topic {input_topic}. The blog should contain {no_paragraphs} paragraphs and total number of words should be {no_words}. The style of the blog should be {blog_style}. Include emojis and stickers as well..."""
    #chatprompt template
    chat = PromptTemplate(input_variables=["blog_for","input_topic","no_paragraphs","no_words",'blog_style'],template=template)

    #Generate blog from GGML LLM
    respone = llm.invoke(chat.format(blog_for=blog_for,input_topic=input_topic,no_paragraphs=no_paragraphs,no_words=no_words,blog_style=blog_style))
    return respone
if submit:
    blog=generate_blog(input_topic,no_words,no_paragraphs,blog_for,blog_style)
    st.write(blog)


