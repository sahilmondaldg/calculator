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

        stage('Build and Test') {
            agent {
                docker {
                    image 'python:3.8'
                    args '-v %CD%:C:\\workspace'
                    reuseNode true
                }
            }
            steps {
                echo 'Starting Build and Test...'
                bat 'python --version'
                bat 'dir'
                bat 'python -m pip install --upgrade pip'
                bat '''
                if exist requirements.txt (
                    python -m pip install -r requirements.txt
                ) else (
                    echo No requirements.txt found, skipping dependency installation.
                )
                '''
                bat 'python -m unittest discover'
                bat '''
                python -m pip install unittest-xml-reporting
                python -m xmlrunner discover -o test-results
                '''
                echo 'Build and Test completed.'
            }
        }
    }

}