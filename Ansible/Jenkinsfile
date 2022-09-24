pipeline {
    agent any
    stages {
        stage(‘Git’){
            steps{ git branch: 'docker', credentialsId: 'b67c2c35-0b9d-4839-be19-da574b247e65', url: 'git@github.com:zMaAlz/vector-role.git'
                }
            }
        stage(‘molecule’){
            steps{ sh 'molecule test'
                }
            }
        }
}