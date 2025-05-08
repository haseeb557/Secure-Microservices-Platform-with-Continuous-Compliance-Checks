# Secure Microservices Platform with Continuous Compliance Checks

![GitHub Actions](https://img.shields.io/github/workflow/status/haseeb557/Secure-Microservices-Platform-with-Continuous-Compliance-Checks/CI)

## 📌 Project Overview

This project implements a secure, scalable, cloud-native microservices platform built using DevOps and DevSecOps best practices. It integrates:

- Microservices containerization (Docker + ECS)
- Infrastructure as Code (Terraform on AWS)
- Continuous integration/deployment (GitHub Actions)


---

## 🎯 Objectives

- Develop containerized microservices (Flask)
- Automate infrastructure provisioning using Terraform
- Build CI/CD pipelines for testing and deployment
- Implement compliance scripts to detect misconfigurations
- Set up real-time monitoring and Slack-based alerting

---

## 🧱 Project Structure

```bash
secure-microservices-compliance-platform/
├── infra/                  # Terraform scripts for AWS resources
├── services/               # Flask-based microservices
│   ├── auth/
│   ├── billing/
│   └── product/
├── scripts/                # Bash/Python for backups and compliance checks
├── .github/workflows/      # GitHub Actions CI/CD pipelines
└── README.md

