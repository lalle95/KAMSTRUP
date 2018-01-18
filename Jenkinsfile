pipeline {
  agent any
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
          }
        }
        stage('Unit test') {
          steps {
            sh 'bat \'python test_calculator.py\''
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