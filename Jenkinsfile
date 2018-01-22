pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'docker run -v "C:\Users\lli\Documents\INTERNSHIP\Repositories\KAMSTRUP":/home --name gcc -it gcc'
                bat 'g++ -o HelloWorld helloworld.cpp'
                bat './HelloWorld'
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