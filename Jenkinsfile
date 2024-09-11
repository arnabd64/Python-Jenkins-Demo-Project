pipeline {

    agent {
        docker {
            image 'python:3.11-slim-bookworm'
            label 'my-python-agent'
        }
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
