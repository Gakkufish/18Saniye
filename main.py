import streamlit
import langchain_helper
import textwrap

streamlit.title("18 Saniye")

with streamlit.sidebar:
    with streamlit.form(key="my_form"):
        youtube_url = streamlit.sidebar.text_area(
            label = "Video linki:",
            #max_chars= 50
        )

        query = streamlit.sidebar.text_area(
            label = "Sorunuz?",
            #max_chars = 50
            key = "query"
        )

        submit_button = streamlit.form_submit_button(label="Konuştur!")

if query and youtube_url:
    db = langchain_helper.create_vector_db_from_youtube_url(youtube_url)
    #response, docs = langchain_helper.get_response_from_query(db,query)
    response = langchain_helper.get_response_from_query(db,query)

    streamlit.text(textwrap.fill(response, width=80))