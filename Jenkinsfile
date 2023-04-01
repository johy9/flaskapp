pipeline {
  agent any

  stages {
    stage('Checkout SCM') {
      steps {
    

    stage('Checkout Ansible playbook') {
      steps {
        git branch: 'main', url: 'https://github.com/johy9/flaskapp.git' 
      }
    

    stage('Run Ansible playbook') {
      steps {
        ansiblePlaybook credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'ansible-project', inventory: 'host.ini', playbook: 'deploy.yml'
      }
    
  }
}
