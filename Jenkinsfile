pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "dhruva1098/scientific-calculator-api" // Replace with your Docker Hub username and image name
    }

    stages {
        stage('Checkout') {
            steps {
                git scmGit(branches: [[name: '*/main']]), credentialsId: 'github-credentials', extensions: [], userRemoteConfigs: [[url: 'https://github.com/Dhruva1098/SPE_mini_project/']]  // Replace with your repo URL and credentials ID if needed
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover' // Run Python unit tests
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build(env.DOCKER_IMAGE_NAME, '.') // Build Docker image
                    dockerImage.push() // Push to Docker Hub (if Docker Hub credentials are configured)
                }
            }
        }
        stage('Deploy (Local)') {
            steps {
                script {
                    docker.image(env.DOCKER_IMAGE_NAME).pull() // Pull latest image from Docker Hub
                    sh 'docker stop scientific-calculator-container || true' // Stop existing container (ignore error if not running)
                    sh 'docker rm scientific-calculator-container || true'   // Remove existing container (ignore error if not existing)
                    sh 'docker run -d --name scientific-calculator-container -p 8080:80 ${DOCKER_IMAGE_NAME}' // Run new container
                }
            }
        }
    }
}