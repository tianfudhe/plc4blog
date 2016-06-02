Title: Problems In Lubuntu
Date: 2016-06-01 09:40
Category: trouble-shooting
Tags: ubuntu

## Dark Input Panel
After the installation of Lubuntu, I adopted Pin'Yin input method, and was going to write something, but **black input panel poped out with no content**.
  
The solution is as follows:
- open terminal
- execute this:
```bash
killall fcitx-qimpanel
```

## Enable/Disable mouse pad for notebooks
Fn function key does not work... so I cannot disable the mouse pad, the solution is here:
- To disable mouse pad
```bash
sudo modprobe -r psmouse
```
- To enable mouse pad
```bash
sudo modprobe psmouse
```
You can configure shortcut keys for this execution.

## No sound and volume control in lxpanel
```bash
sudo apt-get install pulseaudio
sudo apt-get install pavucontrol
```

## 