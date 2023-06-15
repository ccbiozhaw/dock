
<div align="center">
  <h1>AlphaDock. A PyMol Plugin for AutoDock Vina.</h1>
</div>

## Setup 

The application consists of two parts: 
  - The GUI to access AlphaDock through PyMol.
  - The backend, where docking is performed. We recommend to run the docker container for the backend on a server/workstation, and have all users connect to it. This way not every user needs a docker installation.

<br>

### GUI - PyMol 

Download the github repository and add it to your path:
```
Plugin -> Plugin Manager -> Settings -> Add new directory ... -> Point to the downloaded repository
```
![image](https://github.com/ccbiozhaw/dock/assets/80820813/45242c1e-7798-4898-9fd8-f849debb9f15)


**Restart PyMol. The first time the plugin is loaded it will download required dependencies, so you will have to close PyMol again.**

<br>

### Docker

The docker setup is as easy as running:
```
docker run -t -d -p 77:22 dpatsch/docking:version1.2
```
<br>

### Required configuration

You need to edit the configuration file ```config.py``` in the project root to define the host address.  
**hint: i recommend to place the docking folder on a shared folder, edit the configuration file once, then have all users add this shared folder to their PyMol settings**
```
hosts={
  "localhost": { # this will connect to localhost, and display "local" in the list of remotes
    "alias": "local" #the gui will display your localhost as local in the list of hosts
    "num_cpu": 64 #docking runs will be allowed 64 cpu cores
    "connect_on_port": 77 # by default the port 77 will connect to 22 (ssh default) on the docker 
  },  
}
```

### Usage

#### Inputs

The inputs for the application are PyMOL objects/selections. You can find a dropdown list of all PyMOL items in your current session in the dropdown lists in the Inputs/Box section. If you input a .pdb file with a receptor and a ligand, you do not have to split it. Just select the receptor (in PyMOL), call it “receptor” (or any arbitrary name) and do the same for the ligand. The new objects should now show up in the dropdown menus where you can select them.

If you are not sure if you did it right, click the “preview” button. It will take your selection and pre-process it, as it would during the docking procedure, then display it as “receptor_rigid_preview” or “ligand_preview”.

**Input options**:

**rigid**: refers to the basic receptor you are used to from chimera. It means that the structure is rigid, and residues are unable to move. However, as this plugin also allows flexible residues, a distinction is necessary.  

**flex**: select residues that you want to keep flexible. This is pretty computationally expensive, and if you select too many, it will not generate meaningful results. I limited the maximum number of flexible residues to 10. If you select more, only the first 10 are processed. The preview function here is only meant to validate the pre-processing (if you get a “finished!” everything worked fine), however, displaying the flexible .pdbqt is senseless.

**ligand**: select a ligand for your docking.

**cofactor**: allows for the selection of a second “ligand”. Both of them are flexible (→ multi ligand docking). The functionality is the same as for ligands.

#### Box

The box is placed on the center of mass of a selection, and visualized with a small pseudoatom, named grid_center. You can move it around by entering the editing mode and holding down control. At the moment the box does not auto-update. Re-select the grid center to move the box (technically this is not necessary, the coordinates of the grid_center atom will always be used, no matter where the box is).


#### Outputs

The output structure is pretty important. A project directory is created in the output directory you select (if one doesn’t exist). Within this project directory, your docking-“experiments” are saved. The experiment description below may be used to describe your docking experiments and is saved in the project directory. For example you select your desktop as an output dir, and name your project SHC. Then a new folder called SHC will be created for you. Every time you dock, a new folder will be created within the SHC folder, containing all the information and files associated with your docking run. This is to ensure your docking runs are traceable, and as reproducable as possible.

there is a “experiment_log.txt” file in the Project directory, where the docking descriptions from the gui are saved during docking.


#### menu-bar (left to right):

![image](https://github.com/ccbiozhaw/dock/assets/80820813/df253565-b71a-4f5e-9d17-e3539b84d051)


**new**: starts new pymol session and resets all variables in the GUI (including output paths)
load: use this to restore a checkpoint. Navigate to the Project folder and load the "restore.pickle" file. It contains all relevant information to restore past experiments.
save: this is used to save "snapshots", for example, additional analysis done after a docking run, into its respective experiment folder. E.g. You dock something, visualize it in some way, then you can add this visualization to its respective docking run. Don't name it, only select the directory.
Settings:

**clean_up**: remove all files with “out” or “preview” in them. These are files that the Alphadock creates. Use it between docking runs if you want
history: keep track of experiments. ON by default. I recommend you keep it that way.
host: autodock vina 1.2 only runs on linux. Select which computer to run on
verbosity: get all outputs or only the final scores. Errors are always displayed
History:

Every time you dock, all files associated with the run are saved in folders, starting from 1, in the Project folder. This is done automatically, so you never overwrite past results/lose them. A dropdown list of all past experiments in a Project can be accessed in the history. Click on one, and the Pymol/GUI session at the exact moment of the docking run will be restored.

As this can add up quickly, items can be deleted from the history. You can either delete the folders directly or right-click a history item to remove it.

Every time you dock you have the option to add additional information to the run through the bottom-most line edit (default text is “Describe your experiment”). This is then stored in the experimental_log.txt file in the Project directory. If you open the history and click on it with the middle mouse button, the menu will expand to show your descriptions. You can edit these by clicking on them and confirming with “enter”. This will also update the experimental_log.txt file.

As was mentioned above in the File→ save section, you may associate your personal visualization to the history. In the Program, I call this “snapshot”, and only one snapshot can be associated with each history item. Click save to store a snapshot of your current PyMOL session in a history directory. If you open the history dropdown and hold down “CTRL”, all history items with a snapshot in them will be highlighted. Clicking on any of them will open the snapshot item rather than the history item. In case you save a snapshot in the wrong folder, you can move them around while holding “CTRL”, and if you don’t want them, you can delete them, also while holding “CTRL”.



### Literature

Autodock vina 1.2. release Publication:

https://pubs.acs.org/doi/full/10.1021/acs.jcim.1c00203

This gui is mostly a wrapper around the functions used in the official autodock 1.2. tutorial. you can read more about it here. This resource also has some interesting FAQs, i recommend you read them:

https://autodock-vina.readthedocs.io/_/downloads/en/latest/pdf/

if you want to follow along to the tutorial, download the files from the official github repo:

https://github.com/ccsb-scripps/AutoDock-Vina
