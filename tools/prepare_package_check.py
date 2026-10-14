"""Verified HTTPS preflight for GitHub runners blocking ICMP; tests stay active."""
from pathlib import Path
import sys

path = Path(sys.argv[1]) / "lib/common.sh"
source = path.read_text()
original = "    ping -q -c 2 yunohost.org > /dev/null 2>&1 \\\n"
replacement = "    curl --fail --silent --show-error --proto '=https' --max-time 20 https://repo.yunohost.org/incus/streams/v1/index.json > /dev/null 2>&1 \\\n    || ping -q -c 2 yunohost.org > /dev/null 2>&1 \\\n"
if source.count(original) != 1:
    raise SystemExit("Préflight amont non reconnu ; aucun test contourné.")
path.write_text(source.replace(original, replacement))
