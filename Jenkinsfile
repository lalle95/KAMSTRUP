pipeline {
    agent 'busybox'
    stages {
        stage('Back-end') {
            steps {
                bat 'ls'
            }
        }
        stage('Front-end') {
            steps {
                bat 'uptime'
            }
        }
    }
}
