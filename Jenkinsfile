pipeline {
    agent any
    //agent {
    //    docker {image 'busybox:latest'} 
    //}
    stages {
        stage('build') {
            steps {
                //bat 'python --version'
                //bat 'docker run -v "C:/Users/lli/Documents/INTERNSHIP/Repositories/KAMSTRUP":/home --name gcc -it gcc'
                //bat 'cd home'
                //bat 'g++ -o HelloWorld helloworld.cpp'
                //bat './HelloWorld'
                bat 'python --version'
                echo 'build'
            }
        }

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
    }
}