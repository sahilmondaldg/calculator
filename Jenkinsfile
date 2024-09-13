pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Starting Checkout...'
                git 'https://github.com/sahilmondaldg/calculator.git'
                echo 'Checkout completed.'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment...'
                bat 'python --version'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Starting Install Dependencies...'
                bat 'python -m pip install --upgrade pip'
                bat '''
                if exist requirements.txt (
                    python -m pip install -r requirements.txt
                ) else (
                    echo No requirements.txt found, skipping dependency installation.
                )
                '''
                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Starting Unit Tests...'
                bat 'python -m unittest discover > test_results.log'
                echo 'Generating JUnit-compatible XML reports...'
                bat '''
                python -m pip install unittest-xml-reporting
                python -m xmlrunner discover -o test-results
                '''
                echo 'Unit tests completed.'
            }
        }
    }
}