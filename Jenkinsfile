pipeline {
  agent { label 'docker'}

  environment {
      dockerImage = ''
      credentials = 'docker-hub'
      kubernetesToken = credentials('kubernetes-token')
  }

  stages {
    stage('Build') {
      when { branch 'develop' }
      steps {
        container('docker') {
          script {
            sh 'chmod +x todoapp/entrypoint.sh'
            dockerImage = docker.build("patriciocostilla/todoapp:${BUILD_NUMBER}", "-f todoapp/Dockerfile ./todoapp")
            } 
          }
        }
      }
      
    stage('Publish') {
      when { branch 'develop' }
      steps {
        container('docker') { 
          script {
            docker.withRegistry('', credentials) {
                dockerImage.push()
                dockerImage.push('dev')
              }
            } 
          }
        }
      }
            
    stage('Deploy') {
      when { branch 'develop' }  
      steps {
        container('kubectl') {
          script {
              sh 'kubectl --server https://10.0.2.10:6443 --token=${kubernetesToken} --insecure-skip-tls-verify apply -f manifest.yml'
              sh 'kubectl --server https://10.0.2.10:6443 --token=${kubernetesToken} --insecure-skip-tls-verify rollout restart deployment/todoapp-deployment -n tpi-dev'
              sh 'kubectl --server https://10.0.2.10:6443 --token=${kubernetesToken} --insecure-skip-tls-verify rollout status deployment/todoapp-deployment -n tpi-dev --timeout 5m'
          }
        }
      }
    }
  }
}