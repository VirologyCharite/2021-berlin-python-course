# Notes from day 1

-flow of control: (if/then/else.loop)

-all programs start small!! 

Terry text editor emacs

make a github account send username . 

```sh
pwd ( print working directory)
apt install
mkdir 
```

```sh
# Make a symbolic link to the windows files.
ln -s /mnt/c/Users/USERNAME/Desktop
```

```sh
python hello.py
print ('hello')

cd ( going home )
ls (long listing of what there is) 
ls -l  
ls / 

rm (remove) 
rmdir
```


### symbolic link creation (shell windows to ubuntu):

```sh
 ln -s /mnt/c/Users/JFD/Desktop/Python/
```

What is pycharm ???
 
the shell and unix utilities are around for years . utilities for problems
bind it with r and python.
 
list of useful commands !!!# 

r markdown

command that is called `cat`

`cat` give it a filename it prints the 

root@LAPTOP-54VAJRD0:~/Python# cat hello.py
print('hello')root@LAPTOP-54VAJRD0:~/Python#

command that is called 
less and file 
in less you do a slash  and tap something like aattaaa  to find patterns 

/ 
b to go back 
g takes you to the top file 
G go to top 
Q to quit 
N search backwards
hit return one time

it ike being in a editor 

1. count the words in that file (dracula) 

commnad echo (is like print) it prints whatever 

echo hello phil

******** the importance of pipeline! and how to use it 
in Unix is pipeline to connect one program to another the output from one to the other 
vertical bar | it makes the program to one to the next 

echo hello phil how is your name | wc 

wc -w (just words) 
wc -c ( only letter)
cp (copy file to one place to another 
mv ( move to one place to another quit )

command tr (transliterate one thing to another ) 
echo hello phil how is your name | tr a-z A-Z 

output: HELLO PHIL HOW IS YOUR NAME

Dracula : 

cat dracula.txt |tr A-Z a-z | less 

output : dracula in lower case 

cat dracula.txt |tr A-Z a-z | tr '''\n' ( new line caracter one word per line ) but still problems theres . and , 

ctr G to know line were we are  

tail -n +29 < dracula.txt |tr A-Z a-z | tr '''\n' | tr -dc 'a-z\n' | egrep -v 'v$' | sort -n -r | uniq -c| head -n 10 | less
tail -n +29 < dracula.txt | tr A-Z a-z | tr ' ' '\n' | tr -dc 'a-z\n' | egrep -v '^$' | sort | uniq -c | sort -n -r | head -n 10  | cut -f2 -d' ' | sort
cut  -
--------------------------------------------------
Exel lists !!!

question . how many people per decade in an exel list !!
----> 

grep -i test 
( piped the matching lines -i ignore lower upper cases)

 open ( open the file ) csv tsv or exel 
 
 in the shell 
 
 cut -d, - f (field ) 1-3 ( fields in exel ) 
 
 cut -d (delimiter beween the fields )  , csv or tab 
 
 cut -d, -f-3 /users... |tail -n +2 |egrep '194 ( we show the program te dates 
 
 cut -c 1-3  ( minus character 1 to three )  to count the decades 
 
 uniq -c ( to count the people form the decades ) 
 
 sort -n -r 
 
 ###terry example = 
 
 cut -d, -f3 course-data.csv | tail -n +2 | cut -d- -f1 | cut -c1-3 | sort | uniq -c | sort -n -r
 
 sed ( string editor , edits and write it out -e 's/$//0s/' ( dollar signs means end of line ) 
 
 (every time you see an end of the line )
 
 sort -nr ( sort numerically and in reverse ) 
upohat beginning of the line 

cut -d, -f3 course-data.csv | tail -n +2 | cut -d- -f1 | cut -c1-3 | sort | sed -e 's/^/were born in the /' |  sed -e 's/$/0s/' | sort | uniq -c | sort -nr
**************************************

Python program writing 

read a fasta file and tell us if there is any duplicate names or if fasta files are ok 

------------------------------
biopython 
 
 type ls 
 tell you whatt ls is for exmaple 
 
 called conda miniconda 
 install miniconda in unix environment 
 
 install bash command 
 
 to go out of pyhin ctr D 
 or type quit ()
 
 to enter the environment of conda  
 
 conda activate bpenv
 
 search for sequences that are longer that certain lenghth 
 the number of ns more than 5% ns 
 calculate the CG% 
 
 if len print 
