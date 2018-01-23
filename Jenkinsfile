pipeline {

    agent none

    //agent {
    //    docker {image 'busybox:latest'} 
    //}
  
    stages {

        stage('build') {
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }

            steps {
                sh 'python test_calculator.py'
            }
        }
        /*
        stage('test') {
            steps {
                echo 'test'
            }
        }

        stage('deploy') {
            steps {
                echo 'deploy'
            }
        }
        */
    }
}