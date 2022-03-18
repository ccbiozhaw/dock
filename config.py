"""
set up remote hosts with a dictionary where the key is your remote address/alias and the value is the name you want displayed
hosts={
  "localhost": "local",  # this will connect to localhost, and display "local" in the list of remotes
  "remote1": "server"
}

"""

HOSTS = {
    "ccbio": {
        "alias": "sean",
        "n_cpu": 16,
    },
    "cctwo": {
        "alias": "david",
        "n_cpu": 16,
    },
}


# specify a link you want the map icon to link to. help_path="link"
HELP_PATH = "https://biocatalysis.wiki.zhaw.ch/software/autodock_for_pymol"
