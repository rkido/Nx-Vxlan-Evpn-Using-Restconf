import os

dockerpref = "docker run -v ~/Projects/postman:/etc/newman -t postman/newman_alpine33 run -k "
#dockerpref = "docker run -v ~/Projects/postman:/etc/newman -t postman/newman_ubuntu1404 run -k "
dockercollections = ['"VXLAN 1. Underlay Configuration.postman_collection.json"', \
                    '"VXLAN 2. PIM RP Underlay Configuration.postman_collection.json"', \
                     '"VXLAN 3. Overlay Configuration.postman_collection.json"', \
                     '"VXLAN 4. SPINE BGP Configuration.postman_collection.json"', \
                     '"VXLAN 5. LEAF BGP Configuration.postman_collection.json"', \
                     '"VXLAN 6. Access Port Configuration.postman_collection.json"']
dockerglobals = ' -g "globals.postman_globals.json"'
dockerenvironments = ["""nx-osv9000-1.postman_environment.json""", """nx-osv9000-2.postman_environment.json""", \
                      """nx-osv9000-3.postman_environment.json""", """nx-osv9000-4.postman_environment.json""", \
                      """nx-osv9000-5.postman_environment.json""", """nx-osv9000-6.postman_environment.json""", \
                      """nx-osv9000-7.postman_environment.json""", """nx-osv9000-8.postman_environment.json"""]

### RUN VXLAN UNDERLAY CONFIG ###
for i in dockerenvironments:
    y = dockerpref + '"VXLAN 1. Underlay Configuration.postman_collection.json"' + dockerglobals + " --environment=" + i + " --bail"
    os.system(y)

### RUN PIM RP UNDERLAY CONFIG ###
for i in dockerenvironments:
    if i == """nx-osv9000-1.postman_environment.json""" or i == """nx-osv9000-2.postman_environment.json""":
        y = dockerpref + '"VXLAN 2. PIM RP Underlay Configuration.postman_collection.json"' + dockerglobals + " --environment=" + i + " --bail"
        os.system(y)
    else:
        pass

### CONFIGURE OVERLAY ###
for i in dockerenvironments:
    if i == """nx-osv9000-5.postman_environment.json""" or i == """nx-osv9000-6.postman_environment.json""" \
            or i == """nx-osv9000-7.postman_environment.json""" or i == """nx-osv9000-8.postman_environment.json""":
        y = dockerpref + '"VXLAN 3. Overlay Configuration.postman_collection.json"' + dockerglobals + " --environment=" + i + " --bail"
        os.system(y)
    else:
        pass

### CONFIGURE SPINE BGP ###
for i in dockerenvironments:
    if i == """nx-osv9000-1.postman_environment.json""" or i == """nx-osv9000-2.postman_environment.json""" \
            or i == """nx-osv9000-3.postman_environment.json""" or i == """nx-osv9000-4.postman_environment.json""":
        y = dockerpref + '"VXLAN 4. SPINE BGP Configuration.postman_collection.json"' + dockerglobals + " --environment=" + i + " --bail"
        os.system(y)
    else:
        pass

### CONFIGURE LEAF BGP ###
for i in dockerenvironments:
    if i == """nx-osv9000-5.postman_environment.json""" or i == """nx-osv9000-6.postman_environment.json""" \
            or i == """nx-osv9000-7.postman_environment.json""" or i == """nx-osv9000-8.postman_environment.json""":
        y = dockerpref + '"VXLAN 5. LEAF BGP Configuration.postman_collection.json"' + dockerglobals + " --environment=" + i + " --bail"
        os.system(y)
    else:
        pass

### CONFIGURE ACCESS PORTS FOR VNI7348 on NX-OSv9000-6 and NX-OSv9000-8 ###
for i in dockerenvironments:
    if i == """nx-osv9000-6.postman_environment.json""" or i == """nx-osv9000-8.postman_environment.json""":
        y = dockerpref + '"VXLAN 6. Access Port Configuration VNI 7348.postman_collection.json"' + dockerglobals + " --environment=" + i + " --bail"
        os.system(y)
    else:
        pass

### CONFIGURE ACCESS PORT FOR VNI8348 on NX-OSv9000-8 ###
for i in dockerenvironments:
    if i == """nx-osv9000-8.postman_environment.json""":
        y = dockerpref + '"VXLAN 7. Access Port Configuration VNI 8348.postman_collection.json"' + dockerglobals + " --environment=" + i + " --bail"
        os.system(y)
    else:
        pass