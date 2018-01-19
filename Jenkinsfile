pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                bat 'docker { image 'maven:3-alpine' }'
            }
            steps {
                bat 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                bat docker '{ image 'node:7-alpine' }
            }
            steps {
                bat 'node --version'
            }
        }
    }
}