pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'docker stop gcc'
                sh 'docker container prune y'
                sh 'docker run -v pwd:/home --name gcc gcc g++ -o'

            }
        }
    }
}
