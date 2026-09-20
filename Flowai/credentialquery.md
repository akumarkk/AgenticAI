##### flowise cred query
```

/ # cd ~/.flowise/
~/.flowise # dir
/bin/sh: dir: not found
~/.flowise # ls
database.sqlite  encryption.key   settings.json    uploads
~/.flowise # sqlite3 database.sqlite 
SQLite version 3.47.1 2024-11-25 12:07:48
Enter ".help" for usage hints.

sqlite> select * from credential
credential      credentialName  
sqlite> select * from credential
   ...> 
   ...> ;
```