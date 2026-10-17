# Containerized FastAPI GitOps CI/CD Pipeline

A production-grade, zero-cost Continuous Integration and Continuous Deployment (CI/CD) pipeline demonstrating modern DevOps practices, containerization, and GitOps workflows.

---

## Live Application & API Docs

* **Live API Endpoint:** [https://gitops-devops-app.onrender.com](https://gitops-devops-app.onrender.com)
* **Interactive API Docs (Swagger UI):** [https://gitops-devops-app.onrender.com/docs](https://gitops-devops-app.onrender.com/docs)
* **Version Endpoint:** [https://gitops-devops-app.onrender.com/version](https://gitops-devops-app.onrender.com/version)

---

## Technology Stack

* **Programming Language:** Python 3.11
* **Web Framework:** FastAPI + Uvicorn
* **Containerization:** Docker (Multi-stage build runtime)
* **Continuous Integration (CI):** GitHub Actions (`pytest`, `httpx`)
* **Continuous Deployment (CD):** Render Web Services (Webhook-triggered container builds)

---

## GitOps Architecture & Workflow

```text
[ Developer ] --( git push )--> [ GitHub Repository ]
                                        |
                 +----------------------+----------------------+
                 |                                             |
                 v                                             v
     [ GitHub Actions (CI) ]                         [ Render Hosting (CD) ]
  • Provisions Python 3.11                        • Detects push on main
  • Installs dependencies                         • Builds Docker image
  • Executes automated tests (`pytest`)           • Serves updated app live
