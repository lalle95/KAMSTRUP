pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                bat 'python src/helloworld.py'
            }
        }
    }
}