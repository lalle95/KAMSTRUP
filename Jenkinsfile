pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pwd'    
            }
        }
        stage('deploy') {
            steps {
                mail body: 'project run successful',
                     from: 'lli@kamstrup.com',
                     replyto: 'lli@kamstrup.com',
                     subject: 'test message from jenkins',
                     to: "gag@kamstrup.com"
    
            }
            
        }
    }
}
