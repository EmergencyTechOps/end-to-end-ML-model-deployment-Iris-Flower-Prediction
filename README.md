

# **End-to-End ML Model Deployment with Flask and Docker**

This repository provides a complete setup for building, training, and deploying a machine learning model with a user interface, containerized using Docker, and hosted on an Ubuntu EC2 instance.

---
## **Command to Download Dataset:**
```bash

wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data -O iris.csv
```
## **1. System Requirements**

### **EC2 Instance Requirements**  
- Instance Type: `t2.medium` (minimum)  
- OS: Ubuntu 20.04 or 22.04  
- Storage: 20 GB EBS Volume  
- Network: Open ports `22` (SSH) and `5000` (Flask API/UI).

### **Packages to Install on EC2**
- Python 3 and pip  
- Docker  
- Required Python libraries: `pandas`, `scikit-learn`, `joblib`  

---

## **2. Commands to Set Up EC2**

### **Connect to EC2 Instance**
Use SSH to connect to your Ubuntu-based EC2 instance:
```bash
ssh -i your-key.pem ubuntu@<EC2-Public-IP>
```

---

### **Install System Dependencies**

1. **Update Ubuntu and Install Python 3**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-pip python3-venv -y
   ```

2. **Install Docker**:
   ```bash
   sudo apt install docker.io -y
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. **Install Required Python Libraries** (system-wide):
   ```bash
   sudo apt install python3-pandas python3-sklearn python3-joblib -y
   ```

---

## **3. Project Setup**

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Train the Model**:
   Run the `train_model.py` script to train the model and save it as `iris_model.pkl`:
   ```bash
   python3 train_model.py
   ```

---

## **4. Build and Run Docker Container**

1. **Build the Docker Image**:
   ```bash
   sudo docker build -t iris-predictor .
   ```

2. **Run the Docker Container**:
   ```bash
   sudo docker run -d -p 5000:5000 iris-predictor
   ```

---

## **5. Access the Application**

Once the container is running:
- Open your browser and go to:
   ```
   http://<EC2-Public-IP>:5000
   ```

- You can now use the user interface to enter input values and see the predictions.

---

## **6. API Testing**

You can test the API directly using `curl` or tools like Postman.

### **Example `curl` Command**:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '[{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}]' \
http://<EC2-Public-IP>:5000/predict
```

**Expected Output**:
```json
{"prediction": ["Iris-setosa"]}
```

---

## **7. Security Group Configuration**

While setting up the EC2 instance, ensure the following ports are open:

| Type          | Protocol | Port Range | Source           | Description            |
|---------------|----------|------------|------------------|------------------------|
| SSH           | TCP      | 22         | My IP (0.0.0.0/0)| To connect to EC2      |
| Custom TCP    | TCP      | 5000       | 0.0.0.0/0        | Flask API/UI access    |

---

## **8. Project Files**

| File Name         | Description                                      |
|--------------------|--------------------------------------------------|
| `train_model.py`   | Script to train the ML model and save it.        |
| `app.py`           | Flask API to serve predictions.                  |
| `templates/index.html` | Simple UI to interact with the API.          |
| `Dockerfile`       | Dockerfile to containerize the application.      |

---

## **9. Clean Up**

To stop and remove the Docker container:
```bash
sudo docker ps
sudo docker stop <container-id>
sudo docker rm <container-id>
```

---

## **10. Next Steps**
1. Extend the UI for better styling.
2. Explore deploying the Docker container using Kubernetes for scalability.

---




