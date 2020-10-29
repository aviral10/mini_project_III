# MNIST Handwritten Digit Recognition

## This Project has been broken down into two parts:
 - Preparing the Machine Learning model for recognition of the digits
 - Using the model to predict custom drawn digits

### The GUI version of this project has been hosted online at:
​	https://www.mnistdigitrecognition.herokuapp.com 

> Note: The website has been hosted on a free server, so it might take around 1-2 minutes to load up
> completely when you open it the first time. Please have patience until it loads up and refresh it once after its done  
> :) 


## Kaggle Link:
#### If the website somehow fails, I have made the static version of the project on a Python Notebook. You can find it here 

​	https://www.kaggle.com/panda19/mnist-model

**This covers the project entirely from training of the ML model to the testing on some custom data**



### If you want to run the app-based project locally follow these instructions:

- Install Anaconda or Miniconda as we need to setup a virtual environment before installing the required libraries 
  Once you install it successfully run the following commands 
  
  `conda create --name ENV_NAME python=3.8` 
  
 - Replace ENV_NAME with any name you like, once this finishes do: 
   `conda activate ENV_NAME` 
   
 - Installing pip is optional, but pip seems to install the correct variant of tensorflow that this project requires so I would recommend using pip instead 
`conda install pip`  

 - Once inside the fully set up virtual environment, navigate to the project directory and run the following command:  

    - Install the required libraries  

       `pip install -r requirements.txt`

    - On windows  

        `python app.py`

    - On linux  

       `python3 app.py`  

  - Copy the `localhost` address and open it in your browser

### To close the project run: 
  - Hit `Ctrl+C` to close down the `app.py` running on the command line.
  - Use `conda deactivate` to deactivate the environment.
  - Use `conda activate ENV_NAME` to just activate it again if you wish to do so.