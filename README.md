# Heart Problem Classification 

(Heart) The most sesetive organ of human. Due to various factor People all around the world are suffering from heart problem. Problem in heart is the one of the serious and critical problem and need immidiate action to control. 
So In order to self check the problem I develop the machine learning system based on classification problem which gives 90% accuracy on giving accurate test data from the user From that we can predict initial stages of the heart problem 

## Data Description

age: The person's age in years 
sex: The person's sex (1 = male, 0 = female) 
cp: The chest pain experienced (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic) 
trtbps: The person's resting blood pressure (mm Hg on admission to the hospital) chol: The person's cholesterol measurement in mg/dl 
fbs: The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false) 
restecg: Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria) thalach: The person's maximum heart rate achieved exang: Exercise induced angina (1 = yes; 0 = no) 
oldpeak: ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot) 
slp: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping) 
caa: The number of major vessels (0-3) 
thall: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect) inherited blood disorder that causes body to have less hemoglobin than normal 
output: Heart disease (0 = no, 1 = yes)

💫 **Version 1.0**
## 📖 Require files

| Find Files                 |                                                                |
| -------------------------- | -------------------------------------------------------------- |
| 📚 **[Find notebook]**     |  Interative notebook for EDA                                   |
| 📚 **[Find Model]**        | ML model (download form link and place inside models foler)    |

[Final Model]:https://drive.google.com/file/d/1enVuG9CPkBeqcP97yoTaTGlEdzVbfIGC/view?usp=sharing
[Find notebook]:https://drive.google.com/file/d/1R0xSEuEqXJxQWMe-BlwJusBcElOtRYLU/view?usp=sharing

## Features

- Data Understanding
- Exploratory Data Analysis on the Data
- Derivation of High Level Statistics
- Visualization of various plots
- Flask API
- Html files
- Predictive Modeling using Ensemble Method
- Evaluation using Various Metrics

## 📦 Setting up the project
```bash
git clone https://github.com/bhupinbaral25/heart-problem-detection-.git
```
Set up the environment.

- **Operating system**: macOS / OS X · Linux · Windows (Cygwin, MinGW, Visual
  Studio)
- **Python version**: Python 3.9 (only 64 bit)
- **Package managers**: [venv]

[venv]: https://docs.python.org/3/library/venv.html

### virtualenv

Using pip, we can install the virtualenv package manager, make sure that
your `pip`, `setuptools` and `wheel` are up-to-date. If you already have 
venv installed, you can skip the first command.

```bash
pip install virtualenv
```
To create a virtualenv environment in linux.
```bash
virtualenv envname
```
To activate virtual environment 
```bash
source envname/bin/activate
```
### Getting the dataset

To download the dataset into the folder, use:
```bash
wget https://drive.google.com/file/d/132qGT7lTEwNXMHhXGLLpEjPWolzCtYKm/view?usp=sharing heart.csv
```
(Alternatively): Copy and open these links and download them manually.

## ⚒ Run the project

We need to activate the flask servers . 

# Run the Flask Server
```bash
python app.py
```

## Author 
Bhupin Baral
bhupinbaral.729@gmail.com



