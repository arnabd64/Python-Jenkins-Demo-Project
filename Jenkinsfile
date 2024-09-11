pipeline {
    agent none

    environment {
        GIT_REPO = 'https://github.com/arnabd64/Python-Jenkins-Demo-Project.git'
    }

    stages {
        stage('Checkout') {
            agent {
                docker {
                    image "python:3.11-slim-bookworm"
                }
            }
            steps {
                git "$env.GIT_REPO_URL"
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    bash "pip install -r requirements.txt"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    bash "uvicorn app:app --host=0.0.0.0"
                }
            }
        }

    }
    
    post {
        always {
            cleanWs()
        }
    }
}