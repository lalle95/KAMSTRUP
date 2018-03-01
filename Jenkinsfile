pipeline {
    agent {label 'slave'}
    stages {
        stage('Back-end') {
            agent {
                label 'slave'
                docker { image 'maven:3-alpine' }
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                label 'slave'
                docker { image 'node:7-alpine' }
            }
            steps {
                sh 'node --version'
            }
        }
    }
}