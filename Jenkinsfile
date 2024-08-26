pipeline {
    agent any

    stages {
        stage('Checkout GitHub repo') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/bjnandi/python-flask-postgresql-crud-application.git']])
            }
        }
        
        // stage('Build and Tag Docker Image') {
        //     steps {
        //         script {
        //             sh 'docker build . -t python-app:v1.0.${BUILD_NUMBER}'
        //             sh 'docker tag python-app bjnandi/python-app:v1.0.${BUILD_NUMBER}'
        //         }
        //     }
        // }
        
        // stage('Push the Docker Image to DockerHUb') {
        //     steps {
        //         script {
        //             withCredentials([string(credentialsId: 'docker_hub', variable: 'docker_hub')]) {
        //             sh 'echo "${docker_hub}" | docker login -u bjnandi --password-stdin'
        //             }
        //             sh 'docker push bjnandi/python-app:v1.0.${BUILD_NUMBER}'
        //         }
        //     }
        // }
        // run sonarqube test
        // stage('Run Sonarqube') {
        //     environment {
        //         scannerHome = tool 'lil-sonar-tool';
        //     }
        //     steps {
        //       withSonarQubeEnv(credentialsId: 'lil-sonar-credentials', installationName: 'lil sonar installation') {
        //         sh "${scannerHome}/bin/sonar-scanner"
        //       }
        //     }
        // }

        stage('SonarQube Analysis') {
            def scannerHome = tool 'SonarScanner';
            withSonarQubeEnv(credentialsId: 'sonerqube', installationName: 'sonerqube') {
            sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
}