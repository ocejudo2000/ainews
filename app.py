import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import source_manager
import news_fetcher
import content_generator
import exporter
import email_sender
from io import BytesIO

st.set_page_config(page_title="AI News Aggregator", layout="wide")

st.title("AI News Aggregator & Content Creator")

st.sidebar.title("Settings")

# Source management
st.sidebar.header("Manage Data Sources")
sources = source_manager.get_sources()
st.sidebar.table(sources)

new_source_name = st.sidebar.text_input("Source Name:")
new_source_url = st.sidebar.text_input("Source URL or RSS Feed:")
new_source_type = st.sidebar.selectbox("Source Type:", ["blog", "news", "rss"])

if st.sidebar.button("Add Source"):
    if new_source_name and new_source_url:
        source_manager.add_source(new_source_name, new_source_url, new_source_type)
        st.sidebar.success(f"Source '{new_source_name}' added!")
        st.experimental_rerun()
    else:
        st.sidebar.error("Please provide a name and URL for the source.")


# Time period selection
st.sidebar.header("Time Period")
time_period = st.sidebar.selectbox("Select the time period:", ["Last 24 hours", "Last 3 days", "Last week"])

# Email configuration
st.sidebar.header("Email Configuration")
sender_email = st.sidebar.text_input("Sender Email")
sender_password = st.sidebar.text_input("Sender Password", type="password")
receiver_email = st.sidebar.text_input("Receiver Email")
smtp_server = st.sidebar.text_input("SMTP Server", "smtp.gmail.com")
smtp_port = st.sidebar.number_input("SMTP Port", 587)

# Main content area
st.header("Latest AI News")

if st.button("Generate News Summary and Article"):
    with st.spinner("Fetching news and generating content..."):
        articles = news_fetcher.fetch_all_news(sources)
        st.session_state.articles = articles

        summary = content_generator.generate_executive_summary(articles)
        st.session_state.summary = summary

        linkedin_title, linkedin_body, linkedin_image = content_generator.generate_linkedin_article(articles)
        st.session_state.linkedin_title = linkedin_title
        st.session_state.linkedin_body = linkedin_body
        st.session_state.linkedin_image = linkedin_image

if 'articles' in st.session_state:
    with st.expander("Executive Summary", expanded=True):
        st.markdown(st.session_state.summary)

    st.header("LinkedIn Article")
    with st.container():
        st.subheader(st.session_state.linkedin_title)
        st.markdown(st.session_state.linkedin_body)
        st.image(st.session_state.linkedin_image, caption="Generated Image")

    st.header("Export & Email")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # HTML Download
        html_content = exporter.export_to_html(st.session_state.summary, st.session_state.articles)
        st.download_button(
            label="Download as HTML",
            data=html_content,
            file_name="ai_news_summary.html",
            mime="text/html",
        )
    with col2:
        # PDF Download
        pdf_buffer = BytesIO()
        pdf = exporter.export_to_pdf(st.session_state.summary, st.session_state.articles)
        pdf_buffer.write(pdf.output(dest='S').encode('latin-1'))
        st.download_button(
            label="Download as PDF",
            data=pdf_buffer,
            file_name="ai_news_summary.pdf",
            mime="application/pdf",
        )
    with col3:
        # Word Download
        doc_buffer = BytesIO()
        doc = exporter.export_to_word(st.session_state.summary, st.session_state.articles)
        doc.save(doc_buffer)
        st.download_button(
            label="Download as Word",
            data=doc_buffer,
            file_name="ai_news_summary.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    with col4:
        if st.button("Send Email"):
            if sender_email and sender_password and receiver_email:
                with st.spinner("Sending email..."):
                    html_content = exporter.export_to_html(st.session_state.summary, st.session_state.articles)
                    status = email_sender.send_email(
                        sender_email, sender_password, receiver_email, 
                        smtp_server, smtp_port, 
                        "AI News Summary", html_content
                    )
                    st.info(status)
            else:
                st.error("Please fill in all email configuration fields.")


    st.header("All Articles")
    for article in st.session_state.articles:
        st.write(f"### {article['title']}")
        st.write(f"[Link]({article['link']})")
        st.write(article['summary'])
        st.divider()
