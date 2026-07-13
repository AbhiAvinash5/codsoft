
new@DESKTOP-BL8BQG7 MINGW64 ~
$ pwd
/c/Users/new

new@DESKTOP-BL8BQG7 MINGW64 ~
$ cd documents

new@DESKTOP-BL8BQG7 MINGW64 ~/documents
$ cd abhi

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi
$ git clone https://github.com/AbhiAvinash5/fsd-cse-a-1.git
Cloning into 'fsd-cse-a-1'...
warning: You appear to have cloned an empty repository.

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi
$ cd fsd-cse-a-1/

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ npm init -y
Wrote to C:\Users\new\documents\abhi\fsd-cse-a-1\package.json:

{
  "name": "fsd-cse-a-1",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
Server running at http://localhost:3000
${req.method} ${req.url}
${req.method} ${req.url}


new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        index.js
        node_modules/
        package-lock.json
        package.json

nothing added to commit but untracked files present (use "git add" to track)

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        index.js
        package.json

nothing added to commit but untracked files present (use "git add" to track)

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git add .
warning: in the working copy of 'package.json', LF will be replaced by CRLF the next time Git touches it

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   index.js
        new file:   package.json


new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git commit -m "Initial commit"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'new@DESKTOP-BL8BQG7.(none)')

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$  git config --local user.email "avinashkamella5@gmail.com"

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$  ^C

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$   git config --local user.name "avinash"

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git commit -m "Initial commit"
[main (root-commit) 540feaa] Initial commit
 3 files changed, 43 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 index.js
 create mode 100644 package.json

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 810 bytes | 810.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/AbhiAvinash5/fsd-cse-a-1.git
 * [new branch]      main -> main

new@DESKTOP-BL8BQG7 MINGW64 ~/documents/abhi/fsd-cse-a-1 (main)
$
