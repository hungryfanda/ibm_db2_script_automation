# IBM Db2 Docker & Python Integration Notes

### 🐳 1. Docker & Container Management
Commands used to check, start, stop, and inspect your IBM Db2 container from the host shell.

```bash
# List all containers (active and inactive) to find your target container ID or name - 'testdb2' in this case
docker ps -a

# Safely stop the running Db2 container
docker stop testdb2

# Resume/start your existing Db2 container
docker start testdb2
```

---

### 🗄️ 2. Native IBM Db2 Terminal Interface
Commands executed inside the container terminal (as the `db2inst1` user) to manage the database instance, create objects, and manage tables.

```bash
# Access the container shell environment as the db2inst1 user
docker exec -it testdb2 bash -c "su - db2inst1"

# Verify the operational status and list details of the running Db2 instance
db2instance show -list

# Check system state monitor (alternative check)
db2getstate

# List all databases initialized on this system instance
db2 list db directory

# Create a new local database instance (Takes 2–5 minutes)
db2 create database testdb2

# Open an active session connection to your database (Mandatory before queries)
db2 connect to testdb2

# Create a sample data table with strict financial data fields
db2 "CREATE TABLE store (id INT NOT NULL PRIMARY KEY, name VARCHAR(50), cost DECIMAL(10, 2), quantity INT)"

# Insert standard sample records into your table (Run sequentially)
db2 "INSERT INTO store (id, name, cost, quantity) VALUES (1, 'Laptop', 899.99, 15)"
db2 "INSERT INTO store (id, name, cost, quantity) VALUES (2, 'Wireless Mouse', 25.50, 100)"
db2 "INSERT INTO store (id, name, cost, quantity) VALUES (3, 'Mechanical Keyboard', 119.00, 45)"

# Verify and fetch all active table rows from the database engine
db2 "SELECT * FROM store"
```

---

### 💻 3. Windows PowerShell & WSL Infrastructure Setup
Commands executed in Windows PowerShell to inspect, install, configure, and bridge the Linux Subsystem.

```powershell
# List all active WSL environments on your Windows PC and verify their build states
wsl -l -v

# Download and deploy the official Ubuntu Linux distribution to your PC
wsl --install -d Ubuntu

# Set Ubuntu as the permanent system-wide default distribution choice for WSL shortcuts
wsl --set-default Ubuntu

# Directly jump into your default Linux distro's native home directory (`~`) from PowerShell
wsl ~
```

---

### 🐧 4. WSL Ubuntu 26.04 Environment Configuration
Commands executed inside the new native Ubuntu workspace to configure privileges, package engines, and custom repository wrappers.

```bash
# Verify your specific Linux build details and release metadata
lsb_release -a

# Check the built-in global system Python development language version
python3 --version

# Install core compilation prerequisites into your package registry
sudo apt update && sudo apt install -y software-properties-common build-essential

# Add the deadsnakes repository to fetch older/specific Python versions safely
sudo add-apt-repository ppa:deadsnakes/ppa -y && sudo apt update

# Deploy isolated Python 3.11 runtimes alongside your main OS layers
sudo apt install -y python3.11 python3.11-dev python3.11-venv

# Install missing system layout features to enable advanced group configurations
sudo apt install -y util-linux-extra

# Add your user profile to the Docker security group to stop permission denied errors
sudo usermod -aG docker \$USER

# Instantly activate group profiles for your current terminal connection window
newgrp docker

# Execute a privileged container diagnostic to extract the exact Db2 engine build tracking information
docker exec -it --user db2inst1 testdb2 bash -c "source ~/sqllib/db2profile && db2level"
```

---

### 🐍 5. Python 3.11 Environment Setup & Execution
Commands used inside your project directory (`~/test_ibmdb2`) to structure sandboxed libraries.

```bash
# Create an isolated local virtual environment sandbox profile
python3.11 -m venv venv

# Direct path installation method to cleanly map dependencies without PEP 668 blocks
./venv/bin/pip install --no-cache-dir ibm_db==3.2.3

# Execute your completed connection extraction code script using the environment's interpreter
./venv/bin/python test_ibmdb2.py

# Launch VS Code graphical environment directly inside your exact active Linux terminal paths
code .
```

---

### 🔒 6. OpenSSL Security & Symmetric Keys
Commands used to generate text configurations, enforce permissions, and test symmetric block ciphers.

```bash
# Set strict file permissions so only your user profile can access sensitive data files
chmod 600 .passkey

# Output file contents to your terminal window to inspect layout formats
cat .passkey

# Encrypt your password string using the text word inside your .passkey file as the passphrase
printf "your_db2_password" | openssl enc -aes-256-cbc -pass pass\$(cat .passkey) -out password.enc

# Decrypt the binary package stream back to plain-text string formatting
openssl enc -aes-256-cbc -d -pass pass\$(cat .passkey) -in password.enc
```
