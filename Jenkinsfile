pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t jenkins-python-basic .'
            }
        }

        stage('Run App') {
            steps {
                echo 'Running Python app...'
                sh 'docker run --rm jenkins-python-basic'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'docker run --rm jenkins-python-basic pytest test_app.py'
            }
        }
    }
}
