pipeline {
    agent { dockerfile true }
    stages {
    	stage('git-clone') {
			checkout scm

			now = new Date().format('yyyyMMdd-HHmmss')
			imageTag = "${now}"
			echo $imageTag
    	}
        stage('build') {
            
        }
        stage('run') {
        	
        }
        stage('test') {

        }
    }
}