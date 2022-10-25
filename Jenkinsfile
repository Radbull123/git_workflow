void setBuildStatus(String message, String state) {
    step([
        $class: "GitHubCommitStatusSetter",
        reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/Radbull123/git_workflow"],
        contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
        errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
        statusResultSource: [$class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]]]
    ]);
}

pipeline {
  agent {
    node {
      label 'linux'
    }

  }
  parameters{
    string(name: 'GIT_BRANCH_NAME', defaultValue: 'main', description: 'Required branch under the test')
  }
  stages {
    stage('Build') {
      steps {
        sh 'echo "Simulate building"'
        sh 'poetry shell && poetry install'
      }
    }

    stage('Test') {
      steps {
        sh 'poetry run python -m pytest -v'
      }
    }

    stage('Static Analysis') {
      steps {
        sh 'poetry run python -m flake8'
      }
    }
  }
  post {
      always {
        script {
              step([$class: 'WsCleanup'])
        }
      }
      success{
        setBuildStatus("Build succeeded", "SUCCESS");
      }
      failure {
        setBuildStatus("Build failed", "FAILURE");
      }
  }
}