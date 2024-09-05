pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git 'https://github.com/sahilmondaldg/calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python and pip if necessary
                sh 'python3 -m pip install --upgrade pip'
                
                // Optionally create a virtual environment (if your project requires it)
                // sh 'python3 -m venv venv'
                // sh '. venv/bin/activate'

                // Install dependencies (if you have any)
                // For example, if you have a requirements.txt file
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run the unit tests
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        always {
            // Publish test results
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
