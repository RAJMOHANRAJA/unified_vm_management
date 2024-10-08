# vmrunPacked

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/RAJMOHAN RAJA/vmrunPacked)
[![PyPI](https://img.shields.io/pypi/v/vmrunPacked)](https://pypi.org/project/vmrunPacked)
[![Downloads](https://pepy.tech/badge/vmrunpacked)](https://pepy.tech/project/vmrunpacked)

## Installation
```
pip install vmrunPacked
```
### About
python vmrun commands and actions execute `power` actions. `snapshot` actions. `recoard` actions. `guest os control` actions. `vprobe` actions. `general commands` actions

### Import Pkg

``` python
import vmrunPacked

vmobj = vmrunPacked.Pack("/vmx_file_path/vm.vmx",userName="admin",passWord="admin@123")
# "product" this prams defualt "ws" options ["fusion", "player"]
```

# Power Commands

In this Power command support
- start
- stop
- reset
- suspend
- pause
- unpause

### start
``` python
import vmrunPacked

vmobj = vmrunPacked.Pack("/vmx_file_path/vm.vmx",userName="admin",passWord="admin@123")
vmobj.start()

```
Starts a virtual machine (.vmx file) or team (.vmtm file). The default gui option starts the machine interactively, including startup dialog box, to allow noninteractive scripting.

### stop

stop command Parameters two `soft` and `hard`

``` python
vmobj.stop() #that call normal
vmobj.stop(soft=True) #that call soft "quick close" vm
vmobj.stop(hard=True) #that call hard "force close" vm
# Exception 
# vmobj.stop(soft=True,hard=True)
# tha case defualt "soft" parms call
```

### reset (reboot)

``` python
vmobj.reset() #that call normal
vmobj.reset(soft=True) #that call soft "quick close" vm
vmobj.reset(hard=True) #that call hard "force close" vm
# Exception 
# vmobj.reset(soft=True,hard=True)
# tha case defualt "soft" parms call
```

### suspend

``` python
vmobj.suspend() #that call normal
vmobj.suspend(soft=True) #that call soft "quick close" vm
vmobj.suspend(hard=True) #that call hard "force close" vm
# Exception 
# vmobj.suspend(soft=True,hard=True)
# tha case defualt "soft" parms call
```

### pause

``` python
vmobj.pause()
```
Pauses a virtual machine (.vmx file). You can use this either to pause replay, or to pause normal operation.

### unpause

``` python
vmobj.unpause()
```
Resumes operation of a virtual machine (.vmx file) from where you paused replay or normal operation.

# Snapshot Commands

support actions
- listSnapshots
- snapshot
- deleteSnapshot
- revertToSnapshot

### listSnapshots

view list of snap shots
``` python
val = vmobj.list_snap_shots()
print(val)
#return value type "list" 
```

### snapshot

take snap shots vmware
``` python
snap_shot_name = "demo"
val = vmobj.snapshot(snap_shot_name)
print(val)
# retun valus type "list". success when empty list
```
Creates a snapshot of a virtual machine (.vmx file). For products such as Workstation that support multiple snapshots, you must provide the snapshot name.

### deleteSnapshot

remove snap shots vmware
``` python
snap_shot_name = "demo"
val = vmobj.delete_snapshot(snap_shot_name)
print(val)
# retun valus type "list". success when empty list
```
Removes a snapshot from a virtual machine (.vmx file). For products such as Workstation that support multiple snapshots, you must provide the snapshot name.

### revertToSnapshot

``` python
snap_shot_name = "demo"
val = vmobj.revert_to_snap_shot(snap_shot_name)
print(val)
# retun valus type "list". success when empty list
```
Sets the virtual machine to its state at snapshot time. If a snapshot has a unique name within a virtual machine, revert to that snapshot by specifying the path to the virtual machine’s configuration file and the unique snapshot name.

# Record and Replay Commands

support actions
- beginRecording
- endRecording
- beginReplay
- endReplay

### beginRecording
``` python
snap_name = "rec_demo"
val = vmobj.begin_recording(snap_name)
print(val)
# retun valus type "list". success when empty list
```
Begins recording a running virtual machine (.vmx file), storing activity in the specified snapshot object, with optional description.

### endRecording
``` python
val = vmobj.end_recording()
print(val)
# retun valus type "list". success when empty list
```
Ends the recording of a virtual machine (.vmx file) that is in progress, and close its snapshot object.

### beginReplay
``` python
snap_name = "rec_demo"
val = vmobj.begin_replay(snap_name)
print(val)
# retun valus type "list". success when empty list
```
Begins replaying the recorded activity of a powered off virtual machine (.vmx file) from a snapshot object, powering off if necessary.

### endReplay
``` python
val = vmobj.end_replay()
print(val)
# retun valus type "list". success when empty list
```
Ends the replaying of a virtual machine (.vmx file) that is currently underway.

# Guest Operating System Commands

support commands
- writeVariable
- readVariable
- runProgramInGuest
- runScriptInGuest
- setSharedFolderState
- addSharedFolder
- removeSharedFolder
- listProcessesInGuest
- killProcessInGuest
- fileExistsInGuest
- deleteFileInGuest
- renameFileInGuest
- createDirectoryInGuest
- deleteDirectoryInGuest
- listDirectoryInGuest
- copyFileFromHostToGuest
- copyFileFromGuestToHost
- captureScreen

### writeVariable
``` python
var_name = "todo"
var_value = "todo_value"
vmobj.write_variable(var_name,var_value,runtimeConfig=True)
# "runtimeConfig" parms or "guestEnv"
```

### readVariable
``` python
val_name = "todo"
vmobj.read_variable(var_name,runtimeConfig=True)
# "runtimeConfig" parms or "guestEnv"
```

### runProgramInGuest
``` python
file_path = "D:\\new\\todo.bat"
vmobj.run_program_in_guest(file_path,activeWindow=True,interactive=True)
# "noWait" , "activeWindow" , "interactive" - bool value parms
```

### runScriptInGuest
``` python
interpreter_path = "C:\\Program Files\\Ruby\\ruby.exe"
file_path = "D:\\new\\init.rb"
vmobj.run_script_in_guest(interpreter_path, file_path)
``` 
Runs a command script in the guest operating system. VMware Tools and a valid guest login are required.

### setSharedFolderState
``` python
share_name = "vm"
new_path = "D:\\path"
vmobj.set_shared_folder_state(share_name, new_path,writable=True)
# "readonly" or "writable" -> bool any one prams
```
Modifies the writability state of a folder shared between the host and a guest virtual machine (.vmx file).

### addSharedFolder
``` python
share_name = "vm"
host_path = "D:\\new_path"
vmobj.add_shared_folder(share_name, host_path)
```
Adds a folder to be shared between the host and guest. The share name is a mount point in the guest file system. The path to folder is the exported directory on the host.

### removeSharedFolder
``` python
share_name = "D:\\new_path"
vmobj.remove_shared_folder(share_name)
```
Removes a guest virtual machine’s access to a shared folder on the host. The share name is a mount point in the guest file system.

### listProcessesInGuest
``` python
val = vmobj.list_processes_in_guest()
print(val)
# return value "list"
```
Lists all processes running in the guest operating system. VMware Tools and a valid guest login are required.

### killProcessInGuest
``` python
pid = "<pid>"
val = vmobj.kill_process_in_guest(pid)
print(val)
# return value "list"
```

### fileExistsInGuest
``` python
file_path = "D:\\new\\t.mp3"
val = vmobj.file_exists_in_guest(file_path)
print(val)
# return value "list"
```
Checks whether the specified file exists in the guest operating system. VMware Tools and a valid guest login are required.

### deleteFileInGuest
``` python
file_path = "D:\\new\\t.mp3"
val = vmobj.delete_file_in_guest(file_path)
print(val)
# return value "list"
```

### renameFileInGuest
``` python
old_file_name = "D:\\new\\todo.png"
new_file_name = "D:\\new\\work.png"
vmobj.rename_file_in_guest(old_file_name,new_file_name)
```
Renames or moves a file in the guest operating system. VMware Tools and a valid guest login are required.

### createDirectoryInGuest
``` python
var = "C:\\new\\own
vmobj.create_directory_in_guest(var)
```
Creates the specified directory in the guest operating system. VMware Tools and a valid guest login are required.

### deleteDirectoryInGuest
``` python
var = "C:\\new\\own
vmobj.delete_directory_in_guest(var)
```
Deletes a directory from the guest operating system. VMware Tools and a valid guest login are required.

### listDirectoryInGuest
``` python
var = "D:\\new"
val = vmobj.list_directory_in_guest(var)
print(val)
# return value "list"
```
Lists directory contents in the guest operating system. VMware Tools and a valid guest login are required.

### copyFileFromHostToGuest
``` python
host_file_path = "/home/<user>/h.txt"
guest_file_path = "D:\\h.txt"
vmobj.copy_file_from_host_to_guest(host_file_path, guest_file_path)
```

### copyFileFromGuestToHost
``` python
guest_file_path = "D:\\h.txt"
host_file_path = "/home/<user>/h.txt"
vmobj.copy_file_from_guest_to_host(guest_file_path, host_file_path)
```

### captureScreen
``` python
host_path = "/home/<user>/Pic/hub.png"
vmobj.capture_screen(host_path)
```

# VProbes Commands

support commands
- vprobeVersion
- vprobeLoad
- vprobeReset
- vprobeListProbes
- vprobeListGlobals

### vprobeVersion
``` python
vmobj.vprobe_version()
```

### vprobeLoad
``` python
script_path = "<path>"
vmobj.vprobe_load(script_path)
```

### vprobeReset
``` python
vmobj.vprobe_reset()
```

### vprobeListProbes
``` python
val = vmobj.vprobe_list_probes()
print(val)
```

### vprobeListGlobals
``` python
val = vmobj.vprobe_list_globals()
print(val)
```

# GENERAL COMMANDS

support commands
- list
- upgradevm
- installtools
- register
- unregister
- clone
- deleteVM
- listRegisteredVM
- getGuestIpAddress

### list

``` python
val = vmobj.list_vm()
print(val)
```

### upgradevm
``` python
vmobj.upgrade_vm()
```

### installtools
``` python
vmobj.install_tools()
```

### register
``` python
vmobj.register()
```

### unregister
``` python
vmobj.un_register()
```

### clone
``` python
dest_vmx_file = "D:\\new\\clone.vmx"
snap_name = "<name>"
vmobj.clone(dest_vmx_file, snap_name, full=True)
# parms "full" or "linked" -> bool 
```

### listRegisteredVM
``` python
val = vmobj.list_registered_vm()
print(val)
```

### deleteVM
``` python
vmobj.delete_vm()
```

### getGuestIpAddress
``` python
val = vmobj.get_guest_ip_address()
print(val)
```
