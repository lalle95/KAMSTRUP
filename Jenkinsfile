pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                docker 'maven:7-alpine'
            }
            steps {
                bat 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                docker 'node:7-alpine' 
            }
            steps {
                bat 'node --version'
            }
        }
    }
}