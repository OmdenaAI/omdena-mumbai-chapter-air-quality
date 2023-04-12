import streamlit as st
import base64
from styles import streamlit_style

streamlit_style()

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def home():
	# Add background
	add_bg_from_local('bg.jpg') 

	_, c2, _ = st.columns([1, 8, 1])
	with c2:
		# Insert the PNG image in the center of the page
		st.image('aerohue-transparent.png')

	st.markdown("<div class='centered'>", unsafe_allow_html=True)

	# Add heading and introductory text
	st.markdown("<h1 style='color:#4CAF50; text-align: center;'>Welcome to AeroHue</h1>", unsafe_allow_html=True)
	st.write(" ")
	st.markdown("<p style='color:#333333; font-size:18px;'>At AeroHue, we're committed to helping you breathe easier by providing you with the information you need to ensure that the air you're breathing is clean and healthy. Our easy-to-use web application allows you to monitor air quality in real-time and take steps to improve it if necessary.</p>", unsafe_allow_html=True)
	st.write(" ")
	st.write("Hunter ")

	# Add section for real-time air quality monitoring
	st.markdown("<h3 style='color:#4CAF50;'>Real-Time Air Quality Monitoring</h3>", unsafe_allow_html=True)
	st.markdown("<p style='color:#333333; font-size:16px;'>Our web application provides real-time air quality data for your location. You can easily check the air quality index (AQI) and the levels of common pollutants such as particulate matter (PM2.5 and PM10), ozone (O3), nitrogen dioxide (NO2), and sulfur dioxide (SO2). Our data is sourced from reputable air quality monitoring agencies, so you can trust the accuracy of our information.</p>", unsafe_allow_html=True)
	st.markdown("<p style='color:#333333; font-size:16px;'>With AeroHue, you can stay up-to-date on the air quality in your area and make informed decisions about your outdoor activities, travel plans, and more. Our user-friendly interface makes it easy to understand and interpret air quality data, so you can stay safe and healthy no matter where you are.</p>", unsafe_allow_html=True)
	st.write(" ")
	st.write(" ")

	# Add section for personalized air quality recommendations
	st.markdown("<h3 style='color:#4CAF50;'>Personalized Air Quality Recommendations</h3>", unsafe_allow_html=True)
	st.markdown("<p style='color:#333333; font-size:16px;'>Based on your location and the current air quality data, AeroHue provides personalized recommendations for improving your air quality. We'll suggest actions you can take to reduce your exposure to pollutants, such as using air purifiers or avoiding outdoor exercise during peak pollution hours. With AeroHue, you can take control of your air quality and protect your health.</p>", unsafe_allow_html=True)
	st.markdown("<p style='color:#333333; font-size:16px;'>Our recommendations are tailored to your specific needs and preferences, taking into account factors like your age, health status, and lifestyle habits. We'll help you make small changes that can have a big impact on your air quality, so you can breathe easier and live better.</p>", unsafe_allow_html=True)
	st.write(" ")
	st.write(" ")

	# Add section for easy-to-use dashboard and alert system
	st.markdown("<h3 style='color:#4CAF50;'>Easy-to-Use Dashboard and Alert System</h3>", unsafe_allow_html=True)
	st.markdown("<p style='color:#333333; font-size:16px;'>Our user-friendly dashboard provides you with all the information you need to monitor your air quality and take action if necessary. You can view real-time data, track trends over time, and receive alerts when air quality levels become unhealthy. Our alert system can send notifications to your phone or email, so you can stay informed even when you're on the go.</p>", unsafe_allow_html=True)
	st.markdown("<p style='color:#333333; font-size:16px;'>Our dashboard is customizable, so you can choose the metrics that are most important to you and track them over time. You can also view historical data to identify patterns and trends in air quality, which can help you make more informed decisions about your daily activities.</p>", unsafe_allow_html=True)
	st.write(" ")
	st.write(" ")

	# Add call to action
	st.markdown("<h3 style='color:#4CAF50;'>Get Started with AeroHue Today</h3>", unsafe_allow_html=True)
	st.markdown("<p style='color:#333333; font-size:16px;'>Join the millions of people around the world who are using AeroHue to monitor and improve their air quality. Our web application is free and easy to use, and it can help you breathe easier and live healthier. Sign up today and start taking control of your air quality!</p>", unsafe_allow_html=True)
	st.write(" ")
	st.markdown("<a href='#'><button style='background-color:#4CAF50; color:#FFFFFF; padding:10px 20px; border:none; border-radius:5px; font-size:16px;'>Sign Up Now</button></a>", unsafe_allow_html=True)
	st.write(" ")
	st.write(" ")

	# Close centered content div
	st.markdown("</div>", unsafe_allow_html=True)


# Define function for Air Quality Prediction page
def air_quality_prediction():
    st.header("Air Quality Prediction")
    st.write("This page will show you the predicted air quality for your location based on historical data and machine learning algorithms.")

# Define function for Real-time AQI Monitoring page
def real_time_aqi_monitoring():
    st.header("Real-time AQI Monitoring")
    st.write("This page will show you the current air quality index (AQI) for your location in real-time, based on data from sensors and other sources.")


# Create sidebar with navigation links
st.sidebar.markdown("<h1 style='color:#000000; text-align: center;'>Navigator</h1>", unsafe_allow_html=True)

st.sidebar.write(" ")
st.sidebar.image('aerohue-black.png')

st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.markdown("<h1 style='color:#000000; text-align: center;'>Select Page</h1>", unsafe_allow_html=True)
page = st.sidebar.radio(" ", ("Home", "Air Quality Prediction", "Real-time AQI Monitoring"))


# Call appropriate page based on navigation link selection
def main():

	if page == "Home":
		home()
	elif page == "Air Quality Prediction":
		air_quality_prediction()
	elif page == "Real-time AQI Monitoring":
		real_time_aqi_monitoring()


if __name__ == "__main__":
	main()
