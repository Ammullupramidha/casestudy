pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/Pramidha/appointment-scheduler.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pramidha/appointment-scheduler:latest .'
            }
        }
        stage('Push Image to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_HUB_PASS')]) {
                    sh 'echo $DOCKER_HUB_PASS | docker login -u Pramidha --password-stdin'
                    sh 'docker push pramidha/appointment-scheduler:latest'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
    post {
        success { echo "✅ Deployed successfully!" }
        failure { echo "❌ Deployment failed!" }
    }
}
