# scripts/ci_cd.py
import subprocess
import os
import logging
from config_loader import load_config_from_file
from taipy import Core

# Set up logging
logging.basicConfig(filename='ci_cd_log.txt', level=logging.ERROR)

def fetch_source_code():
    try:
        subprocess.run(["git", "clone", "https://github.com/surfiniaburger/takeMed.git"])
        print("Source code fetched successfully.")
    except subprocess.CalledProcessError as e:
        error_message = f"Error fetching source code: {e}"
        print(error_message)
        logging.error(error_message)

def perform_unit_tests():
    try:
        subprocess.run(["pytest", "tests/unit"])
        print("Unit tests passed successfully.")
    except subprocess.CalledProcessError as e:
        error_message = f"Unit tests failed: {e}"
        print(error_message)
        logging.error(error_message)

def perform_integration_tests():
    try:
        subprocess.run(["pytest", "tests/integration"])
        print("Integration tests passed successfully.")
    except subprocess.CalledProcessError as e:
        error_message = f"Integration tests failed: {e}"
        print(error_message)
        logging.error(error_message)

def build_artifact():
    try:
        subprocess.run(["python", "setup.py", "sdist"])
        print("Artifact built successfully.")
    except subprocess.CalledProcessError as e:
        error_message = f"Error building artifact: {e}"
        print(error_message)
        logging.error(error_message)

def deploy_to_staging():
    try:
        subprocess.run(["ansible-playbook", "-i", "ansible/staging_inventory.ini", "ansible/deploy.yml"])
        print("Deployment to staging environment completed successfully.")
    except subprocess.CalledProcessError as e:
        error_message = f"Error deploying to staging environment: {e}"
        print(error_message)
        logging.error(error_message)

def deploy_to_production():
    try:
        subprocess.run(["ansible-playbook", "-i", "ansible/production_inventory.ini", "ansible/deploy.yml"])
        print("Deployment to production environment completed successfully.")
    except subprocess.CalledProcessError as e:
        error_message = f"Error deploying to production environment: {e}"
        print(error_message)
        logging.error(error_message)

def run_ci_cd_pipeline():
    fetch_source_code()
    perform_unit_tests()
    perform_integration_tests()
    build_artifact()
    deploy_to_staging()
    deploy_to_production()

if __name__ == "__main__":
    # Load configuration
    config = load_config_from_file("config.yaml")

    # Initialize CI/CD pipeline with configuration
    ci_cd_pipeline = Core()

    # Start your CI/CD pipeline
    ci_cd_pipeline.run()
