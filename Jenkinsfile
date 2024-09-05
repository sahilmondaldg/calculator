pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sahilmondaldg/calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Upgrade pip and install dependencies
                sh 'python3 -m pip install --upgrade pip'
                // Uncomment if you have requirements.txt
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Check Python version for debugging
                sh 'python3 --version'
                
                // Run the unit tests and generate XML reports
                sh 'python3 -m xmlrunner discover -o test-results'
            }
        }
    }

    post {
        always {
            // Publish test results (JUnit XML format)
            junit '**/test-results/*.xml'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}
