pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                docker 'busybox'
            }
            steps {
                sh 'ls'
            }
        }
        stage('Front-end') {
            agent {
                docker 'busybox' 
            }
            steps {
                sh 'uptime'
            }
        }
    }
}
