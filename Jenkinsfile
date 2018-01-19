pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
            }
        }
        stage('test') {
            steps {
                sh 'echo test'
            }
        stage('test') {
            steps {
                sh 'echo test'
            }
        }
    }
}