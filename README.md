# P81-DevOps-Task

## FastAPI Application with Terragrunt and Terraform

This repository contains a FastAPI application designed for processing and verifying product data. The infrastructure is managed using Terragrunt and Terraform. Continuous Integration and Deployment are handled through GitHub Actions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before starting, ensure you have the following installed:
- Python 3.10 or higher
- Terraform
- Terragrunt
- AWS CLI (configured with credentials)

### Installing and Running Locally

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/BirmaNator/P81-AWS-Infra-Task.git
    cd P81-AWS-Infra-Task
    ```

2. **Setting up Infrastructure on AWS with Terraform and Terragrunt**:

    Navigate to the Terragrunt configuration directory:

    ```bash
    cd terraform-terragrunt/live/prod
    terragrunt init
    terragrunt apply
    ```

    **Note**: It's necessary to have AWS CLI configured with a user that has the appropriate permissions for managing the required AWS resources. This typically involves setting up an IAM user with sufficient privileges and configuring AWS CLI with the user's access key and secret key.

3. **Running the Application Locally**:

    It's recommended to run the application in a virtual environment. To set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Define an environment variable with the CloudFront URL and attach `https://` to it:

    ```bash
    export CLOUDFRONT_URL="https://your-cloudfront-url-here"
    ```

    Run the FastAPI application:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 80
    ```

    The application will be accessible at `http://localhost`.

### GitHub Actions Workflow

This project uses GitHub Actions for Continuous Integration and Deployment. The workflow includes the following steps:

- **Infrastructure Deployment**: On push to the main branch or manual trigger, the workflow deploys the infrastructure using Terragrunt.
- **FastAPI Application Deployment**: After successful infrastructure deployment, the workflow triggers the FastAPI application.
- **Configure Secretes**: The workflow can be executed only when adding AWS_ACCESS_KEY_ID && AWS_SECRET_ACCESS_KEY as secrets for github actions.
- **Automated Testing**: The workflow can be extended to include automated testing of the application endpoints.

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Terragrunt](https://terragrunt.gruntwork.io/) - Infrastructure as Code tool
- [Terraform](https://www.terraform.io/) - Infrastructure provisioning tool
