# 🚗 Vehicle Insurance Prediction – End-to-End MLOps Project

This project is a **complete end-to-end Machine Learning system** that predicts whether a customer will purchase vehicle insurance.  
It covers the full lifecycle:

- Data ingestion from MongoDB  
- Model training & experiment tracking  
- Model versioning and storage in AWS S3  
- Web app deployment using Flask  
- Docker containerization  
- CI/CD pipeline using GitHub Actions  
- Automatic deployment on AWS EC2  

This repository demonstrates a **real-world production ML workflow (MLOps)**.

---

# 📌 Problem Statement

Insurance companies need to identify customers who are likely to purchase vehicle insurance.  
The goal of this project is to build a machine learning system that predicts:

👉 Will the customer respond positively to vehicle insurance?

Output:
- **1 → Response Yes**
- **0 → Response No**

---

# 🧠 Tech Stack

## Machine Learning
- Python
- Scikit-learn
- Pandas / NumPy

## MLOps Tools
- DVC → Data & pipeline versioning  
- MLflow → Experiment tracking  
- MongoDB Atlas → Cloud data storage  
- AWS S3 → Model storage  
- Docker → Containerization  
- GitHub Actions → CI/CD  
- AWS EC2 → Deployment  

---

# 📂 Project Architecture

Data Source (MongoDB Atlas)
↓
Data Ingestion Pipeline
↓
Data Validation
↓
Data Transformation
↓
Model Training
↓
Model Saved to AWS S3
↓
Flask Web App
↓
Docker Container
↓
GitHub Actions CI/CD
↓
AWS EC2 Deployment



---

# ⚙️ Step-by-Step Journey

## 1️⃣ Project Setup

Created structured ML project architecture.

src/
├── components/
├── configuration/
├── data_access/
├── cloud_storage/
├── entity/
├── pipeline/
├── exception/
├── logger/



Implemented:
- Custom logging  
- Custom exception handling  
- Constants configuration module  

---

## 2️⃣ Data Ingestion from MongoDB Atlas

Connected pipeline to MongoDB using:
- `pymongo`
- `certifi` SSL certificates

Pipeline fetches dataset and converts it into Pandas DataFrame.

---

## 3️⃣ Data Validation & Transformation

### Validation
- Schema checks  
- Missing column checks  

### Transformation
Feature engineering + preprocessing using:
- StandardScaler
- ColumnTransformer

Generated features:
- `Vehicle_Age_lt_1_Year`
- `Vehicle_Age_gt_2_Years`
- `Vehicle_Damage_Yes`

Saved artifacts:
artifact/.../preprocessing.pkl


---

## 4️⃣ Model Training

Training pipeline performs:
- Train/test split
- Model training
- Evaluation

Saved trained model:
artifact/.../model.pkl


---

## 5️⃣ Experiment Tracking (MLflow)

Logged:
- Parameters
- Metrics
- Model versions

Ensures reproducibility and experiment comparison.

---

## 6️⃣ Model Storage in AWS S3

Configured AWS CLI + Boto3.

Training pipeline automatically uploads:
- `model.pkl`
- `preprocessing.pkl`

to S3 bucket for production usage.

---

## 7️⃣ Prediction Pipeline

Prediction workflow:
1. Load model from S3  
2. Load preprocessor  
3. Accept user input  
4. Return prediction  

---

## 8️⃣ Flask Web Application

Converted ML pipeline into web app.

### Routes

| Route | Description |
|---|---|
| `/` | Show prediction form |
| `/train` | Trigger full training |
| POST `/` | Make prediction |

---

## 9️⃣ Docker Containerization

Created Docker image for full app.

Added `.dockerignore` to exclude:
- venv
- artifacts
- notebooks
- logs

---

## 🔟 CI/CD with GitHub Actions

### Continuous Integration
On every push:
- Build Docker image
- Push image to AWS ECR

### Continuous Deployment
On EC2 self-hosted runner:
- Pull latest image
- Stop old container
- Run new container automatically

Deployment is fully automated 🚀

---

# ☁️ AWS Infrastructure

| Service | Purpose |
|---|---|
| AWS S3 | Model storage |
| AWS ECR | Docker registry |
| AWS EC2 | Application hosting |

---

# 🔐 GitHub Secrets

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
MONGODB_URL








---

# 🚀 Run Locally

### Clone repo
```bash
git clone <repo-url>
cd Vehicle-insurance-domain


#create v-env
python -m venv venv
venv\Scripts\activate
#install dependencies
pip install -r requirements.txt
#run flask
python app.py


### Deployment

# After CI/CD setup, app runs automatically on EC2:
 http://<EC2_PUBLIC_IP>:5000
 