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
                    sh 'docker build . -t bjnandi/python-app:v1.0.${BUILD_NUMBER}'
                    //sh 'docker tag python-app bjnandi/python-app:v1.0.${BUILD_NUMBER}'
                }
            }
        }
        
        // stage('Push the Docker Image to DockerHub') {
        //     steps {
        //         script {
        //             withCredentials([string(credentialsId: 'docker_hub', variable: 'docker_hub')]) {
        //             sh 'echo "${docker_hub}" | docker login -u bjnandi --password-stdin'
        //             }
        //             sh 'docker push bjnandi/python-app:v1.0.${BUILD_NUMBER}'
        //         }
        //     }
        // }


        stage('Update GIT') {
            steps {
                script {
                    //catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                            //def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
                            sh 'git config user.email nbiswajit94@gmail.com'
                            sh 'git config user.name Biswajit Nandi'
                            sh 'pwd'
                            sh 'ls'
                            dir('k8s') {
                                sh """
                                cat py-crud-app.yml
                                sed -i 's+python-crud-app:v1.0.*+python-crud-app:v1.0.${BUILD_NUMBER}+g' py-crud-app.yml
                                cat py-crud-app.yml
                                git add .
                                git commit -m 'Done by Jenkins Job changemanifest: ${BUILD_NUMBER}'
                                git push
                                // git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/python-flask-postgresql-crud-application.git HEAD:main
                                """
                            }
                        }
                    //}
                }
            }
        }
    }
}