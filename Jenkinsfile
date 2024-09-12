pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u root'
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

        stage('Install Dependencies') {
            steps {
                echo 'Starting Install Dependencies...'

                // Check if Python is installed and print the version
                sh 'python --version'

                // Install or upgrade pip
                echo 'Upgrading pip...'
                sh 'python -m pip install --upgrade pip'

                // Install dependencies from requirements.txt (if present)
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
            steps {
                echo 'Starting Unit Tests...'

                // Print Python version for debugging
                sh 'python --version'

                // Run the unit tests and generate a log file
                echo 'Running unit tests and generating log...'
                sh 'python -m unittest discover | tee test_results.log'

                // Install the unittest-xml-reporting library and generate XML test reports
                echo 'Generating JUnit-compatible XML reports...'
                sh '''
                python -m pip install unittest-xml-reporting
                python -m xmlrunner discover -o test-results
                '''
                echo 'Unit tests completed.'
            }
        }
    }

    post {
        always {
            echo 'Publishing test results...'

            // Print the directory structure to verify that test results are present
            sh 'ls -R'

            // Publish JUnit test results if XML results are generated
            junit 'test-results/*.xml'  // Adjust the path if needed
        }
        success {
            echo 'All stages completed successfully!'
        }
        failure {
            echo 'Pipeline failed at some stage.'
        }
    }
}
