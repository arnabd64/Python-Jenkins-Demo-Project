pipeline {

    agent any

    stages {
        stage('Setup') {

            agent defaultAgent

            script {
                // create a virtual environment
                sh "python3 -m venv venv"

                // activate the environment
                sh "source venv/bin/activate"

                // install dependencies
                sh "python3 -m pip install --progress-bar off -r requirements.txt"
            }
        }

        stage('Testing') {

            agent defaultAgent

            script {
                // Run pytest
                sh "pytest"
            }
        }

        stage('Deploy') {

            agent defaultAgent

            script {
                sh "echo Deploy to the Cloud"
            }
        }
    }
}