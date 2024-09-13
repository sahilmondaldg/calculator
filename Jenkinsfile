pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8'
                    args '-u root -v /c/ProgramData/Jenkins/.jenkins/workspace/pipe3:/workspace'
                }
            }
            steps {
                echo 'Starting Build...'
                sh 'python --version'
                echo 'Build stage completed.'
            }
        }

        stage('Checkout') {
            steps {
                echo 'Starting Checkout...'
                git 'https://github.com/sahilmondaldg/calculator.git'
                echo 'Checkout completed.'
            }
        }

        stage('Install Dependencies') {
            agent {
                docker {
                    image 'python:3.8'
                    args '-u root -v /c/ProgramData/Jenkins/.jenkins/workspace/pipe3:/workspace'
                }
            }
            steps {
                echo 'Starting Install Dependencies...'
                sh 'python --version'
                echo 'Upgrading pip...'
                sh 'python -m pip install --upgrade pip'
                sh '''
                if [ -f requirements.txt ]; then
                    python -m pip install -r requirements.txt
                else
                    echo "No requirements.txt found, skipping dependency installation."
                fi
                '''
                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Unit Tests') {
            agent {
                docker {
                    image 'python:3.8'
                    args '-u root -v /c/ProgramData/Jenkins/.jenkins/workspace/pipe3:/workspace'
                }
            }
            steps {
                echo 'Starting Unit Tests...'
                sh 'python --version'
                echo 'Running unit tests and generating log...'
                sh 'python -m unittest discover | tee test_results.log'
                echo 'Generating JUnit-compatible XML reports...'
                sh '''
                python -m pip install unittest-xml-reporting
                python -m xmlrunner discover -o test-results
                '''
                echo 'Unit tests completed.'
            }
        }
    }
}