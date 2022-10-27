================================================
Learn Git by Building an SQL Reference Object
================================================

Git is a version control system that keeps track of all the changes you make to your 
codebase.

In this 240-lesson course, you will learn how Git keeps track of your code by creating 
an object containing commonly used SQL commands.

------------------------------------------------------------------------------------------

The first thing you need to do is start the terminal. Open a new one by clicking the 
"hamburger" menu at the top left of the window, going to the "terminal" section, and 
clicking "new terminal". Once you open a new one, type echo hello git into the terminal 
and press enter.

codeally@fc1313dc5b33:~/project$ echo hello git
hello git

------------------------------------------------------------------------------------------

You should be in the project folder in the terminal you opened. Use the terminal to 
make a new directory named sql_reference in the project folder. As a reminder, you can 
use the mkdir command to make a new folder.

codeally@fc1313dc5b33:~/project$ mkdir sql_reference

------------------------------------------------------------------------------------------

Use the "change directory" command in the terminal to change to your new folder.

codeally@fc1313dc5b33:~/project$ cd sql_reference/

------------------------------------------------------------------------------------------

Git is a version control system to keep track of your code. This folder will be your 
git repository. Turn it into one by typing git init in the terminal from this folder.

codeally@fc1313dc5b33:~/project/sql_reference$ git init
Initialized empty Git repository in /home/codeally/project/sql_reference/.git/

------------------------------------------------------------------------------------------

Use the list command with the -a flag to list the hidden folders and files.

codeally@fc1313dc5b33:~/project/sql_reference$ ls -a
.  ..  .git

------------------------------------------------------------------------------------------

The git init command created that .git folder for you. It's what keeps track of all the 
things in your repository. Use git status to see the status of where you are. This command 
will be your best friend.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

------------------------------------------------------------------------------------------

A git repository has branches to help keep track of things you are doing with your code. 
It's common to have a main branch which might be for your production code, and other 
branches for adding new features or fixing bugs. You can create and go to a new branch 
with git checkout -b new_branch. The -b stands for "branch". Use that command to switch 
to a new branch named main.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b main
Switched to a new branch 'main'

------------------------------------------------------------------------------------------

Check your status again with git status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)


------------------------------------------------------------------------------------------

Now you are on the main branch. Use the touch command to create README.md inside your 
repository. This is a file you will see in many repos to describe what the repo is for.

codeally@fc1313dc5b33:~/project/sql_reference$ touch README.md

------------------------------------------------------------------------------------------

Add the text SQL Reference at the top of your new file to let people know what your repo is for.

------------------------------------------------------------------------------------------

Check the status of your repo again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)

------------------------------------------------------------------------------------------

The file you created has not been added to git yet so it is showing that it is untracked. 
There's two steps to make git keep track of it for you. First you need to add it to the 
staging area like this: git add file_name. Add your README.md file to the staging area.

codeally@fc1313dc5b33:~/project/sql_reference$ git add README.md 

------------------------------------------------------------------------------------------

Check your status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

------------------------------------------------------------------------------------------

Now your file is in staging and will be added with the next commit. You aren't quite 
ready to commit this yet though. Use touch again to create sql_reference.json in your repo.

codeally@fc1313dc5b33:~/project/sql_reference$ touch sql_reference.json

------------------------------------------------------------------------------------------

Check your status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        sql_reference.json

------------------------------------------------------------------------------------------

You now have one file in staging and one that is untracked. Add the new file you 
created to the staging area.

codeally@fc1313dc5b33:~/project/sql_reference$ git add sql_reference.json 

------------------------------------------------------------------------------------------

Check your status one more time please.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
        new file:   sql_reference.json

------------------------------------------------------------------------------------------

Now you have two files in staging. To commit them, you can use 
git commit -m "Initial commit". 

The -m stands for "message". Often times, the first commit of a repo will have the 
message "Initial commit". Commit your two files with the message Initial commit.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "Initial commit"
[main (root-commit) f5bac49] Initial commit
 2 files changed, 1 insertion(+)
 create mode 100644 README.md
 create mode 100644 sql_reference.json

------------------------------------------------------------------------------------------

When you make a commit, whatever is in the staging area will be added to your git history. 
You can see some info in the terminal output about the commit. Check your status again 
to see what's there.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main
nothing to commit, working tree clean

------------------------------------------------------------------------------------------

Your "working tree" is clean, the files were committed and there's no other new changes 
that git recognizes. You can see your commit history with git log. Check your commit history.

codeally@fc1313dc5b33:~/project/sql_reference$ git log
commit f5bac49cfec0e05b4faa12badd0247869d9b9e79 (HEAD -> main)
Author: User <user>
Date:   Thu Oct 27 08:51:48 2022 +0000

    Initial commit

------------------------------------------------------------------------------------------

You can see the commit you made. It shows the message you gave with the commit, along 
with your username, email, the date, and a commit hash. The hash is that long string of 
characters. Open up your .json file and create an object with a reference for how to 
create a database that looks like this:

{
  "database": {
    "create": "CREATE DATABASE database_name;"
  }
}
Make sure there's one empty line at the bottom of the file and no extra spaces after 
the value or any of the curly brackets.


{
  "database": {
    "create": "CREATE DATABASE database_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check your status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

Git recognizes new unstaged changes to your file. Notice that it says that file is 
modified instead of untracked because the file has been previously committed. You can 
see the changes you made with git diff. Take a look at the new changes.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index e69de29..d2a52a9 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -0,0 +1,5 @@
+{
+  "database": {
+    "create": "CREATE DATABASE database_name;"
+  }
+}

------------------------------------------------------------------------------------------

The lines with + in front means that those lines were added. Add your new changes to 
staging with the git add command again. Make sure to put the filename you want to add 
at the end of the command.

codeally@fc1313dc5b33:~/project/sql_reference$ git add sql_reference.json 

------------------------------------------------------------------------------------------

Check your status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   sql_reference.json

------------------------------------------------------------------------------------------

Your new changes are staged and ready to be committed. Commit them with the message 
feat: add create database reference. As a reminder, here what the command to commit 
looks like: git commit -m "message".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add create database reference"
[main a69d6e6] feat: add create database reference
 1 file changed, 5 insertions(+)

------------------------------------------------------------------------------------------

Commit messages often start with fix: or feat:, among others, to help people understand 
what your commit was for. Check your git log again to see the new commit added.

codeally@fc1313dc5b33:~/project/sql_reference$ git log
commit a69d6e6d9bed622084ed5e575273e759147ca8bc (HEAD -> main)
Author: User <user>
Date:   Thu Oct 27 09:11:47 2022 +0000

    feat: add create database reference

commit f5bac49cfec0e05b4faa12badd0247869d9b9e79
Author: User <user>
Date:   Thu Oct 27 08:51:48 2022 +0000

    Initial commit

------------------------------------------------------------------------------------------

Now there's two commits in your history, the newest one is at the top. In your JSON file, 
add a drop key to your database object. Give it a value for how to drop a database similar 
to the create value. The syntax is in the hints. Again, make sure there's an empty line at 
the bottom of the file and no extra spaces after any values or curly brackets.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check your status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

Changes not staged. Check the diff quick.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index d2a52a9..229e300 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -1,5 +1,6 @@
 {
   "database": {
-    "create": "CREATE DATABASE database_name;"
+    "create": "CREATE DATABASE database_name;",
+    "drop": "DROP DATABASE database_name;"
   }
 }

------------------------------------------------------------------------------------------

It should show one line removed and two lines added. Add your changes to the staging area.

codeally@fc1313dc5b33:~/project/sql_reference$ git add sql_reference.json 

------------------------------------------------------------------------------------------

Commit your staged changes with the message, "feat: add drop database reference"

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add drop database reference"
[main 8e995b5] feat: add drop database reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

I think you're catching on. Check the log again.

codeally@fc1313dc5b33:~/project/sql_reference$ git log
commit 8e995b5a972103b8586216cc4fb8af839f7905d2 (HEAD -> main)
Author: User <user>
Date:   Thu Oct 27 09:17:35 2022 +0000

    feat: add drop database reference

commit a69d6e6d9bed622084ed5e575273e759147ca8bc
Author: User <user>
Date:   Thu Oct 27 09:11:47 2022 +0000

    feat: add create database reference

commit f5bac49cfec0e05b4faa12badd0247869d9b9e79
Author: User <user>
Date:   Thu Oct 27 08:51:48 2022 +0000

    Initial commit

------------------------------------------------------------------------------------------

Now there's three commits. You have been making changes to your main branch. You 
actually want to try and avoid that. Type git branch to see the current branches in 
your repo.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
* main

------------------------------------------------------------------------------------------

You only have the main branch still. You can create a branch with git branch branch_name. 
Branches often start with fix/ or feat/, among others, like commit messages, but they use 
a forward slash and can't contain spaces. Create a new branch named 
feat/add-create-table-reference.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch feat/add-create-table-reference

------------------------------------------------------------------------------------------

Your new branch is a clone of the main branch since that's the branch you were on when 
you created it. It will have the same code and commit history as main did at the time 
of the branch creation. View your branches again with git branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
  feat/add-create-table-reference
* main

------------------------------------------------------------------------------------------

You can see your new branch, but you are still on the main branch, as denoted with the *. 
To switch to a branch use: git checkout branch_name. Switch to your new branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-create-table-reference
Switched to branch 'feat/add-create-table-reference'

------------------------------------------------------------------------------------------

It says you switched to your new branch. Type git branch so I can make sure the * switched.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
* feat/add-create-table-reference
  main

------------------------------------------------------------------------------------------

Like I said, you often don't want to make commits directly to the main branch of a repo. 
This branch will be for some new changes. What you will do is make the changes and 
commits here, then merge them into the main branch when they are ready. Add a reference 
for creating an SQL table to your json file along side your database property. 
Make it look like this:

"table": {
  "create": "CREATE TABLE table_name;"
}


{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Show me the status again. You might as well get used to it.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-create-table-reference
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

Changes not staged. Check the diff quick so you can make sure your changes look good.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 229e300..9bbcdb1 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -2,5 +2,8 @@
   "database": {
     "create": "CREATE DATABASE database_name;",
     "drop": "DROP DATABASE database_name;"
+  },
+  "table": {
+    "create": "CREATE TABLE table_name;"
   }
 }

------------------------------------------------------------------------------------------

You made new changes so the file shows up as not staged. Add the file to staging so 
you can commit the changes.

codeally@fc1313dc5b33:~/project/sql_reference$ git add sql_reference.json 

------------------------------------------------------------------------------------------

The changes are now in staging. Commit your staged changes with the message 
"feat: add create table reference".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add create table reference"
[feat/add-create-table-reference 85e8681] feat: add create table reference
 1 file changed, 3 insertions(+)

------------------------------------------------------------------------------------------

Check your git log again.

codeally@fc1313dc5b33:~/project/sql_reference$ git log
commit 85e86815e7b55144e9997d5310cb0204be7a0cf9 (HEAD -> feat/add-create-table-reference)
Author: User <user>
Date:   Thu Oct 27 09:27:32 2022 +0000

    feat: add create table reference

commit 8e995b5a972103b8586216cc4fb8af839f7905d2 (main)
Author: User <user>
Date:   Thu Oct 27 09:17:35 2022 +0000

    feat: add drop database reference

commit a69d6e6d9bed622084ed5e575273e759147ca8bc
Author: User <user>
Date:   Thu Oct 27 09:11:47 2022 +0000

    feat: add create database reference

commit f5bac49cfec0e05b4faa12badd0247869d9b9e79
Author: User <user>
Date:   Thu Oct 27 08:51:48 2022 +0000

    Initial commit

------------------------------------------------------------------------------------------

Now you have four commits, they are getting a little hard to see. Check the log again, 
but this time use the --oneline flag to condense the output so it's more readable.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
85e8681 (HEAD -> feat/add-create-table-reference) feat: add create table reference
8e995b5 (main) feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

That's better. Use git checkout to switch back to the main branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

You may have noticed that the code you added disappeared from the JSON file. Your 
changes were added on the feat/add-create-table-reference branch so they don't exist on 
this branch. Check the log of the main branch, use the --oneline flag again.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
8e995b5 (HEAD -> main) feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

You can see three commits on this branch and four on the feature branch you were just on. 
The commit and code you added on the feature branch only exist over there for now. View 
the branches you have to remind me the name of your other branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
  feat/add-create-table-reference
* main

------------------------------------------------------------------------------------------

You created the feat/add-create-table-reference branch, made a commit, and now it's 
ready to be added to the main branch. You can use git merge branch_name to bring changes 
from a branch into the branch you are currently on. Merge the changes from your feature 
branch into the main branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge feat/add-create-table-reference
Updating 8e995b5..85e8681
Fast-forward
 sql_reference.json | 3 +++
 1 file changed, 3 insertions(+)

------------------------------------------------------------------------------------------

The commits and code from your feature branch were added to this branch. There's a 
message with some info about the merge. Check the log with the --oneline flag again.

odeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
85e8681 (HEAD -> main, feat/add-create-table-reference) feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

The feat: add create table reference commit you made on your feature branch was added 
to this branch with the merge. You can delete a branch with git branch -d branch_name. 
-d stands for "delete". Since your changes were added, you can safely delete your feature 
branch. Do that now.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d feat/add-create-table-reference
Deleted branch feat/add-create-table-reference (was 85e8681).

------------------------------------------------------------------------------------------

It said it was deleted, but view your branches again for me to verify that it's gone.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
* main

------------------------------------------------------------------------------------------

You're just left with the main branch... Want to try it again? Last time you created a 
branch and then switched to it. You can do both at the same time with 
git checkout -b branch_name. 

Create and switch to a new branch named feat/add-drop-table-reference.

odeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b feat/add-drop-table-reference
Switched to a new branch 'feat/add-drop-table-reference'

------------------------------------------------------------------------------------------

Add a drop key to the table object of your JSON file. Give it a value for how to drop a 
table. The syntax is in the hints.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name;",
    "drop": "DROP TABLE table_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check your status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-drop-table-reference
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

Check the diff so you can confirm you like your changes.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 9bbcdb1..e91bec5 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -4,6 +4,7 @@
     "drop": "DROP DATABASE database_name;"
   },
   "table": {
-    "create": "CREATE TABLE table_name;"
+    "create": "CREATE TABLE table_name;",
+    "drop": "DROP TABLE table_name;"
   }
 }

------------------------------------------------------------------------------------------

Add your changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add sql_reference.json 

------------------------------------------------------------------------------------------

Commit your staged changes with the message "feat: add drop table reference".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add drop table reference"
[feat/add-drop-table-reference eb3f478] feat: add drop table reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Switch back your main branch so you can merge in these changes.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

Remember that the code and commit you added aren't on this branch, so they disappeared 
again. View the branches on your repo so you can get the name of it to merge your feature 
into the main branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
  feat/add-drop-table-reference
* main

------------------------------------------------------------------------------------------

Merge your feature branch into the main branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge feat/add-drop-table-reference
Updating 85e8681..eb3f478
Fast-forward
 sql_reference.json | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

The commit from your feature branch was added to the main branch so you can safely 
delete the feature branch. Delete your feature branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d feat/add-drop-table-reference
Deleted branch feat/add-drop-table-reference (was eb3f478).

------------------------------------------------------------------------------------------

You're getting the hang of it. The process is to create a branch, make the changes you 
want, commit them, and then merge the changes into branch you started on. Pretty simple, 
lets keep going. Create and checkout a new branch named feat/add-column-references.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b feat/add-column-references
Switched to a new branch 'feat/add-column-references'

------------------------------------------------------------------------------------------

This branch will be a work in progress. Add a column key to your JSON object. Make it an 
object like the other two. Give it a single property, add, that has the value 
"ALTER TABLE table_name ADD COLUMN column_name;".

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name;",
    "drop": "DROP TABLE table_name;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

View the diff to make sure your new changes are what you expect.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index e91bec5..2d390d3 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -6,5 +6,8 @@
   "table": {
     "create": "CREATE TABLE table_name;",
     "drop": "DROP TABLE table_name;"
+  },
+  "column": {
+    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
   }
 }

------------------------------------------------------------------------------------------

Add your changes to staging. Here's a tip: you can use "git add ." to add all files to 
staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your staged changes with the message feat: add column reference.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add column reference"
[feat/add-column-references 8d9942f] feat: add column reference
 1 file changed, 3 insertions(+)

------------------------------------------------------------------------------------------

View your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
8d9942f (HEAD -> feat/add-column-references) feat: add column reference
eb3f478 (main) feat: add drop table reference
85e8681 feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

The commit was added. I see an error in the syntax of one of the commands. You want to 
fix it, but this branch is not for fixing it. Switch back to your main branch so you can 
create a new branch to fix it.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

Remember that, when you create a branch, it will be a clone of whatever branch you are 
on when you create it. That's why you switched to main first. Create and switch to a 
branch named fix/create-table-syntax.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b fix/create-table-syntax
Switched to a new branch 'fix/create-table-syntax'

------------------------------------------------------------------------------------------

The create table command is a function, so it needs parenthesis () at the end. 
Add those to the end of the command.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check your status and diff to see your new changes. Then, add your files to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch fix/create-table-syntax
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")


codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index e91bec5..11761b7 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -4,7 +4,7 @@
     "drop": "DROP DATABASE database_name;"
   },
   "table": {
-    "create": "CREATE TABLE table_name;",
+    "create": "CREATE TABLE table_name();",
     "drop": "DROP TABLE table_name;"
   }
 }

 codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your changes with the message fix: create table syntax.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "fix: create table syntax"
[fix/create-table-syntax 770c936] fix: create table syntax
 1 file changed, 1 insertion(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Switch back to your main so you can merge this important bug fix.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

View your branches to remind me of the branch name.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
  feat/add-column-references
  fix/create-table-syntax
* main

------------------------------------------------------------------------------------------

Merge your bug fix branch into this branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge fix/create-table-syntax
Updating eb3f478..770c936
Fast-forward
 sql_reference.json | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

------------------------------------------------------------------------------------------

View your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
770c936 (HEAD -> main, fix/create-table-syntax) fix: create table syntax
eb3f478 feat: add drop table reference
85e8681 feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

The bug fix is in and you can safely delete the branch. Go ahead and delete the branch 
that was for that fix. View your branches if you need to find the name.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d fix/create-table-syntax
Deleted branch fix/create-table-syntax (was 770c936).

------------------------------------------------------------------------------------------

Your bug fix is merged into the main branch. Switch back to your feature branch so 
you can continue adding column references.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-column-references
Switched to branch 'feat/add-column-references'

------------------------------------------------------------------------------------------

View your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
8d9942f (HEAD -> feat/add-column-references) feat: add column reference
eb3f478 feat: add drop table reference
85e8681 feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

You created this branch and made a commit. Since then, a commit for a bug fix was 
added to main. This is common with many people working on a codebase simultaneously. 
You need to update this branch so it has the same commits from main, but you can't just 
merge that branch into this one. You need that bug fix commit to be in the same order 
here as it is on main, right after the "drop table" commit. You need to rebase this 
branch against main to do that. Enter git rebase main to rebase this branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase main
First, rewinding head to replay your work on top of it...
Applying: feat: add column reference
Using index info to reconstruct a base tree...
M       sql_reference.json
Falling back to patching base and 3-way merge...
Auto-merging sql_reference.json

------------------------------------------------------------------------------------------

There was some fancy output there, but you can see the parenthesis from the bug fix 
commit were added to the table.create value. Show me the log again with the same flag 
you have been using so you can see what happened.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
f1ba20c (HEAD -> feat/add-column-references) feat: add column reference
770c936 (main) fix: create table syntax
eb3f478 feat: add drop table reference
85e8681 feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

The logs show that the bug fix commit from main was added, and then the commit from this 
branch was added on top of it. Now, when this branch is ready to be merged into main, 
it will have the same commit history. You should try to keep your branches up to date 
like this by rebasing them often. In your JSON file, add a drop key to the column 
object with a reference for dropping a column. The syntax is in the hints, give it a 
try first.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
    "drop": "ALTER TABLE table_name DROP COLUMN column_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check your status and diff to see your new changes. Then, add your changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-column-references
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")


codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 72cdf00..45ed6b0 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -8,6 +8,7 @@
     "drop": "DROP TABLE table_name;"
   },
   "column": {
-    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
+    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
+    "drop": "ALTER TABLE table_name DROP COLUMN column_name;"
   }
 }

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your changes with the message: "feat: add drop column reference".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add drop column reference"
[feat/add-column-references e328d91] feat: add drop column reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

View your log again. Make sure you use my favorite flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
e328d91 (HEAD -> feat/add-column-references) feat: add drop column reference
f1ba20c feat: add column reference
770c936 (main) fix: create table syntax
eb3f478 feat: add drop table reference
85e8681 feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

Switch to your main branch, there's another feature that needs to be worked on.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

Create and switch to a new branch named feat/add-insert-row-reference.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b feat/add-insert-row-reference
Switched to a new branch 'feat/add-insert-row-reference'

------------------------------------------------------------------------------------------

Pretend that this branch is for someone else working on a new feature at the same time 
you are working on the column commands. Add a row key to your JSON object. Make it an 
object with an insert key whose value is "INSERT INTO table_name(columns) VALUES(values);"

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check your status and diff so you can see your new changes. Then, add your changes to 
staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-insert-row-reference
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")


codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 11761b7..f39cf0a 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -6,5 +6,8 @@
   "table": {
     "create": "CREATE TABLE table_name();",
     "drop": "DROP TABLE table_name;"
+  },
+  "row": {
+    "insert": "INSERT INTO table_name(columns) VALUES(values);"
   }
 }

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your changes with the message: "feat: add insert row reference".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add insert row reference"
[feat/add-insert-row-reference 399cd9a] feat: add insert row reference
 1 file changed, 3 insertions(+)

------------------------------------------------------------------------------------------

This branch is finished. Switch to your main branch so you can merge this commit in.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

View your branches to find the name of the branch you want to merge.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
  feat/add-column-references
  feat/add-insert-row-reference
* main

------------------------------------------------------------------------------------------

Merge your branch with the insert row reference you were just working on into the main branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge feat/add-insert-row-reference
Updating 770c936..399cd9a
Fast-forward
 sql_reference.json | 3 +++
 1 file changed, 3 insertions(+)

------------------------------------------------------------------------------------------

Check your logs to make sure the commit was added. Then, switch to your branch for 
adding column references.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
399cd9a (HEAD -> main, feat/add-insert-row-reference) feat: add insert row reference
770c936 fix: create table syntax
eb3f478 feat: add drop table reference
85e8681 feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-column-references
Switched to branch 'feat/add-column-references'

------------------------------------------------------------------------------------------

Another commit was added to main, you should update this branch again. To be more 
specific, a rebase will "rewind" this branch to where it last matched main, then, add 
the commits from main that aren't here. After that, it adds the commits you made to this 
branch on top. rebase this branch against main so it's up to date. You should see a 
conflict...

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-column-references
Switched to branch 'feat/add-column-references'
codeally@fc1313dc5b33:~/project/sql_reference$ git rebase main
First, rewinding head to replay your work on top of it...
Applying: feat: add column reference
Using index info to reconstruct a base tree...
M       sql_reference.json
Falling back to patching base and 3-way merge...
Auto-merging sql_reference.json
CONFLICT (content): Merge conflict in sql_reference.json
error: Failed to merge in the changes.
Patch failed at 0001 feat: add column reference
hint: Use 'git am --show-current-patch' to see the failed patch
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".

------------------------------------------------------------------------------------------

The confict arose because the first commit you added to this branch changed the same 
lines as the commit from main. So it tried to add the commit, but couldn't because 
something was already there. There are sections, separated by characters (<, >, and =), 
that represent the commit you are on (HEAD) and the commit that is trying to be added 
(feat: add column reference). Fix the conflict by removing those <, >, and = characters. 
Then making the JSON object valid again.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
<<<<<<< HEAD
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);"
=======
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
>>>>>>> feat: add column reference
  }
}


{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
  }
}

------------------------------------------------------------------------------------------

Check your status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
rebase in progress; onto 399cd9a
You are currently rebasing branch 'feat/add-column-references' on '399cd9a'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

It says that you are still in the middle of rebasing and there's one file that needs to 
be merged yet. Add the file to staging like you would any other commit.

codeally@fc1313dc5b33:~/project/sql_reference$ git add sql_reference.json 

------------------------------------------------------------------------------------------

Check your status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
rebase in progress; onto 399cd9a
You are currently rebasing branch 'feat/add-column-references' on '399cd9a'.
  (all conflicts fixed: run "git rebase --continue")

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   sql_reference.json

------------------------------------------------------------------------------------------

You fixed the conflicts that arose from trying to add this commit and added them to 
staging. It says all conflicts fixed: run "git rebase --continue". Run the suggested 
command to continue the rebase.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --continue
Applying: feat: add column reference
Applying: feat: add drop column reference
Using index info to reconstruct a base tree...
M       sql_reference.json
Falling back to patching base and 3-way merge...
Auto-merging sql_reference.json

------------------------------------------------------------------------------------------

The last commit was added after you continued the rebase without conflict. The rebase 
is now finished. View your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
42c69c6 (HEAD -> feat/add-column-references) feat: add drop column reference
3f8d527 feat: add column reference
399cd9a (main, feat/add-insert-row-reference) feat: add insert row reference
770c936 fix: create table syntax
eb3f478 feat: add drop table reference
85e8681 feat: add create table reference
8e995b5 feat: add drop database reference
a69d6e6 feat: add create database reference
f5bac49 Initial commit

------------------------------------------------------------------------------------------

You can see the "insert row" commit from main was added to this branch before the two 
commits you made here. Now this branch is up to date and you can continue working on it. 
Add a rename key to the column object. The value should look like this: 
"ALTER TABLE table_name RENAME COLUMN column_name TO new_name;"

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
    "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
    "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;"
  }
}

------------------------------------------------------------------------------------------

Check your status and diff to see your new changes. Then, add the file to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-column-references
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 3a4951d..b3759a1 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -12,6 +12,7 @@
   },
   "column": {
     "add": "ALTER TABLE table_name ADD COLUMN column_name;",
-    "drop": "ALTER TABLE table_name DROP COLUMN column_name;"
+    "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
+    "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;"
   }
 }

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your changes with the message feat: add rename column reference

odeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add rename column reference"
[feat/add-column-references ee9466f] feat: add rename column reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

There's now three commits that are unique to this branch, you will come back to it later. 
Switch to the branch for adding row references.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-insert-row-reference
Switched to branch 'feat/add-insert-row-reference'

------------------------------------------------------------------------------------------

This branch is still up to date since no commits have been added to main since this 
branch was created. Add an update key to the row object with 
"UPDATE table_name SET column_name = new_value WHERE condition;" as it's value.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
  }
}

------------------------------------------------------------------------------------------

Check your status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-insert-row-reference
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

There's been a mistake. This branch was for the insert command, not the update command. 
You can put your changes aside with git stash. Stash your changes so you can add them to 
a different branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash
Saved working directory and index state WIP on add-insert-row-reference: 
399cd9a feat: add insert row reference

------------------------------------------------------------------------------------------

You might have noticed your uncommitted changes disappeared from the file. 
Check your status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-insert-row-reference
nothing to commit, working tree clean

------------------------------------------------------------------------------------------

Your working tree is clean and there's no changes git recognizes. The changes you made 
are stashed. View the things you have stashed with git stash list.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash list
stash@{0}: WIP on add-insert-row-reference: 399cd9a feat: add insert row reference

------------------------------------------------------------------------------------------

You can see one item there. Bring the changes back with git stash pop.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash pop
On branch feat/add-insert-row-reference
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (75ebad33199686f9e4455b7ca5339f9c1be60e59)

------------------------------------------------------------------------------------------

The changes from the stash reappeared in the file and git showed the status for you. 
You are right where you left of before stashing the changes. Popping a stash like that 
will remove the most recent stash and apply it to your working tree. View the list of 
your stashes again.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash list

------------------------------------------------------------------------------------------

The list is empty again. Put the changes back in the stash.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash
Saved working directory and index state WIP on add-insert-row-reference: 
399cd9a feat: add insert row reference


------------------------------------------------------------------------------------------

View the list of your stashed changes.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash list
stash@{0}: WIP on add-insert-row-reference: 399cd9a feat: add insert row reference

------------------------------------------------------------------------------------------

The changes are stashed again. View a condensed version of the changes in the latest 
stash with git stash show.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash show
 sql_reference.json | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

You can see what file was changed and how many lines were added and removed from the file. 
View the full changes of the latest stash with git stash show -p. -p stands for "patch".

codeally@fc1313dc5b33:~/project/sql_reference$ git stash show -p
diff --git a/sql_reference.json b/sql_reference.json
index f39cf0a..b2920bd 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -8,6 +8,7 @@
     "drop": "DROP TABLE table_name;"
   },
   "row": {
-    "insert": "INSERT INTO table_name(columns) VALUES(values);"
+    "insert": "INSERT INTO table_name(columns) VALUES(values);",
+    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
   }
 }

------------------------------------------------------------------------------------------

Now you can see the actual changes that are stored in the stash. Before, you used the 
pop command to removed the latest stash and add it to your working tree. You can add 
the latest stash while keeping it in the list with git stash apply. Apply your stash 
with this method.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash apply
On branch feat/add-insert-row-reference
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

Git showed you your status after applying the stash. The one file is unstaged again. 
View your stash list.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash list
stash@{0}: WIP on add-insert-row-reference: 512a05f feat: add insert row reference


------------------------------------------------------------------------------------------

Now there's two things stashed. You can use the name at the front of each stash 
(stash@{#}) with many of the stash commands to select one other than the latest one. 
The most recent stash is the one at the top, stash@{0}. View the condensed changes of 
the oldest stash with the git stash show command by putting the name of the stash after it.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash show stash@{0}
 sql_reference.json | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Next, using a similar method, show the full changes of the oldest stash with the 
"patch" flag you used earlier.


codeally@fc1313dc5b33:~/project/sql_reference$ git stash show stash@{0} -p
diff --git a/sql_reference.json b/sql_reference.json
index f39cf0a..b2920bd 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -8,6 +8,7 @@
     "drop": "DROP TABLE table_name;"
   },
   "row": {
-    "insert": "INSERT INTO table_name(columns) VALUES(values);"
+    "insert": "INSERT INTO table_name(columns) VALUES(values);",
+    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
   }
 }

 ------------------------------------------------------------------------------------------

There's two identical items in your stash. Drop one of them with git stash drop or 
git stash drop <stash_name>.

 codeally@fc1313dc5b33:~/project/sql_reference$ git stash drop stash@{1}

------------------------------------------------------------------------------------------

View the list of stashed changes again to verify the one got deleted.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash list
stash@{0}: WIP on add-insert-row-reference: 512a05f feat: add insert row reference

------------------------------------------------------------------------------------------

You should just have the one stash left. Switch to your main branch so you can 
create a new branch from that and add these changes to it.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
M       sql_reference.json
Switched to branch 'main'

------------------------------------------------------------------------------------------

Before I make you work on the wrong branch again. Delete the branch for inserting a row.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d feat/add-insert-row-reference
Deleted branch feat/add-insert-row-reference (was 512a05f).

------------------------------------------------------------------------------------------

Create and checkout a new branch named "feat/add-more-row-references" for 
adding some more row related commands.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b feat/add-more-row-references
Switched to a new branch 'feat/add-more-row-references'

------------------------------------------------------------------------------------------

Show me your stash list again to make sure your changes from the other branch are 
still stashed.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash list
stash@{0}: WIP on add-insert-row-reference: 512a05f feat: add insert row reference

------------------------------------------------------------------------------------------

It's still there. Pop the stash so the code gets added to this new branch.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash pop
On branch feat/add-more-row-references
nothing to commit, working tree clean
Dropped refs/stash@{0} (619b7ab4c276d736e27e07a8c9bd803e595905b9)

------------------------------------------------------------------------------------------

Git showed you your status again, and it looks like it recognizes that the file has new 
changes after adding the stash. View the stash list to verify that it's empty.

codeally@fc1313dc5b33:~/project/sql_reference$ git stash list

------------------------------------------------------------------------------------------

The list is empty. View the diff of your changes so you can make sure they are what you expect.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index f39cf0a..b2920bd 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -8,6 +8,7 @@
     "drop": "DROP TABLE table_name;"
   },
   "row": {
-    "insert": "INSERT INTO table_name(columns) VALUES(values);"
+    "insert": "INSERT INTO table_name(columns) VALUES(values);",
+    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
   }
 }

 ------------------------------------------------------------------------------------------

 It looks good. Add the changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

View your status, then commit the staged changes with the message 
"feat: add update row reference".

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-more-row-references
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   sql_reference.json

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add update row reference"
[feat/add-more-row-references e175b20] feat: add update row reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Your work on this branch is done for now. Switch to your main branch so you can merge 
the commit you just made.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

Merge your branch for adding row references that you just added a commit to.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge feat/add-more-row-references
Updating 512a05f..e175b20
Fast-forward
 sql_reference.json | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Switch to your branch for the column references so you can continue working on that.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-column-references
Switched to branch 'feat/add-column-references'

------------------------------------------------------------------------------------------

Once again, commits have been added to main so you should update this branch. 
Rebase this branch against main to bring in the new commits. You should get a conflict.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase main
First, rewinding head to replay your work on top of it...
Applying: feat: add column reference
Using index info to reconstruct a base tree...
M       sql_reference.json
Falling back to patching base and 3-way merge...
Auto-merging sql_reference.json
CONFLICT (content): Merge conflict in sql_reference.json
error: Failed to merge in the changes.
Patch failed at 0001 feat: add column reference
hint: Use 'git am --show-current-patch' to see the failed patch
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".


------------------------------------------------------------------------------------------

This conflict is a little trickier. Make the JSON object whole again so you can add 
the changes and finish rebasing. Make sure you put all the references in their correct 
objects, and in the same order they were originally in. There may be a duplicate line you 
need to delete.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
<<<<<<< HEAD
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
=======
    "insert": "INSERT INTO table_name(columns) VALUES(values);"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
>>>>>>> feat: add column reference
  }
}


{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

View the status of your repo.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
rebase in progress; onto e175b20
You are currently rebasing branch 'feat/add-column-references' on 'e175b20'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

You are still rebasing. You fixed the conflicts for the commit trying to be added. 
It looks like it was the "add column" commit that had the conflict. Add your changes to 
staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

View the status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
rebase in progress; onto e175b20
You are currently rebasing branch 'feat/add-column-references' on 'e175b20'.
  (all conflicts fixed: run "git rebase --continue")

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   sql_reference.json

------------------------------------------------------------------------------------------

Continue your rebase with the suggested command.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --continue
Applying: feat: add column reference
Applying: feat: add drop column reference
Using index info to reconstruct a base tree...
M       sql_reference.json
Falling back to patching base and 3-way merge...
Auto-merging sql_reference.json
Applying: feat: rename column reference

------------------------------------------------------------------------------------------

The rest of the commits were added without conflict. View your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
e8fe6c5 (HEAD -> feat/add-column-references) feat: rename column reference
c03aa0c feat: add drop column reference
5b737c6 feat: add column reference
e175b20 (main, feat/add-more-row-references) feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

The rebase added the "row" commits where they are supposed to be, then the "column" 
commits from this branch on top. Excellent. Now you can continue working on it. 
Add a reference to the column object for setting a column as the primary key. 
Give it a key of primary_key and a value of 
"ALTER TABLE table_name ADD PRIMARY KEY(column_name);"

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
    "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
    "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
    "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check the diff to make sure you like your changes. Then, add the changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your staged files with "feat: add primary key reference as the message".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add primary key reference"
[feat/add-column-references af7d48b] feat: add primary key reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Add foreign_key to the column object for another command. It's value should be 
"ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);".

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
    "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
    "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
    "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

Check the diff to make sure you like the changes, then add the changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit the changes with "feat: add foreign key reference" as its message.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add foreign key reference"
[feat/add-column-references 519de19] feat: add foreign key reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Go to your branch for the row references so you can continue work on those.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-more-row-references
Switched to branch 'feat/add-more-row-references'

------------------------------------------------------------------------------------------

In your JSON file, add a delete key to the row object. Take a guess at the value, it 
should include the DELETE FROM and WHERE keywords. The whole value is in the hints.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
    "delete": "DELETE FROM table_name WHERE condition;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

View the diff of your changes, then add them to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index b2920bd..5761ca5 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -9,6 +9,7 @@
   },
   "row": {
     "insert": "INSERT INTO table_name(columns) VALUES(values);",
-    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
+    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
+    "delete": "DELETE FROM table_name WHERE condition;"
   }
 }

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit the staged changes with the message "feat: add delete row reference".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add delete row reference"
[feat/add-more-row-references 9c7611d] feat: add delete row reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Go to the main branch so you can merge these commits.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main

------------------------------------------------------------------------------------------

Merge the branch for the row commands into main.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge feat/add-more-row-references
Updating e175b20..9c7611d
Fast-forward
 sql_reference.json | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

You merged the branch and are done with it. Delete the branch for the row references.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d feat/add-more-row-references
Deleted branch feat/add-more-row-references (was 9c7611d).


------------------------------------------------------------------------------------------

I missed a bunch of the rename commands when I had you work on a few of the objects. 
Create and checkout a branch named fix/add-missing-rename-references.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b fix/add-missing-rename-references
Switched to a new branch 'fix/add-missing-rename-references'

------------------------------------------------------------------------------------------

I forgot to add a command for how to rename a database. In your JSON file, add a 
rename key to the database object. The value should be 
"ALTER DATABASE database_name RENAME TO new_name;"

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;",
    "rename": "ALTER DATABASE database_name RENAME TO new_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
    "delete": "DELETE FROM table_name WHERE condition;"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

View the diff of your changes to make sure you like them, then add them to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 5761ca5..47ddd29 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -1,7 +1,8 @@
 {
   "database": {
     "create": "CREATE DATABASE database_name;",
-    "drop": "DROP DATABASE database_name;"
+    "drop": "DROP DATABASE database_name;",
+    "rename": "ALTER DATABASE database_name RENAME TO new_name;"
   },
   "table": {
     "create": "CREATE TABLE table_name();",

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your stages changes with "fix: add missing rename database reference" for the message.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "fix: add missing rename database reference"
[fix/add-missing-rename-references c76e1fe] fix: add missing rename database reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Leave this branch for now. Switch back to your branch for the column references so you 
can hopefully finally finish it.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout feat/add-column-references
Switched to branch 'feat/add-column-references'

------------------------------------------------------------------------------------------

There was a commit to main since you last worked on this from when you merged the 
"add more row references" branch. Rebase this branch against main so it's up to date 
and you can finish working on it.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase main
First, rewinding head to replay your work on top of it...
Applying: feat: add column reference
Using index info to reconstruct a base tree...
M       sql_reference.json
Falling back to patching base and 3-way merge...
Auto-merging sql_reference.json
CONFLICT (content): Merge conflict in sql_reference.json
error: Failed to merge in the changes.
Patch failed at 0001 feat: add column reference
hint: Use 'git am --show-current-patch' to see the failed patch
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".

------------------------------------------------------------------------------------------

Fix the conflicts so that all the commands are in their correct objects.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
<<<<<<< HEAD
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
    "delete": "DELETE FROM table_name WHERE condition;"
=======
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
>>>>>>> feat: add column reference
  }
}


{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
    "delete": "DELETE FROM table_name WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
  }
}

------------------------------------------------------------------------------------------

You fixed the conflicts. Check your status, then add your files to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
rebase in progress; onto 9c7611d
You are currently rebasing branch 'feat/add-column-references' on '9c7611d'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Check your status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
rebase in progress; onto 9c7611d
You are currently rebasing branch 'feat/add-column-references' on '9c7611d'.
  (all conflicts fixed: run "git rebase --continue")

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   sql_reference.json

------------------------------------------------------------------------------------------

Use the suggested command to continue your rebase.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --continue
Applying: feat: add column reference
Applying: feat: add drop column reference
Using index info to reconstruct a base tree...
M       sql_reference.json
Falling back to patching base and 3-way merge...
Auto-merging sql_reference.json
Applying: feat: rename column reference
Applying: feat: add primary key reference
Applying: feat: add foreign key reference

------------------------------------------------------------------------------------------

There was a conflict when it tried to add the first commit from this branch on top of 
the one that was brought in from main. The rest of the commits were added without conflicts. 
In your JSON file, add a unique key to the column object. Give it a value of 
"ALTER TABLE table_name ADD UNIQUE(column_name);"

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
    "delete": "DELETE FROM table_name WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
    "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
    "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
    "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);",
    "unique": "ALTER TABLE table_name ADD UNIQUE(column_name);"
  }
}

(see sql_reference.json)

------------------------------------------------------------------------------------------

View the diff to make sure you like the changes, then add the changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 37df137..264a924 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -17,6 +17,7 @@
     "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
     "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
     "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
-    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
+    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);",
+    "unique": "ALTER TABLE table_name ADD UNIQUE(column_name);"
   }
 }

codeally@fc1313dc5b33:~/project/sql_reference$ git add .


------------------------------------------------------------------------------------------

Commit the stages files with "feat: add unique reference" for the message.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add unique reference"
[feat/add-column-references 50b2627] feat: add unique reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

I'm going to show you a few ways to remove or undo a commit. The first is to simply 
"travel back in time". You can use the git reset command to travel to any point in your 
commit history. Your current HEAD is a reference to the last commit you just made. 
Use git reset HEAD~1 to go back one before HEAD.

codeally@fc1313dc5b33:~/project/sql_reference$ git reset HEAD~1
Unstaged changes after reset:
M       sql_reference.json

------------------------------------------------------------------------------------------

This is a "mixed" reset and will put the changes from the commit you undid in your 
working tree. You can see that it says there's unstaged changes after the reset to your 
file. View your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
07b2a2f (HEAD -> feat/add-column-references) feat: add foreign key reference
bb0ae7e feat: add primary key reference
a5df927 feat: rename column reference
c154a71 feat: add drop column reference
4b51327 feat: add column reference
9c7611d (main) feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

Your commit for how to set a column to unique is gone. View your status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-column-references
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   sql_reference.json

no changes added to commit (use "git add" and/or "git commit -a")

------------------------------------------------------------------------------------------

View the diff.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 37df137..264a924 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -17,6 +17,7 @@
     "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
     "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
     "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
-    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
+    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);",
+    "unique": "ALTER TABLE table_name ADD UNIQUE(column_name);"
   }
 }

------------------------------------------------------------------------------------------

And the changes from the reset are back in the working tree. So when you reset to one 
commit before HEAD, it removed the most recent commit, and put all the changes in the 
working tree. If you used the --hard flag with the reset, the changes would have not 
been added to the working tree and if you used the --soft flag, the changes would have 
been added to the working tree and to staging. Add the changes back to staging so you 
can commit them again.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit the change staged files with "feat: add unique reference" for its message.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add unique reference"
[feat/add-column-references a706a55] feat: add unique reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

Reverting is a good way to undo a commit because you don't lose the commit from the history. 
You can revert the most recent commit (HEAD) with git revert HEAD. Do that now.

codeally@fc1313dc5b33:~/project/sql_reference$ git revert HEAD

------------------------------------------------------------------------------------------

Git put you into Nano and is asking you enter a commit message for the revert, but they 
added a default one for you. Don't change anything in Nano, just exit the file to use 
the default message. You can exit the file by pressing ctrl+x.

ctrl+x

[feat/add-column-references a0969fe] Revert "feat: add unique reference"
 1 file changed, 1 insertion(+), 2 deletions(-)


------------------------------------------------------------------------------------------

View the log with that flag I like again.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
a0969fe (HEAD -> feat/add-column-references) Revert "feat: add unique reference"
a706a55 feat: add unique reference
07b2a2f feat: add foreign key reference
bb0ae7e feat: add primary key reference
a5df927 feat: rename column reference
c154a71 feat: add drop column reference
4b51327 feat: add column reference
9c7611d (main) feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

Using revert to undo that commit added another commit that is the exact opposite of it. 
Enter git show into the terminal to see the last commit added (now HEAD) and its details.

codeally@fc1313dc5b33:~/project/sql_reference$ git show
commit a0969feaab0d6e98475d642c0061ecccafd2f87b (HEAD -> feat/add-column-references)
Author: User <user>
Date:   Thu Oct 27 15:37:59 2022 +0000

    Revert "feat: add unique reference"
    
    This reverts commit a706a55618968c50b9bb31e69d30c5d62f080825.

diff --git a/sql_reference.json b/sql_reference.json
index 264a924..37df137 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -17,7 +17,6 @@
     "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
     "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
     "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
-    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);",
-    "unique": "ALTER TABLE table_name ADD UNIQUE(column_name);"
+    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
   }
 }

------------------------------------------------------------------------------------------

Type "git show HEAD~1" to take a look at the details of the original commit that you 
reverted.

codeally@fc1313dc5b33:~/project/sql_reference$ git show HEAD~1
commit a706a55618968c50b9bb31e69d30c5d62f080825
Author: User <user>
Date:   Thu Oct 27 15:37:14 2022 +0000

    feat: add unique reference

diff --git a/sql_reference.json b/sql_reference.json
index 37df137..264a924 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -17,6 +17,7 @@
     "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
     "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
     "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
-    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
+    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);",
+    "unique": "ALTER TABLE table_name ADD UNIQUE(column_name);"
   }
 }

------------------------------------------------------------------------------------------

If you look at the bottom of those two messages, it shows the diff. The diff of the 
revert commit is the exact opposite of the one before it. Effectively, undoing the changes. 
You've used rebase to update this branch, but you can enter an "interactive" mode to 
manipulate commits. Type "git rebase --interactive HEAD~2" into the terminal to enter 
this mode. The HEAD~2 means you will have a chance to change the last two commits.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --interactive HEAD~2

------------------------------------------------------------------------------------------

At the top of Nano, you can see the two commits with pick next to them. Below them, 
there's a list of options for working with them. pick means that it will use the commits 
as they were. At the bottom, it says, d, drop = remove commit. Replace the word pick 
preceeding your two commits with a d to drop them both. When you are done, save the 
file and exit Nano.

drop a706a55 feat: add unique reference
drop a0969fe Revert "feat: add unique reference"

ctrl+x
Successfully rebased and updated refs/heads/feat/add-column-references.

------------------------------------------------------------------------------------------

View your log. Use the --oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
07b2a2f (HEAD -> feat/add-column-references) feat: add foreign key reference
bb0ae7e feat: add primary key reference
a5df927 feat: rename column reference
c154a71 feat: add drop column reference
4b51327 feat: add column reference
9c7611d (main) feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

Both, the commit to add the unique command and the one to revert it, were dropped. 
Enter another --interactive rebase that goes back to the --root instead of HEAD~2. 
I am going to show you how to change a commit message. --root means that the rebase will 
go back to your very first commit.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --interactive --root

------------------------------------------------------------------------------------------

You can see that the latest commit is at the bottom here. Be careful not to change the 
wrong commits. One of the options is r, reword = use commit, but edit the commit message. 
Replace pick with an r next to the commit with the message "feat: add column reference" to 
reword the message, it's the very first commit you added to this branch. When you are done, 
save the file and exit Nano. Git will put you in another Nano instance to reword the 
commit message. Don't change anything in it yet.

r 4b51327 feat: add column reference
ctrl+x

------------------------------------------------------------------------------------------

Git is waiting for you to edit the commit message. Add an s at the end of the commit 
message so it is feat: add column references. When you are done, save the file and exit Nano.

feat: add column references
ctrl+x

detached HEAD 1396a50] feat: add column references
 Date: Thu Oct 27 14:16:31 2022 +0000
 1 file changed, 3 insertions(+)
Successfully rebased and updated refs/heads/feat/add-column-references.

------------------------------------------------------------------------------------------

View your log. Use the --oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
3920cd8 (HEAD -> feat/add-column-references) feat: add foreign key reference
1c6868c feat: add primary key reference
6f5be3d feat: rename column reference
108d075 feat: add drop column reference
1396a50 feat: add column references
9c7611d (main) feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

The message was reworded, but there's a problem. Look at the commit hash for your 
Initial commit from the last two times you viewed the log, it's that string left of the 
log. They aren't the same anymore since you rebased back to the root. Same goes for the 
rest of the commits. When you rebase interactively it changes all those hashes, so git 
sees them as different commits. If you were to try and merge this into main, it 
wouldn't work because they don't share the same history anymore. For this reason, you 
don't want to do an interactive rebase where you go back passed commits unique to the 
branch you are on. Fortunately, you can fix this. Enter "git rebase main" to realign the 
history of the two branches.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase main
Current branch feat/add-column-references is up to date.

------------------------------------------------------------------------------------------

View your log again. Use the --oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
3920cd8 (HEAD -> feat/add-column-references) feat: add foreign key reference
1c6868c feat: add primary key reference
6f5be3d feat: rename column reference
108d075 feat: add drop column reference
1396a50 feat: add column references
9c7611d (main) feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

Now the hashes are the same as they were before you rebased back to --root, which is 
what they are on main. Enter another interactive rebase. Go back to the first commit you 
added to this branch, it's HEAD~5.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --interactive HEAD~5

------------------------------------------------------------------------------------------

Squashing commits means that you will take a bunch of commits and turn them into one. 
This is helpful to keep your commit history clean and something you want try to do. 
Replace pick with an s next to all your commits except the one with the message 
"feat: add column references". When you are done, save and exit the file. 
You will find yourself in another instance of Nano. Don't change anything in it yet.

pick 1396a50 feat: add column references
s 108d075 feat: add drop column reference
s 6f5be3d feat: rename column reference
s 1c6868c feat: add primary key reference
s 3920cd8 feat: add foreign key reference
ctrl+x

------------------------------------------------------------------------------------------

Nano brought up a list of all the commit messages you used for the commits. 
Don't change anything in there, just exit the file to use those messages and finish 
squashing the commits.

ctrl+x

 Date: Thu Oct 27 14:16:31 2022 +0000
 1 file changed, 7 insertions(+)
Successfully rebased and updated refs/heads/feat/add-column-references.

------------------------------------------------------------------------------------------

View your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
0a7717d (HEAD -> feat/add-column-references) feat: add column references
9c7611d (main) feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

Now all the "column" commits you made to this branch have been squashed into just the 
one commit at the top. View the log again, but use -1 instead of --oneline this time 
to view only the last commit.

codeally@fc1313dc5b33:~/project/sql_reference$ git log -1
commit 0a7717d73fb109503f7124493af2d69a3a1b2fa0 (HEAD -> feat/add-column-references)
Author: user <user>
Date:   Thu Oct 27 14:16:31 2022 +0000

    feat: add column references
    
    feat: add drop column reference
    
    feat: rename column reference
    
    feat: add primary key reference
    
    feat: add foreign key reference

------------------------------------------------------------------------------------------

You can see that your one commit has all the messages that were in Nano, which are all 
of the commits you made to this branch squashed into one commit. I think you are finally 
done with this branch. Go to your main branch so it can get merged.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

Merge your branch for adding column commands into this one.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge feat/add-column-references
Updating 9c7611d..0a7717d
Fast-forward
 sql_reference.json | 7 +++++++
 1 file changed, 7 insertions(+)

------------------------------------------------------------------------------------------

Hopefully, there were no conflicts. Delete your branch for adding information about 
column commands since you are done with it.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d feat/add-column-references
Deleted branch feat/add-column-references (was 0a7717d).

------------------------------------------------------------------------------------------

Go to your branch for adding the commands that were missing. There's one more to add.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout fix/add-missing-rename-references
Switched to branch 'fix/add-missing-rename-references'

------------------------------------------------------------------------------------------

There was added a commit to main since you last worked on this. Update this branch with 
a rebase against main.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase main
First, rewinding head to replay your work on top of it...
Applying: fix: add missing rename database reference

------------------------------------------------------------------------------------------

You viewed the most recent log with a -1 flag. You can view the last x number of 
commits with any number instead of 1. View the last five commits with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline -5
976027d (HEAD -> fix/add-missing-rename-references) fix: add missing rename database reference
0a7717d (main) feat: add column references
9c7611d feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference

------------------------------------------------------------------------------------------

This branch is up to date now. In your JSON file, add a rename key to the table object. 
The value is in the hints, but give it a try first. It follows a similar structure as 
the rest of them.

{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;",
    "rename": "ALTER DATABASE database_name RENAME TO new_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;",
    "rename": "ALTER TABLE table_name RENAME TO new_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
    "delete": "DELETE FROM table_name WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
    "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
    "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
    "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
  }
}

------------------------------------------------------------------------------------------

Check the diff of your changes, then add them changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git diff
diff --git a/sql_reference.json b/sql_reference.json
index 21d4641..fdaf589 100644
--- a/sql_reference.json
+++ b/sql_reference.json
@@ -6,7 +6,8 @@
   },
   "table": {
     "create": "CREATE TABLE table_name();",
-    "drop": "DROP TABLE table_name;"
+    "drop": "DROP TABLE table_name;",
+    "rename": "ALTER TABLE table_name RENAME TO new_name;"
   },
   "row": {
     "insert": "INSERT INTO table_name(columns) VALUES(values);",

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your staged changes with the message, "fix: add missing rename table reference".

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "fix: add missing rename table reference"
[fix/add-missing-rename-references fd0741d] fix: add missing rename table reference
 1 file changed, 2 insertions(+), 1 deletion(-)

------------------------------------------------------------------------------------------

View your last five logs with the oneline flag again.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline -5
fd0741d (HEAD -> fix/add-missing-rename-references) fix: add missing rename table reference
976027d fix: add missing rename database reference
0a7717d (main) feat: add column references
9c7611d feat: add delete row reference
e175b20 feat: add update row reference

------------------------------------------------------------------------------------------

You have two commits on this branch that could be squashed. Enter an interactive rebase 
that goes back to HEAD~2 so you can squash them.

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --interactive HEAD~2

------------------------------------------------------------------------------------------

Replace pick with s next to your commit for adding the rename table reference to 
squash it. Be careful not to do the wrong one. When you are done, save and exit Nano.

pick 976027d fix: add missing rename database reference
s fd0741d fix: add missing rename table reference

ctrl+x

------------------------------------------------------------------------------------------

The lines that don't start with a # will be the commit messages. Add a new message at the 
top of the file on it's own line. Give it the text, 
"fix: add missing rename references". 
When you are done, save and exit the file.

fix: add missing rename references
ctrl+x

[detached HEAD fe85cc6] fix: add missing rename references
 Date: Thu Oct 27 15:24:18 2022 +0000
 1 file changed, 4 insertions(+), 2 deletions(-)
Successfully rebased and updated refs/heads/fix/add-missing-rename-references.

------------------------------------------------------------------------------------------

View only the last commit in your log to see your squashed commit.

codeally@fc1313dc5b33:~/project/sql_reference$ git log -1
commit fe85cc6b95965a4c8abf04905141aa7690232898 (HEAD -> fix/add-missing-rename-references)
Author: user <user>
Date:   Thu Oct 27 15:24:18 2022 +0000

    fix: add missing rename references
    
    fix: add missing rename database reference
    
    fix: add missing rename table reference

------------------------------------------------------------------------------------------

I think this branch is ready to go. Switch to main so you can merge it.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

Merge your branch for adding the rename commands into main.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge fix/add-missing-rename-references
Updating 0a7717d..fe85cc6
Fast-forward
 sql_reference.json | 6 ++++--
 1 file changed, 4 insertions(+), 2 deletions(-)

------------------------------------------------------------------------------------------

View your branches.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch
  fix/add-missing-rename-references
* main

------------------------------------------------------------------------------------------

Delete all your branches except main.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d fix/add-missing-rename-references
Deleted branch fix/add-missing-rename-references (was fe85cc6).

------------------------------------------------------------------------------------------

I think the file is complete, thanks for making this for me. View the log with the 
oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
fe85cc6 (HEAD -> main) fix: add missing rename references
0a7717d feat: add column references
9c7611d feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

That's a nice looking commit history. There's one more thing you should learn. 
Create and checkout a branch named feat/add-gitignore.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout -b feat/add-gitignore
Switched to a new branch 'feat/add-gitignore'

------------------------------------------------------------------------------------------

Use the touch command to create a file named .env in your repo.

codeally@fc1313dc5b33:~/project/sql_reference$ touch .env

------------------------------------------------------------------------------------------

.env files are used to store environment variables for running code. Often times, 
there may be sensitive information in it. Add the text SECRET=MY_SECRET to the file.

SECRET=MY_SECRET

(see .env)

------------------------------------------------------------------------------------------

View your status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-gitignore
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .env

nothing added to commit but untracked files present (use "git add" to track)

------------------------------------------------------------------------------------------

You can see the .env file is new. Use touch again to create another file named 
.gitignore in your repo.

codeally@fc1313dc5b33:~/project/sql_reference$ touch .gitignore

------------------------------------------------------------------------------------------

View the status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-gitignore
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .env
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)

------------------------------------------------------------------------------------------

Now there's two new files that aren't tracked yet. Add the text .env to your 
.gitignore file.

.env

(see .gitignore)

------------------------------------------------------------------------------------------

View the status again.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-gitignore
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)

------------------------------------------------------------------------------------------

Now the .env file is being ignored by git because you added it to the .gitignore file. 
There are often a number of things you don't want to include in a repository, especially 
if it's publicly visible. Now, you know how to keep them from being tracked by git. Add 
your new changes to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit your changes with feat: add .gitignore for the message.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add .gitignore"
[feat/add-gitignore ca6e9b5] feat: add .gitignore
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore

------------------------------------------------------------------------------------------

Use touch to create another file named sample.env in your repo.

codeally@fc1313dc5b33:~/project/sql_reference$ touch sample.env

------------------------------------------------------------------------------------------

View the status.

codeally@fc1313dc5b33:~/project/sql_reference$ git status
On branch feat/add-gitignore
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        sample.env

nothing added to commit but untracked files present (use "git add" to track)

------------------------------------------------------------------------------------------

Git won't ignore this file. Sensitive information can be stored in the .env file, but 
people need to know the variables that are in there so they can run a repository locally. 
Add SECRET= to sample.env.

SECRET=

(see sample.env)

------------------------------------------------------------------------------------------

Now, when someone wants to run your repo, they will know that they need to create a 
.env file and add a value in it for SECRET. Add your new file to staging.

codeally@fc1313dc5b33:~/project/sql_reference$ git add .

------------------------------------------------------------------------------------------

Commit the new changes with the message feat: add sample.env.

codeally@fc1313dc5b33:~/project/sql_reference$ git commit -m "feat: add sample.env"
[feat/add-gitignore 9a443f6] feat: add sample.env
 1 file changed, 1 insertion(+)
 create mode 100644 sample.env

------------------------------------------------------------------------------------------

View the last five commits in your log with the oneline flag.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline -5
9a443f6 (HEAD -> feat/add-gitignore) feat: add sample.env
ca6e9b5 feat: add .gitignore
fe85cc6 (main) fix: add missing rename references
0a7717d feat: add column references
9c7611d feat: add delete row reference

------------------------------------------------------------------------------------------

The two commits you made to this branch can be squashed. Do an interactive rebase that 
goes back to all the commits unique to this branch (HEAD~2).

codeally@fc1313dc5b33:~/project/sql_reference$ git rebase --interactive HEAD~2

------------------------------------------------------------------------------------------

Squash your commit that was for adding the sample.env file. When you are done, 
save the file and exit Nano.

pick ca6e9b5 feat: add .gitignore
s 9a443f6 feat: add sample.env
ctrl+x

------------------------------------------------------------------------------------------

Add a new message at the very top of the file, "feat: add .gitignore and sample.env". 
When you are done, save and exit the file.

feat: add .gitignore and sample.env
ctrl+x

[detached HEAD e655ffd] feat: add .gitignore and sample.env
 Date: Thu Oct 27 16:33:01 2022 +0000
 2 files changed, 2 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 sample.env
Successfully rebased and updated refs/heads/feat/add-gitignore.

------------------------------------------------------------------------------------------

View only the last commit in your log.

codeally@fc1313dc5b33:~/project/sql_reference$ git log -1
commit e655ffd3e08c6d74911def7634f4b9e2d468d029 (HEAD -> feat/add-gitignore)
Author: user <user>
Date:   Thu Oct 27 16:33:01 2022 +0000

    feat: add .gitignore and sample.env
    
    feat: add .gitignore
    
    feat: add sample.env

------------------------------------------------------------------------------------------

Switch back to main so you can add this in.

codeally@fc1313dc5b33:~/project/sql_reference$ git checkout main
Switched to branch 'main'

------------------------------------------------------------------------------------------

Merge the branch you just made into here.

codeally@fc1313dc5b33:~/project/sql_reference$ git merge feat/add-gitignore
Updating fe85cc6..e655ffd
Fast-forward
 .gitignore | 1 +
 sample.env | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 sample.env

------------------------------------------------------------------------------------------

Delete the feature branch you just merged.

codeally@fc1313dc5b33:~/project/sql_reference$ git branch -d feat/add-gitignore
Deleted branch feat/add-gitignore (was e655ffd).

------------------------------------------------------------------------------------------

I think it's all finished. View your log with the oneline flag to see your whole history.

codeally@fc1313dc5b33:~/project/sql_reference$ git log --oneline
e655ffd (HEAD -> main) feat: add .gitignore and sample.env
fe85cc6 fix: add missing rename references
0a7717d feat: add column references
9c7611d feat: add delete row reference
e175b20 feat: add update row reference
512a05f feat: add insert row reference
1453091 fix: create table syntax
b120e07 feat: add drop table reference
9c64412 feat: add create table reference
4e66e8e feat: add drop database reference
6c6e413 feat: add create database reference
07dba64 Initial commit

------------------------------------------------------------------------------------------

Looks great. View the log one last time, without any flags, to see the details of all 
the commits. Congratulations, you are finished with your repo for now.

codeally@fc1313dc5b33:~/project/sql_reference$ git log

...

------------------------------------------------------------------------------------------