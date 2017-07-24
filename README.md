<img src="https://user-images.githubusercontent.com/1143921/28504990-ef517fb8-6fba-11e7-9e82-6e732a073f13.png" align="right" width="300" height="200" />

# Nx-Vxlan-Evpn-Using-Restconf

> This is an example of how to use the ***RESTCONF*** api with Nexus 9K/3K.  We will take an 8 switch spine/leaf fabric with virtually no configuration, and build an underlay (using *IP unnumbered*) and a *BGP EVPN* L2 and L3 VXLAN overlay with *Anycast Gatway*.


## This is the Nexus fabric we are working with
![topology](https://user-images.githubusercontent.com/1143921/28494277-014e364e-6ec5-11e7-8aa3-ac975d6b4cfb.png)




## Configuration Pre-reqs
* Ansible
* Docker
* Nexus switches with Restconf support
* Mgmt address reachability and SSH but otherwise no setup
* Postman
* Newman in a Docker Container
  ```
  docker pull postman/newman_alpine33
  ```
 

## Project Files
- [scripts/vxlan_postman_collections.py](https://github.com/rkido/Nx-Vxlan-Evpn-Using-Restconf/blob/master/scripts/vxlan_postman_collections.py) - Main script to run for building the fabric.
- [restconf-netconf-switches.yml](https://github.com/rkido/Nx-Vxlan-Evpn-Using-Restconf/blob/master/playbooks/restconf-netconf-switches.yml) - The primary ansible playbook to run.
- [postman/VXLAN 1. Underlay Configuration.postman_collection.json](https://github.com/rkido/Nx-Vxlan-Evpn-Using-Restconf/blob/master/postman/VXLAN%201.%20Underlay%20Configuration.postman_collection.json) - This is Step 1 in the build process.  Each of the files **VXLAN json** files represent a step in the build process.
- [postman/nx-osv9000-1.postman_environment.json](https://github.com/rkido/Nx-Vxlan-Evpn-Using-Restconf/blob/master/postman/nx-osv9000-1.postman_environment.json) - Switch 1s postman variables.  There is a json file per switch.  These are referenced by the VXLAN json files in the build process.
- [postman/globals.postman_globals.json](https://github.com/rkido/Nx-Vxlan-Evpn-Using-Restconf/blob/master/postman/globals.postman_globals.json) - Global variables for the Postman Restconf calls.

## Usage Example
Clone the repo.  
Download the Nexus Netconf and Restconf YANG [mtx files](https://devhub.cisco.com/artifactory/open-nxos-agents/)  
Make sure you have your hosts file and group_vars directory in your /etc/ansible folder for the "cli" provider.  This is my /etc/ansible  

```
-rw-r--r--  1 root  wheel    18K Jul 12 09:06 ansible.cfg
drwxr-xr-x  8 root  wheel   272B Jul  3 17:10 group_vars/
-rw-r--r--  1 root  wheel   830B Jul 21 21:12 hosts
:ansible $ cd group_vars/
:group_vars $ ll
total 48
-rw-r--r--  1 root  wheel   117B Jul  3 17:09 border_nodes.yaml
-rw-r--r--  1 root  wheel   117B Jul  3 17:08 core.yaml
-rw-r--r--  1 root  wheel   117B Jul  2 00:05 csr1kvs.yaml
-rw-r--r--  1 root  wheel   117B Jul  3 17:09 edge_nodes.yaml
-rw-r--r--  1 root  wheel   117B Jul  3 17:10 l2_switches.yaml
-rw-r--r--  1 root  wheel    98B Jul  2 00:06 n9ks.yaml
``` 
Modify the main.yml file in the tasks folder to the proper location of your local mtx files.  
Import and Modify the Postman environment json files for your environment.  
Modify the *dockerpref* variable in [vxlan_postman_collections.py](https://github.com/rkido/Nx-Vxlan-Evpn-Using-Restconf/blob/master/scripts/vxlan_postman_collections.py) to the correct location of your [postman](https://github.com/rkido/Nx-Vxlan-Evpn-Using-Restconf/tree/master/postman) directory.

### Step 1 "Prepare the fabric for Restconf"

```
ansible-playbook restconf-netconf-switches.yml -T 30
```
### Step 2 "Run the main script to build the fabric"
This script uses the Docker container to run Restconf API POSTS to the fabric
```
python vxlan_postman_collections.py
```

### Step 3 "Verify"
I built this in VIRL and used LXC hosts to test connectivity over L3 and L2 VNIs
