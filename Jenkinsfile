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
                script {
                    def pythonCmd = sh(script: 'which python3 || which python || echo "Python not found"', returnStdout: true).trim()
                    if (pythonCmd == "Python not found") {
                        error "Python is not installed or not in PATH"
                    } else {
                        echo "Using Python: ${pythonCmd}"
                        sh "${pythonCmd} --version"
                        sh "${pythonCmd} -m venv venv || ${pythonCmd} -m virtualenv venv"
                        sh ". venv/bin/activate"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Starting Install Dependencies...'
                script {
                    def pythonCmd = sh(script: 'which python3 || which python || echo "Python not found"', returnStdout: true).trim()
                    sh """
                    . venv/bin/activate
                    ${pythonCmd} -m pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        ${pythonCmd} -m pip install -r requirements.txt
                    else
                        echo "No requirements.txt found, skipping dependency installation."
                    fi
                    """
                }
                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Starting Unit Tests...'
                script {
                    def pythonCmd = sh(script: 'which python3 || which python || echo "Python not found"', returnStdout: true).trim()
                    sh """
                    . venv/bin/activate
                    ${pythonCmd} -m unittest discover | tee test_results.log
                    ${pythonCmd} -m pip install unittest-xml-reporting
                    ${pythonCmd} -m xmlrunner discover -o test-results
                    """
                }
                echo 'Unit tests completed.'
            }
        }
    }
}