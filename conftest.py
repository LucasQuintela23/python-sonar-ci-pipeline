"""
pytest configuration file for adding environment information to tests.

This file configures pytest to include environment metadata in Allure reports.
"""

import os
import sys
import json
import pytest
import allure
from pathlib import Path


def pytest_configure(config):
    """Configure pytest with environment markers and variables."""
    config.addinivalue_line(
        "markers", "staging: mark test as staging environment test"
    )
    config.addinivalue_line(
        "markers", "production: mark test as production environment test"
    )
    config.addinivalue_line(
        "markers", "development: mark test as development environment test"
    )
    
    # Criar arquivo de environment para Allure
    environment = os.getenv("TEST_ENVIRONMENT", "development").upper()
    
    # Estrutura de diretório para allure
    allure_dir = Path("allure-results")
    allure_dir.mkdir(exist_ok=True)
    
    # Criar arquivo de ambiente (sem usar allure.environment que não existe)
    environment_data = {
        "Environment": environment,
        "Python": sys.version.split()[0],
        "Platform": sys.platform,
        "Test Type": "API/Unit Tests"
    }
    
    # Escrever para arquivo environment.json se allure-results existir
    env_file = allure_dir / "environment.properties"
    try:
        with open(env_file, "w") as f:
            for key, value in environment_data.items():
                f.write(f"{key}={value}\n")
    except Exception:
        pass  # Se falhar, continua mesmo assim


@pytest.fixture(scope="session", autouse=True)
def environment_info():
    """Add environment information to each test."""
    environment = os.getenv("TEST_ENVIRONMENT", "development")
    allure.dynamic.parameter("Environment", environment)
