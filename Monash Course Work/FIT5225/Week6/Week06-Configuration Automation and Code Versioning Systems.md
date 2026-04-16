# **Lab 06 - Configuration Automation and Code Versioning Systems**

# **Goal**

This lab covers the basics of using Infrastructure as Code(IaC) tools. You will learn how to use Ansible to create VMs in Nectar and install Kubernetes; then, we will use the Pulumi tool to deploy the web service from last week. You will learn concepts around configuration automation and how tools such as Ansible and Pulumi can be used to configure multiple servers and applications simultaneously. You will use those tools to automate the creation of various resources in Nectar, including a small-scale Kubernetes cluster.

As we will see in this lab, Ansible yml files are text files with instructions. Initially, it takes time to debug and test similar to other programming languages, therefore, we can use git to perform version control. Once we have those yml files, we can easily repeat those tasks. Most IT students should be familiar with git these days. If you need a refresh, we provide some basic examples of using git for version control in the Appendix section.

# **Resources**

Same as in the previous lab, you need to transfer a few files from your computer to a remote VM, therefore, you need to know how to achieve this based on your computer’s operating system.

## **Task 0: Creating a VM and Preparing the Environment**

For this lab, we need a "**m3.xsmall**” instance that has "NeCTAR Ubuntu **22.04**” as its boot image. After creating the instance, if you don’t have your OpenStack configuration file (**openrc**) from the previous lab, you need to download it again. Additionally, you need the Nectar **password** that you generated as part of the previous lab. We will use this VM to provision other VMs and resources.

Use the following command to update the software repository on your VM and install the required software:

$ sudo apt update \&\& sudo apt install -y software-properties-common git curl python3 \&\& sudo apt install -y python3-pip \&\& export PATH=$PATH:/home/ubuntu/.local/bin

## **Task 1: Using Ansible to Automate Resource Creation and Configuration**

In this task, you will set up Ansible and use it to create some resources in our Nectar project. **First, download "ansible-demo.zip” and "ansible-k8s-demo.zip” from Nectar -> Object Store -> Containers -> Ansible-K8s and copy it along with your private SSH key and your openrc file to your instance.** Note that copying private keys to servers is not recommended and instead, it’s better and safer to install Ansible on your local computer and use it as the control centre to create other resources. However, because installing Ansible on Windows machines requires a few extra steps and software installations, we’re taking this approach.

**Alternatively**, if you lost your private key or do not want to copy it, you can generate a key pair on your VM using the following command in VM terminal

$ ssh-keygen -t ed25519 -f \~/.ssh/id\_ed25519

Now, your <path-of-your-private-key> will be \~/.ssh/id\_ed25519. Then, put the content of \~/.ssh/id\_ed25519.pub on  Nectar at FIT5225-Cloud > Project > Key Pairs > IMPORT PUBLIC KEY > IMPORT PUBLIC KEY

* Key Pair Name\*: <YOUR\_NAME>-personal-vm-public-key
* Key Type \*: SSH Key
* Public Key \*: content of \~/.ssh/id\_ed25519.pub

  You will reuse <YOUR\_NAME>-personal-vm-public-key later as <your-key-name-in-nectar>.

  If you copied the private key to your VM instead, run the following command in VM terminal to save the path in a environment variable so later we can reuse it

  $ export PRI\_KEY\_PATH=<path-of-your-private-key>

  Run the following command to install dependencies:

  $ sudo apt update \&\& sudo apt install -y python3-pip unzip vim python3-shade

  Install the latest version of Ansible and OpenStack SDK/Client

  $ sudo pip3 install -U ansible openstacksdk openstackclient \&\& sudo ansible-galaxy collection install openstack.cloud

  Now let’s unzip "ansible-demo.zip” and copy our openrc file inside the ansible-demo folder:

  $ unzip \~/ansible-demo.zip \&\& cp \~/FIT5225-Cloud-openrc.sh \~/ansible-demo/ \&\& cd \~/ansible-demo

  Inside this folder, there is an ansible playbook named nectar.yaml that we plan to run. Your tutor will give you an overview of the different files in this folder and their purpose as interpreted by Ansible.

  **Go to "host\_vars” folder and open "nectar.yaml” file.**

  **Change the availability zone to "monash-02” and instance flavour to "r3.small”.**

  **Change the instance image to "c0250c96-98a4-4bfa-b67c-51874808337f”.** (Ubuntu 22.04 LTS, your tutor will show you how to find this ID.)

  **Change the folder to ansible-demo.**

  Use the following command to run the Ansible playbook and provide your Nectar password when prompted:

  (This will add OpenStack env variables to your shell environment and enter your password)

  $ source ./FIT5225-Cloud-openrc.sh

  Test if OpenStack works:

  $ openstack server list

  You shall see a list of VM instances in Nectar if the authentication is successful.

  $ ansible-playbook -e "my\_name=<your-name>" -e "key\_name=<your-key-name-in-nectar>" nectar.yaml

  your-key-name-in-nectar: means the **public key name** that you can find it from nectar user keypair.

  Upon successful completion of the playbook, in your Nectar dashboard, verify that two instances containing your name have been created and check their security groups. (Note: In the current version, you may see the "KeyError” exception, this is caused by an empty volumes python dictionary. If your web servers are successfully created, you can ignore this error.)

  Then create a new file named **hosts.ini** and paste the following content in it, replacing server IP lines with the **actual IP** addresses of your instances:

  \[web\_servers]  
SERVER\_1\_IP\_HERE  
SERVER\_2\_IP\_HERE

  The \[web\_servers] header serves as a text-based filter, when you apply commands to a group of servers, you can use this header to find the group of servers.

  Note: You can find the server IP addresses from the Nectar dashboard or use the following command:

   (optional)$ openstack server list | grep <your-name> | awk '{print $8}' | awk -F= '{print $2}' | head -n 2

  In the next step, we are going to use Ansible modules to perform some actions on instances we created in the previous step. First, use the following command that uses the ping module to make sure Ansible can SSH our servers defined in the inventory file:

   $ ansible -i hosts.ini -v web\_servers -m ping --private-key=$PRI\_KEY\_PATH -u ubuntu

  If the ping was successful, you can proceed with installing Apache Web Server on your instances using the command below:

  $ ansible -i hosts.ini -v web\_servers -m apt -a "name=apache2 state=latest" --private-key=$PRI\_KEY\_PATH -u ubuntu --become

  Finally, to access your web server, you need to start it on your instance. Apache HTTP daemon doesn’t start by default. For this, use the following command and next, try to access your web servers using each server’s public IP address in a web browser.

  (optional)$ ansible -i hosts.ini -v web\_servers -a "systemctl start apache2" --private-key=$PRI\_KEY\_PATH -u ubuntu --become

  ## **Task 2: Using Ansible to Install a Kubernetes Cluster**

  In this task, you will learn how to install a Kubernetes cluster with Ansible. Because of the resource constraints of the shared Nectar project, we will reuse the two instances created in Task 2 and create a 2-node Kubernetes cluster with 1 master node and 1 worker node. The files you need for this task are in "**ansible-k8s-demo.zip**” downloaded in Task 2.

  $ unzip ansible-k8s-demo.zip \&\& cd ansible-k8s-demo

  Similar to the previous task, we need to define our host file and assign different roles to the two VMs. Create a **k8s-hosts.ini** file with the following content(change the IP addresses to your server IPs):

  \[masters]  
SERVER\_1\_IP\_HERE

  \[workers]  
SERVER\_2\_IP\_HERE

  Test the connectivity to all hosts:

   $ ansible -i k8s-hosts.ini all -m ping --private-key=$PRI\_KEY\_PATH -u ubuntu

  Your tutor will explain the code of Ansible YAML files. To make it easier to understand, the YAML files use similar steps as we learned from Week 4. They are text-based instructions similar to software written with other programming languages. Therefore, you can use Git to manage revisions of your cluster/infrastructure.

  Apply user permission setting:

   $ ansible-playbook -i k8s-hosts.ini --private-key=$PRI\_KEY\_PATH 1\_users.yml -u ubuntu

  Install Kubernetes dependencies:

  $ ansible-playbook -i k8s-hosts.ini --private-key=$PRI\_KEY\_PATH 2\_install\_k8s.yml

  Create the master node:

  $ ansible-playbook -i k8s-hosts.ini --private-key=$PRI\_KEY\_PATH 3\_create\_master.yml -u ubuntu

  Join the worker node:

  $ ansible-playbook -i k8s-hosts.ini --private-key=$PRI\_KEY\_PATH 4\_join\_worker.yml -u ubuntu

  The installation process may take a few minutes. After this step, you can log in to your master node ssh -i $PRI\_KEY\_PATH ubuntu@SERVER\_1\_IP\_HERE  and run kubectl get nodes to see if your cluster is up and running.

  ## **Task 3: Using Pulumi to Deploy Web Services on Kubernetes Cluster**

  (note: If you cannot complete the previous tasks, install a K3s cluster similar to Week 4 and continue on this task. [**https://k3s.io/**](https://k3s.io/))

  In this task, we are going to use the Pulumi IaC tool to build our ToDo app web service from last week and deploy it to the Kubernetes cluster created in the previous task. Firstly, you need to install the Pulumi **C**ommand **LI**ne(CLI) tool on your local machine for developing and update your Pulumi code; then, initialize a Pulumi Python project and write(copy) the provided source code; and finally, upload your IaC script to your cloud VM(K8s master) and run the script in your production environment.

  Step 1(Install Pulumi CLI): Follow the instructions from the installation page depending on your operating system: [https://www.pulumi.com/docs/iac/download-install/](https://www.pulumi.com/docs/iac/download-install/)

  Step 2: Create a folder, then open it in a terminal, then run

  $ pulumi login --local

  $ pulumi new python

  Follow the prompts to add some basic information and description about your project. Then, Plumni will generate some boilerplate files and create a local venv for you. You can open this folder on your laptop with your preferred editor.

  Activate your venv(MacOS): $ source ./venv/bin/activate

  \*\*\*\***Windows users only**\*\*\*\*

  The command source ./venv/bin/activate only works on macOS/Linux. On Windows, do this instead:

  1\. Open your project folder in Command Prompt (CMD). Tip: in File Explorer, click the address bar, type cmd, and press Enter — it opens CMD directly in that folder.

  2\. Run the activation script. In CMD, run venv\\Scripts\\activate.bat. In PowerShell, run venv\\Scripts\\Activate.ps1 instead. (Note: Windows uses backslashes \\, not forward slashes /.)

  3\. Check it worked. You should see (venv) appear at the start of your prompt, e.g. (venv) C:\\Users\\YourName\\my-pulumi-project>. That means you're inside the virtual environment and ready to run pip install -r requirements.txt.

  \*\*\*\*\*\*\*\*

  Since we need docker and kubernetes plugins of Pulumi, add these two lines to your requirements.txt

  pulumi\_docker

  pulumi\_kubernetes

  Then, run $ pip install -r requirements.txt

  Replace the \_\_main\_\_.py file’s contents with the following source code, and replace the configuration variables with your configuration.

  Note: You need a docker hub account to publish your image to the docker hub. (If you don’t have one, you can register at [https://hub.docker.com/](https://hub.docker.com/))

  Your tutor will explain the source code. The documentation for the Pulumi API reference can be found here: [Pulumi documentation](https://www.pulumi.com/docs/reference/pkg/python/pulumi/)

  """A Python Pulumi program"""

  import pulumi  
import pulumi\_docker as docker  
import pulumi\_kubernetes as k8s  
from pulumi\_kubernetes.core.v1 import Namespace  
from pulumi\_kubernetes.apps.v1 import Deployment  
from pulumi\_kubernetes.core.v1 import Service

  \# Configuration variables  
app\_name = "todoapp"  
docker\_repo\_name = "your-dockerhub-username"  # Replace with your Docker Hub repo  
docker\_tag = "latest"  
k8s\_namespace\_name = "todo-app-ns"  
service\_type = "ClusterIP" # Change to 'LoadBalancer' if needed

  \# 1. Create a Kubernetes Namespace  
namespace = Namespace(  
k8s\_namespace\_name,  
metadata={"name": k8s\_namespace\_name},  
)

  \# 2. Build the Docker image  
docker\_image = docker.Image(  
app\_name,  
build={"context": "./src",  
"platform": "linux/amd64"  
},  # Path to the directory containing your Dockerfile.  Assumes Dockerfile is in the same directory as this script.  
image\_name=f"docker.io/{docker\_repo\_name}/{app\_name}:{docker\_tag}",  
)

  \# 3. Deploy to Kubernetes  
app\_labels = {"app": app\_name}  
deployment = Deployment(  
app\_name,  
metadata={  
"namespace": k8s\_namespace\_name,  
},  
spec={  
"selector": {"matchLabels": app\_labels},  
"replicas": 2,  # You can scale this as needed  
"template": {  
"metadata": {"labels": app\_labels},  
"spec": {  
"containers": \[  
{  
"name": app\_name,  
"image": docker\_image.image\_name,  
"ports": \[{"containerPort": 8000}],  # Expose the port your FastAPI app listens on (default: 8000)  
"env": \[ #Add environment variables, if needed.  
# {"name": "VAR\_NAME", "value": "value"},  
],  
}  
]  
},  
},  
},  
)

  \# 4. Create a Kubernetes Service  
service = Service(  
app\_name,  
metadata={  
"namespace": k8s\_namespace\_name,  
},  
spec={  
"selector": app\_labels,  
"ports": \[{"port": 80, "targetPort": 8000}], #  Map the service port to the container port  
"type": service\_type,  # Use ClusterIP for internal access, LoadBalancer for external  
},  
)

  \# 5. Export the Service's IP address (if applicable)  
if service\_type == "LoadBalancer":  
service\_ip = service.status.apply(lambda status: status.load\_balancer.ingress\[0].ip if status.load\_balancer and status.load\_balancer.ingress else "pending")  
pulumi.export("service\_ip", service\_ip)  
else:  
pulumi.export("service\_name", service.metadata\["name"])  
Then, create a folder inside your pulumi project folder named **src** and copy the source code(todo-app.py) **from last week** to this folder.

  Exercise(10-15 minutes): Create a **Dockerfile** and **requirements.txt** to build your application to a docker image. (You can refer to the Week 3 content for this task.) Those files should be placed in the src folder alongside your todo-app.py.

  The source code contains multiple stages:

1. Create a namespace in Kubernetes
2. Build and push your docker image to the docker hub (docker login is required, see: [https://docs.docker.com/reference/cli/docker/login/](https://docs.docker.com/reference/cli/docker/login/)
3. Deploy your todo-app to Kubernetes
4. Create a Kubernetes service and config app selector
5. Expose your service using ClusterIP.

   To execute the Pulumi IaC code,

1. On your master node, install Pulumi: $ curl -fsSL https://get.pulumi.com | sh
2. Install python virtual env: $ sudo apt install python3-venv
3. If you haven’t, login to your docker account with $ docker login
4. Create a new folder and initialise it with $ 	pulumi login --local \&\& pulumi new python
5. Upload the Pulumi folder(src folder, requirements.txt, \_\_main\_\_.py) from your laptop to the cloud VM(master node)
6. Go to the project folder, activate the new venv with $ source venv/bin/activate, then $ pip install -r requirements.txt
7. Use $ pulumi up. It automates everything we learnt in weeks 3 and 5: build a Docker container from your source code, push it to your docker hub account, deploy your web service to the Kubernetes cluster, then export the service using ClusterIP. (If it shows connection refused after you input `yes`, you can try to reboot your master node with the command **$ sudo reboot.** Then wait for 1 min and reconnect to the master node and rerun pulumi up. If it still doesn’t work, refer to week 04 to reset Kubernetes cluster on the master node)

   You can use $  <your-namekubectl get all -nspace> to view the deployment and test the web service on

   $ curl -X GET <CLUSTER\_IP>/todo/api/v1.0/tasks --basic --user fastapi:FIT5225

   ## **Appendix: Hands-On with Git (Home Task)**

   (Please see the appendix for a reference git branching strategy.)

   Let’s start by creating a new directory, making a simple README.md file in it, and changing our current directory:

   $ mkdir -p \~/git-demo \&\& echo "# Git is cool” > \~/git-demo/README.md \&\& cd \~/git-demo

   A Git repository is basically a directory that holds and tracks your files. To convert any directory to a git repository, use ***git init*** inside that directory. Note that if you now use the ***ls -a*** command to list all files inside this directory, you will see a new .git folder. Git internally uses this hidden folder to store its refs, configs, etc.

   First, configure your git environment by setting your username and email address using the following command:

   $ git config --global user.name <your-name> \&\& git config --global user.email <your-email>

   At any time, to see the latest status of your Git repository, use the ***git status*** command. This command tells you if any file has been modified and shows the currently staged file(s). Modify the content of the README.md file using the following command and get the status again to see if you notice any difference.

   $ echo "It’s also easy to learn" >>  README.md

   To commit your changes, first you need to stage them. You can use ***git add*** to stage any file or directory or use ***git add --all*** to stage all changes at once.  After staging your changes, do another ***git status*** to see the difference. Now commit your changes using the ***git commit -m*** "***Add README file***" command.

   To see the commit history for your current branch, use ***git log*** and you should see the commit that you just made in the repository. Additionally, to get a list of local and remote branches, use ***git branch -a*** inside your repository.

   Next, use the following command to create a new branch named "feature1” and add a new Python file:

   $ git checkout -b feature1 \&\& echo "print('Hello World')" > app.py

   Verify you are now in the feature1 branch and use the following one-liner to stage and commit the new change:

   $ git add . \&\& git commit -m "Add application source code"

   Switch to the master branch using ***git checkout master*** and then using ***git diff feature1*** and ***git log*** commands to verify that the master branch is behind the feature1 branch by 1 commit and note the differences. Now use the following command to merge the feature1 branch into master and after that use git log to confirm the merge operation has been successful:

   $ git merge feature1

   To see the difference between merge and rebase, create a new file with some content in it and commit the changes in the master branch. Then switch to the feature1 branch again using ***git checkout feature1*** and modify the README file and commit the changes. Now your feature1 branch has diverged from the master branch (verify using git diff and git log). Use the following command to rebase your current branch into master interactively:

   $ git rebase -i master

   Using git log you should be able to verify that your last commit has been applied on top of the last commit in the master branch. Rebasing also allows you to squash your commits and merge them into bigger and more comprehensive commits.

   You can find nice visualisations of the above git operations [here.](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1)

   Appendix(Image Credit: Vincent Driessen):

   References:

1. [git-scm](https://git-scm.com/)
2. [https://nvie.com/files/Git-branching-model.pdf](https://nvie.com/files/Git-branching-model.pdf)
3. [Ansible Openstack Module](https://docs.ansible.com/ansible/latest/collections/openstack/cloud/index.html)
4. [Deploy K8s with Ansible](https://buildvirtual.net/deploy-a-kubernetes-cluster-using-ansible/)

