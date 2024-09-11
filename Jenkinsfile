pipeline {

    agent {
        label 'defaultAgent'
    }

    stages {
        stage('Setup') {

            steps {
                // create a virtual environment
                sh "python3 -m venv venv"

                // activate the environment
                sh "source venv/bin/activate"

                // install dependencies
                sh "python3 -m pip install --progress-bar off -r requirements.txt"
            }
        }

        stage('Testing') {

            steps {
                // Run pytest
                sh "pytest"
            }
        }

        stage('Deploy') {

            steps {
                sh "echo Deploy to the Cloud"
            }
        }
    }
}
