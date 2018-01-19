pipeline {
    agent none

    stages {
        stage('Build') {
            agent {
                bat docker { image 'busybox' }
            }
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            agent {
                bat docker { image 'busybox' }
            }
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            agent {
                bat docker { image 'busybox' }
            }
            steps {
                echo 'Deploying....'
            }
        }
    }
}

