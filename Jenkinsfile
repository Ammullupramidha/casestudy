pipeline {
    agent any

    stages {

        stage('Pull Code') {
            steps {
                // Pull latest code from GitHub using credentials
                git branch: 'main',
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/Ammullupramidha/casestudy.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🔧 Building Docker image...'
                bat 'docker build -t pramidha/appointment-scheduler:latest .'
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                echo '🚀 Pushing Docker image to DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-pass', 
                                                 usernameVariable: 'DOCKER_USER', 
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push pramidha/appointment-scheduler:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '⚙️ Deploying to Kubernetes cluster...'
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo "✅ Appointment Scheduler deployed successfully from casestudy repo!"
        }
        failure {
            echo "❌ Deployment failed! Please check the Jenkins logs for errors."
        }
    }
}
