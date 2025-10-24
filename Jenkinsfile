pipeline {
    agent any

    stages {

        stage('Pull Code') {
            steps {
                // Pull latest code from your GitHub repository using credentials
                git branch: 'main',
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/Ammullupramidha/casestudy.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🔧 Building Docker image...'
                sh 'docker build -t pramidha/appointment-scheduler:latest .'
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                echo '🚀 Pushing Docker image to DockerHub...'
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_HUB_PASS')]) {
                    sh 'echo $DOCKER_HUB_PASS | docker login -u Pramidha --password-stdin'
                    sh 'docker push pramidha/appointment-scheduler:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '⚙️ Deploying to Kubernetes cluster...'
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
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
