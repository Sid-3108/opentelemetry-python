pipeline {
    agent any //this could be docker agent or kubernetes agent or anything

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        } 
        stage('Sanity Test') {
            steps{
                echo 'Jenkins Pipeline is working successfully'
            }
        }
    }
}