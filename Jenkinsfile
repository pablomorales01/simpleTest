
pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build images') {
      steps {
        sh '''
          set -e
          echo "== Building images ==" | tee -a pipeline.log
          docker compose build 2>&1 | tee -a pipeline.log
        '''
      }
    }
    stage('Selenium tests (docker compose)') {
      steps {
        sh '''
          set -e
          echo "== Starting services and running Selenium tests ==" | tee -a pipeline.log
          docker compose up --abort-on-container-exit --exit-code-from tests 2>&1 | tee -a pipeline.log || true
        '''
      }
      post {
        always {
          sh 'docker compose down -v || true'
        }
      }
    }
    stage('Unit tests') {
      steps {
        sh '''
          set -e
          echo "== Python unit tests ==" | tee -a pipeline.log
          python -m pip install --upgrade pip 2>&1 | tee -a pipeline.log
          pip install -r requirements.txt 2>&1 | tee -a pipeline.log
          pytest -q tests/unit 2>&1 | tee -a pipeline.log || true
        '''
      }
    }
    stage('PDF log') {
      steps {
        sh '''
          python tools/make_pdf.py pipeline.log pipeline_log.pdf
        '''
        archiveArtifacts artifacts: 'pipeline.log,pipeline_log.pdf,artifacts/homepage.png', fingerprint: true
      }
    }
  }
  post {
    always {
      echo 'Pipeline complete.'
    }
  }
}
