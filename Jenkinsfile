pipeline {
    agent any

    stages {
        stage('Run App') {
            steps {
                echo 'Running app from minfy-app image...'
                sh 'docker run --rm minfy-app:latest'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests inside Docker container...'
                sh 'docker run --rm minfy-app:latest pytest test_app.py'
            }
        }
    }
}
