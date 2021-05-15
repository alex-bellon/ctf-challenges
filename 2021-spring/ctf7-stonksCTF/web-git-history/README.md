# Unpleasant or Contemptable Person
* **Event:** stonksCTF
* **Problem Type:** Web
* **Point Value / Difficulty:** Easy/Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The problem mentions that there may be an issue with the permissions on the website, and this is definitely true. If you look at the file structure of the website (which usually shouldn't be public), you can see that there are only 2 things: the homepage and a `.git` folder. Since there's nothing interesting in the homepage, you should probably start ivesitgating the `.git` folder.

#### Step 2
Git is a distributed version control system, meaning that any local copy of the repo contains in it all history associated with the repo. For this reason, if internal git folders (`.git/`) are exposed on a webserver, an attacker can discover the history of the website down the granularity of a commit. Git uses a `.git` directory with a well-defined structure in order to keep track of changes. 

To copy this folder to your machine so you can inspect it better, you can run 

```shell
wget -I .git <website>/.git/ 
```

#### Step 3
From inside the Git directory, you can use this command to see if any files have been deleted:

```shell
git log --diff-filter=D --summary | grep delete
```

Once you have the name of the file that was deleted (in this case `flag.html`), you can use this command to find the commit ID from when the file was deleted. We'll need this to look at the diff and see the exact code that was changed.

```shell
git log --all -- <file path>
```

Once you have the commit ID, just run this command to get the code (which is the flag).

```shell
git show <commit ID> -- <file path>
```

`utflag{gotta_git_that_flag}`

