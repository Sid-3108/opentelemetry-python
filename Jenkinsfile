pipeline {
    agent any //this could be docker agent or kubernetes agent or anything

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        } 
        stage('Verify Workspace') {
            steps {
                sh '''
                    echo 'Current Directory'
                    pwd

                    echo 'Listing repo root'
                    ls -l

                    echo 'Listing contents of demo-service folder'
                    ls -l demo-service
                '''
            }
        }

        stage('Verify Service level Sanity Check') {
            steps{
                sh '''
                    echo 'Getting into the demo-service folder'
                    cd demo-service

                    echo 'Listing out files inside demo-service folder'
                    ls -l

                    echo 'Python version info'
                    python --version || python3 --version
                '''
            }
        }

        stage('Sanity Test') {
            steps{
                echo 'Jenkins Pipeline is working successfully'
            }
        }
    }
}