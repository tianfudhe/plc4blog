Title: How-To Add Right-click Menu in ubuntu
Date: 2016-05-31 00:34
Category: deploy notes

# How to add an item into ubuntu right-click context menu?
To achieve this, following the 2 steps below:
## Create a .desktop file
In ubuntu, all custemized context menu items are given in the format of .desktop file, all of which are settled in `~/.local/share/file-manager/actions/`.
  
Thus, the **first step is creating the .desktop file**.
```shell
mkdir ~/.local/share/file-manager/actions
vim 
```

## Edit .desktop file.
*Oh it's too late I have to sleep,* donot blame me that I would give a simple example at this time, well I think it readable enough, or you can search `Nautilus` or `PCManFM` etc. for details documentations of your file system manager.
  
`open-jupyter-here.desktop`
```
[Desktop Entry]
Type=Action
ToolbarLabel[zh_CN]=python here
ToolbarLabel[zh]=python here
Name[zh_CN]=python here
Name[zh]=python here
Profiles=profile-zero;

TargetLocation=true
TargetContext=false

[X-Action-Profile profile-zero]
Exec=/home/tianfu/Apps/anaconda2/bin/jupyter-qtconsole 
Name[zh_CN]=python
Name[zh]=python
Path=%f
```
