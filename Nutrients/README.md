# AI-Fitness-trainer
The AI Fitness Tracker App is an innovative and interactive fitness application designed to assist users in optimizing their workout routines and form. The app leverages the power of computer vision using Mediapipe and OpenCV to provide real-time feedback and guidance on exercise performance. Whether you are a fitness enthusiast, a beginner, or someone looking to improve their workout technique, this app is your personal AI fitness trainer at your fingertips.
## Features
1.Ecxercise form tracking.\
2.Rep counting.\
3.Tutorials of each excercise (both video as well as text based tutorials)\
4.Daily Nutrition Tracker\
5.FitBot (Our chatbot)


## Getting started
1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:
``` py
pip install streamlit
pip install opencv-python mediapipe
pip install streamlit-lottie
```
3. Go to the models directory
``` py
cd models
```
4. Run the application
``` py
streamlit run 1_🏠_Home.py
```

Make the following changes in the code :
  - Make sure to use your OpenAi API key to enable the chatbot.(Change to be made in 4_🤖_Chatbot.py file)
  - Make sure to put in your email id to allow form submission.(Change to be made in 1_🏠_Home.py file)
