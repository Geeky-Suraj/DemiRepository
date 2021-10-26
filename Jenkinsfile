pipeline {
	agent any
	stages {
		stage("Compile") {
			steps {
				//pip install requirements.txt
				echo "Python compilation successfully done"
			}
		}
		stage("Unit test") {
			steps {
				sh "python3 DemoTest.py"
			}
		}
	}
}
