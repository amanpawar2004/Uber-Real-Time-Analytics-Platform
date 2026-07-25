# 🚖 Uber Real-Time Analytics Platform

> **A Production-Ready Real-Time Data Engineering Project** built using **Apache Kafka, Apache Flink, Docker, Python, Streamlit, and GitHub Actions** to process live Uber ride events and visualize streaming analytics through an interactive dashboard.

---

## 📌 Project Overview

The **Uber Real-Time Analytics Platform** is an end-to-end real-time data engineering project that simulates live Uber ride booking events, streams them through **Apache Kafka**, processes the events using **Apache Flink**, stores processed data, and displays real-time business insights on a modern **Streamlit Dashboard**.

This project demonstrates industry-standard technologies and event-driven architecture commonly used in companies like **Uber, Netflix, Amazon, Swiggy, Ola, and Zomato**.

---

# 🚀 Key Features

- 🚖 Real-Time Uber Ride Event Simulation
- 📡 Apache Kafka Event Streaming
- ⚡ Apache Flink Stream Processing
- 📊 Live Analytics Dashboard
- 📈 City-wise Ride Analytics
- 💰 Fare Monitoring
- 📁 Automatic CSV Data Storage
- 🐳 Dockerized Infrastructure
- 🔄 GitHub Actions CI/CD Pipeline
- 📉 Interactive Charts & KPIs
- 🧩 Modular Project Architecture
- ⚙️ Production-Style Data Pipeline

---

# 🏗️ System Architecture

```text
                 Uber Ride Events
                        │
                        ▼
              Python Event Producer
                        │
                        ▼
                Apache Kafka Topic
                  (Uber_Rides)
                        │
                        ▼
             Apache Flink Processor
                        │
                        ▼
             Stream Processing Logic
                        │
                        ▼
                Processed CSV File
                        │
                        ▼
             Streamlit Dashboard
                        │
                        ▼
            Live Business Analytics
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Event Producer |
| Apache Kafka | Message Broker |
| Apache Flink | Stream Processing |
| Docker | Containerization |
| Streamlit | Dashboard |
| Pandas | Data Processing |
| Git | Version Control |
| GitHub Actions | CI/CD |

---

# 📂 Project Structure

```text
Uber-Real-Time-Analytics-Platform
│
├── dashboard
│   ├── app.py
│   ├── charts.py
│   ├── components.py
│   ├── utils.py
│   ├── style.css
│   ├── rides.csv
│   └── requirements.txt
│
├── docker
│   └── docker-compose.yml
│
├── flink
│   ├── ride_processor.py
│   └── requirements.txt
│
├── producer
│   ├── producer.py
│   └── requirements.txt
│
├── jars
│   └── flink-sql-connector-kafka.jar
│
├── .github
│   └── workflows
│       └── python-app.yml
│
├── README.md
└── requirements.txt
```

---

# 📈 Real-Time Data Pipeline

```text
Ride Booking Event
        │
        ▼
Python Producer
        │
        ▼
Apache Kafka
        │
        ▼
Apache Flink
        │
        ▼
Real-Time Processing
        │
        ▼
CSV Storage
        │
        ▼
Streamlit Dashboard
        │
        ▼
Business Insights
```

---

# 📊 Dashboard Features

The Streamlit dashboard provides real-time analytics including:

- ✅ Total Ride Count
- ✅ Average Fare
- ✅ City-wise Ride Distribution
- ✅ Live Ride Monitoring
- ✅ Fare Analysis
- ✅ Interactive Charts
- ✅ Real-Time Dashboard Refresh

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/amanpawar2004/Uber-Real-Time-Analytics-Platform.git
```

---

## 2️⃣ Navigate to Project

```bash
cd Uber-Real-Time-Analytics-Platform
```

---

## 3️⃣ Start Docker Containers

```bash
docker compose up -d
```

---

## 4️⃣ Start Kafka Producer

```bash
cd producer

python producer.py
```

---

## 5️⃣ Start Flink Processor

```bash
cd flink

python ride_processor.py
```

---

## 6️⃣ Launch Dashboard

```bash
cd dashboard

streamlit run app.py
```

---

# 📄 Sample Ride Event

```json
{
  "ride_id": "R6322",
  "driver_id": "D14",
  "location": "Delhi",
  "fare": 231,
  "timestamp": "2026-07-25T07:59:05"
}
```

---

# 📌 Project Highlights

- ✔ End-to-End Real-Time Data Pipeline
- ✔ Event-Driven Architecture
- ✔ Apache Kafka Streaming
- ✔ Apache Flink Processing
- ✔ Dockerized Deployment
- ✔ Interactive Streamlit Dashboard
- ✔ GitHub Actions CI/CD
- ✔ Clean Modular Code Structure
- ✔ Production-Ready Workflow

---

# 💼 Skills Demonstrated

- Python Programming
- Apache Kafka
- Apache Flink
- Stream Processing
- Data Engineering
- Docker
- Streamlit
- Data Analytics
- Event-Driven Architecture
- Git & GitHub
- GitHub Actions
- CI/CD
- Dashboard Development

---

# 🔮 Future Enhancements

- PostgreSQL Data Storage
- Apache Spark Streaming
- Redis Cache
- Prometheus Monitoring
- Grafana Dashboard
- Kubernetes Deployment
- AWS Cloud Deployment
- REST API Integration
- Machine Learning Predictions

---

# 📸 Project Screenshots

## 📊 Live Dashboard

> Add your dashboard screenshot here.
![Dashboard](![Uploading image.png…]()
)
---

## ⚡ Apache Flink Processing

> Add your Flink terminal screenshot here.

---

## 📡 Kafka Producer

> Add your Kafka producer screenshot here.
![Kafka Producer](images/kafka-producer.png)
---

## 🐳 Docker Containers

> Add your Docker Desktop screenshot here.
![Docker](images/docker-containers.png)
---

## ✅ GitHub Actions CI/CD

> Add your GitHub Actions screenshot here.
![GitHub Actions](images/github-actions.png)
---

# 🎯 Why This Project?

This project showcases the practical implementation of a **real-time event-driven data engineering pipeline**, combining streaming technologies, containerization, dashboard development, and CI/CD automation to solve real-world analytics problems.

It demonstrates industry-relevant skills expected from **Data Engineers, Data Analysts, Python Developers, and Big Data Engineers**.

---

# 👨‍💻 Author

## Aman Pawar

**Data Engineering | Python | Apache Kafka | Apache Flink | Docker | Streamlit | SQL | GitHub | Data Analytics**

📧 Email: amanpawar5100@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/aman-pawar-7a72852bb/

🌐 GitHub: https://github.com/amanpawar2004

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
