pipeline {
  agent {docker image 'busybox'}
  stages {

    stage('build') {
      parallel {
        stage('print') {
          steps {
            echo 'building ...'
          }
        }
        stage('print parallel') {
          steps {
            echo 'building in parallel ...'
          }
        }
      }
    }

    stage('test') {
      parallel {
        stage('print') {
          steps {
            echo 'testing ... '
          }
        }
        stage('print parallel') {
          steps {
            echo 'testing in parallel ...'
            echo 'test change'
          }
        }
        stage('Unit test') {
          steps {
            echo 'its working'
            //bat 'python test_calculator.py'
          }
        }
      }
    }

    stage('deploy') {
      parallel {
        stage('print') {
          steps {
            echo 'deploying ...'
          }
        }
        stage('print parallel') {
          steps {
            echo 'deploying in parallel ...'
          }
        }
      }
    }
  }
}