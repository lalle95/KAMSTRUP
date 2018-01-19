pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                docker 'busybox'
            }
            steps {
                bat 'ls'
            }
        }
        stage('Front-end') {
            agent {
                docker 'busybox' 
            }
            steps {
                bat 'uptime'
            }
        }
    }
}
