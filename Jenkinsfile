pipeline {
    agent {
        docker {
            image 'python:3.11'  // You can change this to a specific Python version if needed
            args '/mnt/c/ProgramData/Jenkins/.jenkins/workspace/pipe3/'
        }
    }

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
                sh 'python --version'
                sh 'pip install virtualenv'
                sh 'virtualenv venv'
                sh '. venv/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Starting Install Dependencies...'
                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
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
                sh '''
                . venv/bin/activate
                python -m unittest discover | tee test_results.log
                pip install unittest-xml-reporting
                python -m xmlrunner discover -o test-results
                '''
                echo 'Unit tests completed.'
            }
        }
    }
}