# CloudOps DevOps Platform

A hands-on DevOps and cloud engineering project demonstrating the end-to-end lifecycle of a containerised application, from development and automated testing to CI/CD, cloud deployment, infrastructure as code, and observability.

## Current Architecture

Developer
↓
GitHub
↓
GitHub Actions
↓
Automated Tests
↓
Docker Build
↓
Cloud Deployment

## Tech Stack

- Python
- FastAPI
- Pytest
- Docker
- Git & GitHub
- GitHub Actions
- Microsoft Azure
- Terraform (planned)
- Azure Monitor (planned)
- Kubernetes / AKS (planned)

## Features

- FastAPI REST service
- Health check endpoint
- Readiness endpoint
- Automated API testing with Pytest
- Dockerised application
- GitHub Actions CI pipeline
- Automated testing on every push to `main`
- Automated Docker image build after successful tests
- CI pipeline failure detection demonstrated through a simulated regression

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Service information |
| GET | `/health` | Application health check |
| GET | `/ready` | Application readiness check |
| GET | `/docs` | Interactive Swagger API documentation |

## Run Locally

### Install dependencies

```bash
pip install -r requirements.txt