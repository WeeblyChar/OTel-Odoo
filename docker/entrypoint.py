import sys
import odoo

import os
os.environ["PYTHONPATH"] = "/usr/local/lib/python3.12/dist-packages"

if __name__ == "__main__":
    sys.argv.extend(["-i", "base"])  # Ensure base module installation
    odoo.cli.main()