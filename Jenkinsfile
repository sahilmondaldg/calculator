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

        stage('Install Dependencies') {
            steps {
                echo 'Starting Install Dependencies...'
                
                // Check if Python is installed and print the version
                bat 'python --version'

                // Install or upgrade pip
                echo 'Upgrading pip...'
                bat 'python -m pip install --upgrade pip'

                // Optionally, install dependencies if you have a requirements.txt file
                // Uncomment the following line if applicable
                // sh 'pip install -r requirements.txt'

                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Starting Unit Tests...'
                
                // Run the tests and print Python version for debugging
                bat 'python --version'
                
                // Run the unit tests and generate XML reports for Jenkins to parse
                echo 'Running unit tests and generating XML reports...'
                bat 'python -m unittest discover'

                // Optional: If you want to generate JUnit-compatible XML output, install `xmlrunner`
                // sh 'pip install unittest-xml-reporting'
                // sh 'python3 -m xmlrunner discover -o test-results || python -m xmlrunner discover -o test-results'

                echo 'Unit tests completed.'
            }
        }
    }

    post {
        always {
            echo 'Publishing test results...'
            junit '**/test-results/*.xml'  // This only works if XML results are generated
        }
        success {
            echo 'All stages completed successfully!'
        }
        failure {
            echo 'Pipeline failed at some stage.'
        }
    }
}
