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
                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Starting Install Dependencies...'
                sh 'python3 -m pip install --upgrade pip'
                sh '''
                if [ -f requirements.txt ]; then
                    python3 -m pip install -r requirements.txt
                else
                    echo "No requirements.txt found, skipping dependency installation."
                fi
                '''
                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Starting Unit Tests...'
                sh 'python3 -m unittest discover | tee test_results.log'
                echo 'Generating JUnit-compatible XML reports...'
                sh '''
                python3 -m pip install unittest-xml-reporting
                python3 -m xmlrunner discover -o test-results
                '''
                echo 'Unit tests completed.'
            }
        }
    }
}