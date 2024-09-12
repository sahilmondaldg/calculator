pipeline {
    agent {
        docker {
            image 'python:3.11' // Specify the Python Docker image version
            args '-u root'           // Optional: Run as root to avoid permission issues
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
                bat 'python --version'

                // Install or upgrade pip
                echo 'Upgrading pip...'
                bat 'python -m pip install --upgrade pip'

                // Install dependencies from requirements.txt (if present)
                bat '''
                if exist requirements.txt (
                    python -m pip install -r requirements.txt
                ) else (
                    echo "No requirements.txt found, skipping dependency installation."
                )
                '''
                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Starting Unit Tests...'

                // Print Python version for debugging
                bat 'python --version'

                // Run the unit tests and generate a log file
                echo 'Running unit tests and generating XML reports...'
                bat 'python -m unittest discover > test_results.log'
                bat 'type test_results.log'  // Print the test results log

                // Optional: Generate JUnit-compatible XML output
                bat '''
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
            bat 'dir /S'

            // Publish JUnit test results if XML results are generated
            junit 'test-results\\*.xml'  // Adjust the path if needed
        }
        success {
            echo 'All stages completed successfully!'
        }
        failure {
            echo 'Pipeline failed at some stage.'
        }
    }
}
