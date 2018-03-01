pipeline {
    agent {label 'slave'}
    stages {
        stage('Back-end') {
            agent {
                docker { image 'maven:3-alpine' }
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                docker { image 'node' }
            }
            steps {
                sh 'node --version'
            }
        }
    }
}