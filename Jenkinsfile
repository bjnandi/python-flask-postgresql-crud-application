pipeline {
    agent any

    stages {
        stage('Checkout GitHub repo') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/bjnandi/python-flask-postgresql-crud-application.git']])
            }
        }
        
        // stage('SonarQube Analysis') {
        //     environment {
        //         scannerHome = tool 'python-app';
        //     }
        //     // def scannerHome = tool name: 'python-app', type: 'hudson.plugins.sonar.SonarRunnerInstallation';111
        //     steps {
        //         withSonarQubeEnv(credentialsId: 'sonerqube', installationName: 'python-app') {
                    
        //         sh "${scannerHome}/bin/sonar-scanner"
        //         }
        //     }
        // }

        // stage('Quality Gate') {
        //     steps {
        //         script {
        //             // Wait for SonarQube Quality Gate result and proceed only if it passes
        //             def qualityGate = waitForQualityGate() // Wait for the quality gate result
        //             if (qualityGate.status != 'OK') {
        //                 error "Pipeline aborted due to quality gate failure: ${qualityGate.status}"
        //             }
        //         }
        //     }
        // }

        stage('Build and Tag Docker Image') {
            steps {
                script {
                    sh 'docker build . -t bjnandi/python-crud-app:v1.0.${BUILD_NUMBER}'
                    //sh 'docker tag python-app bjnandi/python-crud-app:v1.0.${BUILD_NUMBER}'
                }
            }
        }
        
        stage('Push the Docker Image to DockerHub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'docker_hub', variable: 'docker_hub')]) {
                    sh 'echo "${docker_hub}" | docker login -u bjnandi --password-stdin'
                    }
                    sh 'docker push bjnandi/python-crud-app:v1.0.${BUILD_NUMBER}'
                }
            }
        }


        // stage('Trigger Manifest Update') {
        //     steps {
        //         script {
        //             sh 'echo "triggering updatemanifest job"'
        //         }
        //         build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        //     }
        // }
    }
}

