#!/usr/bin/env python
# coding: utf-8

# # Worksheet 01
# 
# Name: Anran Du
# UID: U30910250
# 
# ### Topics
# 
# - Git
# 
# ## Prerequisites (installations)
# 
# #### This is your checklist:
# 
# - [x] Access to terminal
# - [x] Install Git
# - [x] Sign up for a GitHub account
# - [x] Choose editor
# - [x] Set up ssh keys
# - [x] Configure git
# 
# ### Step 1: Work Environment:  Access to Terminal 
# 
# - Mac/Linux: use **Terminal**
# - Windows:
# 	- Option 1:  [Power Shell](https://www.digitalcitizen.life/simple-questions-what-powershell-what-can-you-do-it)
# 	- Option 2:  Git Bash (recommended)
# 	
# ### Step 2: Install Git
# 
# - Mac:  
# 	- [Git](https://git-scm.com/download/mac)
# - Windows:  
# 	- [Git for Windows (Git Bash)](https://gitforwindows.org/)
# - Linux:
# 	- [Install Git on Linux](https://www.atlassian.com/git/tutorials/install-git#linux)
# 
# Confirm Git is installed by typing `git --version` on your terminal
# 
# ### Step 3: Sign up for a GitHub Account
#  
#  Go to [github.com](https://github.com/)
# 
# ### Step 4: Choose a Graphical Editor
# 
# - Try Visual Studio Code
# 	* [Visual Studio Code](https://visualstudio.microsoft.com/downloads/)
# - OR one of these other editors
# 	* [Sublime Text 3](https://www.sublimetext.com/)
# 	* [Atom](https://atom.io/) 
# 	* [Notepad++](https://notepad-plus-plus.org/) (for Windows)
# 
# ### Step 5: SSH Setup
# 
# #### Mac & Linux Users
# 
# Go to home directory (in terminal)
# 
# ```bash
# % cd ~
# % pwd
# /Users/gallettilance
# ```
# 
# Go to `.ssh` directory
# 
# ```bash
# % pwd
# /Users/gallettilance
# % cd .ssh
# % pwd
# /Users/gallettilance/.ssh 
# ```
# 
# **Note:**  If you do not have the `.ssh` directory, you can create it
# 
# - if you are in your home directory:
# 	- <kbd> mkdir .ssh </kbd>  
# - if you are not in your home directory:
# 	- <kbd> mkdir ~/.ssh </kbd>  
# 
# Generate `id_rsa` keypair files if needed
# 
# - **Note:**  these `id_rsa` files contain a special password for your computer to be connect to network services (Ex:  GitHub, AWS).
# - Check to see if these files exist by typing <kbd> ls -alt</kbd>
# - If you do not have these two files (`id_rsa` and `id_rsa.pub`), create them by typing:  
# 	- <kbd> ssh-keygen</kbd>
# 	- Hit  <kbd> enter  </kbd> **3 times**
# 
# ```bash
# % pwd 
# /Users/gallettilance/.ssh
# % ls
# % ssh-keygen
# Generating public/private rsa key pair.
# Enter file in which to save the key (/Users/gallettilance/.ssh/id_rsa): 
# Enter passphrase (empty for no passphrase): 
# Enter same passphrase again: 
# Your identification has been saved in /Users/gallettilance/.ssh/id_rsa.
# Your public key has been saved in /Users/gallettilance/.ssh/id_rsa.pub.
# The key fingerprint is:
# SHA256:jmDJes1qOzDi8KynXLGQ098JMSRnbIyt0w7vSgEsr2E gallettilance@RESHAMAs-MacBook-Pro.local
# The key's randomart image is:
# +---[RSA 2048]----+
# |   .=+           |
# |.  .==           |
# |.o  +o           |
# |..+= oo          |
# |.E.+X.  S        |
# |+o=o=*oo.        |
# |++.*o.+o.        |
# |..*.oo           |
# |o= o+o           |
# +----[SHA256]-----+
# % ls
# total 16
# -rw-------  1   1675 Dec 17 12:20 id_rsa
# -rw-r--r--  1    422 Dec 17 12:20 id_rsa.pub
# % 
# ```
# 
# Navigate to the `.ssh` directory
# 
# <kbd> cd ~/.ssh </kbd>  
# 
# open `id_rsa.pub` using your editor of choice and copy its contents. Add `ssh` key to GitHub by following these steps:
# 
# - go to your [GitHub account](https://github.com/) (create one if you don't have one, and save your user name and password somewhere easily accessible for you.)
# - click on your avatar/profile picture (upper right of screen)
# - go to `Settings`
# - on left of screen, select `SSH and GPG keys`
# - Select <kbd> New SSH key </kbd>
# - for "Title":  entitle it  "GitHub key"
# - for "Key":  paste key from clipboard here
# - click <kbd> Add SSH key </kbd>
# - save, exit, confirm GitHub password as requested
# 
# #### Windows Users
# 
# Follow [How to Create SSH Keys with PuTTY on Windows](https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-putty/)
# 
# ### Step 6: Configure Git
# 
# #### Configure user name and email (lets Git know who you are)
# 
# <kbd> git config --global user.name "First Last"  </kbd>  
# <kbd> git config --global user.email "myname@email.com"  </kbd>  
# 
# To verify these additions, type:  
# <kbd> git config --list  </kbd>  
# 
# #### Default Editor
# 
# The default editor will be [Vim](https://vim.rtorr.com/). You may want to look up how to edit, save, and close vim as this can't be done with just point and click (you must use the vim commands).

# ### Git / GitHub
# 
# a) what is the difference between git and github?

# git is a version control system on laptop while github is a website to backup and host files online

# b) what command would you use to copy a repo locally?

# git clone<url>

# c) what button would you use to make a copy of a repo in GitHub?

# Fork button

# d) let's say you have a copy of a repo in GitHub but that repo changes, does your copy change too?

# It does nor change automatically but copy can be changed through using Sync fork button on Github. 

# e) what are the three commands you use to create a new save point in your git repo and back it up to GitHub?

# git status
# git add .
# git commit -m<>
# git pull
# git push origin<>
# 

# f) how would you make your copy change so that it has the most up-to-date version of the repo it is copied from?

# git fetch
# git merge

# g) why are there sometimes conflicts between copied repos / branches? How do you resolve them?

# In[ ]:


Because multiple people might work on the same file.

Unify the final order with the teammates
edit it again in VI
and then add it to repo

# h) describe all the steps needed to make a PR to contribute your notes to the class repository.

# Fork orginal repo
# Clone repo
# git remote add origin <url of repo>
# update changes in repo
# click new pull request button on github to raise

# i) Write here some other commands we used in class and what they mean / how to use them:

# git status:check the changes like whether files are staged or unstaged
# git add .:add changes to branch
# git commit -m"":commit changes to branch
# git-log:check commit history
