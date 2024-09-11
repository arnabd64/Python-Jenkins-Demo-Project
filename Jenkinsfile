pipeline {

    agent any

    stages {
        stage('Setup') {

            agent defaultAgent

            steps {
                // create a virtual environment
                "python3 -m venv venv"

                // activate the environment
                "source venv/bin/activate"

                // install dependencies
                "python3 -m pip install --progress-bar off -r requirements.txt"
            }
        }

        stage('Testing') {

            agent defaultAgent

            steps {
                // Run pytest
                "pytest"
            }
        }

        stage('Deploy') {

            agent defaultAgent

            steps {
                "echo Deploy to the Cloud"
            }
        }
    }
}