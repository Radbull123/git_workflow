pipeline {
  agent {
    node {
      label 'linux'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'echo "Simulate building"'
      }
    }

    stage('Test') {
      steps {
        sh 'poetry run pytest'
      }
    }

    stage('Static Analysis') {
      steps {
        sh 'poetry run python -m flake8'
      }
    }

  }
}