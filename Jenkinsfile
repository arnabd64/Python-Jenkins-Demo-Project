pipeline {

    agent {
        node {
            label 'defaultAgent'
            customWorkspace '/tmp/python_project'
        }
    }

    stages {
        stage('System Info') {
            steps {
                echo "$(uname -a)"
                echo "$(python3 --version)"
            }
        }

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
                echo "Deploy to the Cloud"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
