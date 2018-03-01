pipeline {
    agent {label 'slave'}
    stages {
        stage('Back-end') {
            agent {
                docker { image 'maven:3-alpine' 
                         args '-u root:root'}
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                docker { image 'node'
                         args '-u root:root' }
            }
            steps {
                sh 'node --version'
            }
        }
    }
}