# ⚙️Automated Jenkins CI/CD Pipeline using Kubernetes (Kubeadm) with SonarQube & Argo CD for Python App

Our automated CI/CD pipeline uses Kubernetes, Argo CD, Jenkins, SonarQube, PostgreSQL, Python app, DockerHub & GitHub are key components in this project. Jenkins building, testing & deploying Python apps to Kubernetes to handle application scaling & management while SonarQube ensures code quality. DockerHub hosts container images & Argo CD uses GitOps principles for seamless deployments.

# Diagram
[![Automated Jenkins CI/CD Pipeline using Kubernetes (Kubeadm) with SonarQube & Argo CD for Python App
 Zero Downtime TechTips CloudComputing DevOps DevOpsTools DevOpsPipeline DevOpsLife bjnandi biswajitnandi Biswajit Nandi](/src/main/resources/static/images/Implement%20GitLab%20CICD%20Pipeline%20on%20AWS%20ECS%20with%20RDS%20MySQL%20for%20Java%20Spring%20Boot%20Application.webp)](https://github.com/bjnandi/python-flask-postgresql-crud-application "Automated Jenkins CI/CD Pipeline using Kubernetes (Kubeadm) with SonarQube & Argo CD for Python App")

# Demo
[![Automated Jenkins CI/CD Pipeline using Kubernetes (Kubeadm) with SonarQube & Argo CD for Python App
 Zero Downtime TechTips CloudComputing DevOps DevOpsTools DevOpsPipeline DevOpsLife bjnandi biswajitnandi Biswajit Nandi](/src/main/resources/static/images/Implement%20GitLab%20CICD%20Pipeline%20on%20AWS%20ECS%20with%20RDS%20MySQL%20for%20Java%20Spring%20Boot%20Application.gif)](https://github.com/bjnandi/python-flask-postgresql-crud-application "Automated Jenkins CI/CD Pipeline using Kubernetes (Kubeadm) with SonarQube & Argo CD for Python App")


## For more Details

### ⚙️Automated Jenkins CI/CD Pipeline using Kubernetes (Kubeadm) with SonarQube & Argo CD for Python App <br>
https://medium.com/@bjnandi/%EF%B8%8Fautomated-jenkins-ci-cd-pipeline-using-kubernetes-kubeadm-with-sonarqube-argo-cd-for-python-5b55dc5d1ff8


### 📣 Follow & Show Your Support ⭐️

If you found this project helpful, please give it a star! ⭐️ It helps others discover the project and motivates us to continue improving it.

Stay updated with my latest projects and articles:

- **GitHub**: Follow me on [GitHub](https://github.com/bjnandi) to see my latest repositories and contributions.  
  [![Follow @bjnandi](https://img.shields.io/github/followers/bjnandi?label=Follow%20%40bjnandi&style=social)](https://github.com/bjnandi)

- **Medium**: Follow me on [Medium](https://medium.com/@bjnandi) to read my latest articles and insights.  
  ![Medium Badge](https://img.shields.io/badge/Medium-Follow%20Me%20on%20Medium-000?logo=medium&style=social)

<br>
Thank you for your support and interest in my work! <br>
Happy coding! 💻✨
<br><br>

**🙏 Special Thanks:** A huge thank you to [@aaravchauhan18](https://github.com/aaravchauhan18) for amazing java base [python-flask-postgresql-crud-application](https://github.com/aaravchauhan18/python-flask-postgresql-crud-application/) projects!

<hr>

# Python Flask PostgreSQL CRUD Application

This project is a web application built with Python Flask and PostgreSQL to manage student records.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/aaravchauhan18/python-flask-postgresql-crud-application.git
cd python-flask-postgresql-crud-application
```

2. **Set up the database**

Create a PostgreSQL database named crud.

```bash
CREATE TABLE students (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
phone VARCHAR(255) NOT NULL
);

INSERT INTO students (id, name, email, phone) VALUES
(1, 'Aarav Chauhan', 'aaravchauhan2211@gmail.com', '7310628048');
```

3. **Configure database settings in app.py** (e.g., DB_HOST, DB_USER, DB_PASSWORD).

4. **Install dependencies:**      
```bash
   pip install Flask psycopg2-binary

```   

4. **Start the Flask application:**

```bash
python app.py
```
