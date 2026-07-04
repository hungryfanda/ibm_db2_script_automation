from pathlib import Path

def load_password(path: str = ".passkey") -> str:
    p = Path(path)
    if p.exists():
        value = p.read_text(encoding="utf-8").strip()
        if value:
            return value
    return ""

database = "testdb2"
hostname = "localhost"
port = "50000"
protocol = "TCPIP"
uid = "db2inst1"
pwd = load_password()

# Create Hidden Password File
# > echo '<PASSWORD>' > .passkey
# > chmod 600 .passkey