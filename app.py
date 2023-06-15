from flask import Flask, render_template

#pip install azure-mgmt-machinelearningservices==2.0.0b2

app = Flask(__name__)

@app.route("/")

def home():
    from azureml.core.authentication import InteractiveLoginAuthentication

    InteractiveLoginAuthentication(force=False, tenant_id=None, cloud=None)
    
    return render_template("index.html")

@app.route("/compute")
def copmpute():
    return render_template("compute.html")


if __name__ == "__main__":
    app.run(debug=True)
    
    
