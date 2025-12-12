// Sprawdzamy instlal Python jako cocker


pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Test Python') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }
    }
}
