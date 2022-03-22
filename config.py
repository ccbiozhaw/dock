"""
set up remote hosts with a dictionary where the key is your remote address and then additional configuratins in a nested dictionary
the alias describes the displayed name for your server, num_cpu the amount of cpus that can be used (0 => disabled) and then the port you 
connect to the docker container on. 77 is the default. dont change this unless you have to (then you have to expose a different port in your docker too)
hosts={
  "localhost": { # this will connect to localhost, and display "local" in the list of remotes
    "alias": "local" #the gui will display your localhost as local in the list of hosts
    "num_cpu": 64 #docking runs will be allowed 64 cpu cores
    "connect_on_port": 77 # by default the port 77 will connect to 22 (ssh default) on the docker 
  },  
}

"""

HOSTS = {
    "cctwo": {
        "alias": "david",
        "num_cpu": 64,
        "connect_on_port": 77,
    },
    "ccbio": {
        "alias": "sean",
        "num_cpu": 16,
    },
}

# specify a link you want the map icon to link to. help_path="link"
HELP_PATH = "https://biocatalysis.wiki.zhaw.ch/software/autodock_for_pymol"
