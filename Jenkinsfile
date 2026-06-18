pipeline {
agent any
environment {
    DOCKER_IMAGE = "chinninaidu/studenthub-app"
    DOCKER_TAG = "latest"
}
stages {

    stage('Checkout Code') {
        steps {
            git branch: 'main',
                url: 'https://github.com/aegletek/StudentHub.git'
        }
    }
    stage('Verify Files') {
        steps {
            sh 'pwd'
            sh 'ls -la'
        }
    }
    stage('Build Docker Image') {
        steps {
            sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
        }
    }
    stage('Login to DockerHub') {
        steps {
            withCredentials([
                usernamePassword(
                    credentialsId: 'dockerhub-cred',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )
            ]) {
                sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
            }
        }
    }
    stage('Push Docker Image') {
        steps {
            sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
        }
    }
    stage('Deploy to Kubernetes') {
        steps {
            sh 'kubectl apply -f k8s/'
            sh 'kubectl rollout restart deployment/studenthub-deployment'
            sh 'kubectl rollout status deployment/studenthub-deployment'
            sh 'kubectl get pods'
            sh 'kubectl get svc'
        }
    }
}
post {
    success {
        echo 'PIPELINE SUCCESS - Deployment completed'
    }
    failure {
        echo 'PIPELINE FAILED - Check logs'
    }
}
}
