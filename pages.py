import streamlit as st
from PIL import Image
import pandas as pd
import os
import base64
from streamlit.components.v1 import html

st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center ;font-size: 70px; color: white;'>Nakarin Sariten</h1>", unsafe_allow_html=True)
st.markdown("<h7 style='text-align: center ; color: white;'>I am deep passion and enthusiasm for the field of data. With a strong background in industrial engineering and extensive experience in analyzing data, building machine learning models, and implementing advanced analytics techniques, I am driven to unlock valuable insights and drive data-centric innovation., constantly seeking new challenges and opportunities to apply expertise in data analysis and machine learning to drive innovation and business success.</h7>", unsafe_allow_html=True)

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
    
    
@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data()
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code

url = "https://github.com/Nakarin225/Home-Credit-Default-Risk-analysis"
gif_html = get_img_with_href('Img/icons8-github-60.png', 'https://github.com/Nakarin225?tab=repositories')
medium_html = get_img_with_href('Img/icons8-medium-64.png', ' https://medium.com/@nakarinsariten')
#st.markdown(gif_html, unsafe_allow_html=True)

c1, c2,c3,c4 ,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15= st.columns(15,gap="small")
with c7:
    st.markdown(gif_html, unsafe_allow_html=True)

with c8: 
    st.markdown("[![Title](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)](<https://www.linkedin.com/in/nakarin-sariten/>)")
with c9:
    st.markdown(medium_html, unsafe_allow_html=True)
    
st.markdown("<h3 style='text-align: center ;font-size: 50px; color: white;'>Data Projects</h3>", unsafe_allow_html=True)

col1, col2 , col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center; color: white;'>Home Credit Default Risk</h3>", unsafe_allow_html=True)
    with st.container():
        st.image("Img/home.jpg")
        st.markdown("<h10 style='text-align: center; color: white;'>Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders.</h10>", unsafe_allow_html=True)
        st.markdown("<h10 style='text-align: center; color: white;'>Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.</h10>", unsafe_allow_html=True)
        st.button('Full code Github', on_click=open_page, args=('https://github.com/Nakarin225/Home-Credit-Default-Risk-analysis',))
        expander = st.expander("Additional Story")
        expander.markdown("<h10 style='text-align: center; color: white;'>Classification: The label is a binary variable, 0 (will repay loan on time), 1 (will have difficulty repaying loan) 121 features </h10>", unsafe_allow_html=True)
        df = pd.read_csv("Data/testdata.csv")
        expander.markdown("<h10 style='text-align: center; color: white;'>Sample data</h10>", unsafe_allow_html=True)
        expander.dataframe(df, use_container_width=True)
        image1 = Image.open('Img/chart1.png')
        image2 = Image.open('Img/chart2.png')
        image3 = Image.open('Img/Roc_curve.png')
        expander.markdown("<h10 style='text-align: center; color: white;'>Top Applicant's who applied for loan</h10>",unsafe_allow_html=True)
        expander.markdown("<h10 style='text-align: center; color: white;'>Laborers - Apprx. 55 K",unsafe_allow_html=True)
        expander.markdown("<h10 style='text-align: center; color: white;'>Sales Staff - Approx. 32 K",unsafe_allow_html=True)
        expander.markdown("<h10 style='text-align: center; color: white;'>Core staff - Approx. 28 K",unsafe_allow_html=True)
        expander.markdown("<h10 style='text-align: center; color: white;'>Managers - Approx. 21 K",unsafe_allow_html=True)
        expander.image(image1,)
        expander.markdown("<h10 style='text-align: center; color: white;'>Approx. 89 % peoples applied for loan, they mentioned type of house is House / Appartment.",unsafe_allow_html=True)
        expander.image(image2,)
        expander.markdown("<h10 style='text-align: center; color: white;'>Metric: ROC AUC",unsafe_allow_html=True)
        expander.image(image3,)
        expander.markdown("<h10 style='text-align: center; color: white;'>When we measure a classifier according to the ROC AUC, we do not generation 0 or 1 predictions, but rather a probability between 0 and 1. This may be confusing because we usually like to think in terms of accuracy, but when we get into problems with inbalanced classes (we will see this is the case), accuracy is not the best metric. For example, if I wanted to build a model that could detect terrorists with 99.9999% accuracy, I would simply make a model that predicted every single person was not a terrorist. Clearly, this would not be effective (the recall would be zero) and we use more advanced metrics such as ROC AUC or the F1 score to more accurately reflect the performance of a classifier. A model with a high ROC AUC will also have a high accuracy, but the ROC AUC is a better representation of model performance.</h10>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3 style='text-align: center; color: white;'>Predict student performance</h3>", unsafe_allow_html=True)
    with st.container():
        st.image("Img/student.jpg")
        st.markdown("<h10 style='text-align: center; color: white;'>An end-to-end machine learning project typically involves several stages: data collection and preprocessing, model training and evaluation, deployment, and building a web application for prediction. I'll explain the steps involved in creating an end-to-end machine learning project to predict the scores of students using Flask and AWS.</h10>", unsafe_allow_html=True)
        st.button('Full code Github ', on_click=open_page, args=('https://github.com/Nakarin225/End-to-End-MLproject-to-predict-student-performance',))


        
with col3:
    st.markdown("<h3 style='text-align: center; color: white;'>Online Retail Analysis</h3>", unsafe_allow_html=True)
    with st.container():
        st.image("Img/retail.jpg")
        st.markdown("<h10 style='text-align: center; color: white;'>This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.</h10>", unsafe_allow_html=True)
        st.button('Full code Github  ', on_click=open_page, args=('https://github.com/Nakarin225/onlineretail_analysis',))
        st.button('PowerBI Dashboard', on_click=open_page, args=('https://app.powerbi.com/singleSignOn?ru=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1',))
        expander1 = st.expander("Additional Story ")
        expander1.markdown("<h10 style='text-align: center; color: white;'>Cohort Analysis (Retention over User & Product Lifetime)</h10>", unsafe_allow_html=True)
        expander1.markdown("<h10 style='text-align: center; color: white;'>Cohort analysis is a technique used in data analysis to understand the behavior and characteristics of a specific group of customers</h10>", unsafe_allow_html=True)
        expander1.image("Img/cohort.png")
        expander1.markdown("<h10 style='text-align: center; color: white;'>The RFM model is a customer segmentation technique used in marketing and customer relationship management</h10>", unsafe_allow_html=True)
        expander1.markdown("<h10 style='text-align: center; color: white;'>- Recency (R): Recency measures the time since a customer's last purchase </h10>", unsafe_allow_html=True)
        expander1.markdown("<h10 style='text-align: center; color: white;'>- Frequency (F): Frequency refers to how often a customer makes purchases </h10>", unsafe_allow_html=True)
        expander1.markdown("<h10 style='text-align: center; color: white;'>- Monetary Value (M): Monetary Value represents the total amount of money a customer has spent on purchases </h10>", unsafe_allow_html=True)
        expander1.image("Img/rfm.png")
        expander1.markdown("<h10 style='text-align: center; color: white;'>Result it have 3 cluster groups</h10>", unsafe_allow_html=True)
        expander1.markdown("<h10 style='text-align: center; color: white;'>Bronze customers are a group of new users who have not yet decided whether to purchase our product vs those of competitors.</h10>", unsafe_allow_html=True)
        expander1.markdown("<h10 style='text-align: center; color: white;'>Silver Customers are a group who often make small purchases; therefore, we are able to focus on promotions to raise ticket size.</h10>", unsafe_allow_html=True)
        expander1.markdown("<h10 style='text-align: center; color: white;'>Gold Customer is group is Big spender and royalty should maintain this group high impact on business.</h10>", unsafe_allow_html=True)
        expander1.image("Img/cluster.png")
