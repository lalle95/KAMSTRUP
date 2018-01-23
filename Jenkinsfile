pipeline {

    agent none

    //agent {
    //    docker {image 'busybox:latest'} 
    //}
  
    stages {

        stage('build') {
            agent {
                docker {
                    image 'busybox' 
                }
            }

            steps {
                sh 'ls'
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