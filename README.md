# password-manager
I need a password manager.
## Authors

- [@Hubert Sienicki](https://github.com/HubertSienicki)

## How to use the project
1. Prerequisites:

    a) Python 3.9 or above
    
    b) PostgreSQL database with a table for accounts

    c) Create a database.ini file with configuration variables inside the cloned project

    d) Special secret_key.py file with get_secret_key method that returns your master password  
    ###

2. Database.ini
    ```bash
        [postgresql]
        host=localhost
        database="your_db_name"
        user=postgres (or any user you added with enough privleges)
        password="your_db_password"
    ```

3. Get repo
```bash
    git clone https://github.com/HubertSienicki/password-manager
```

3. Change working directory

```bash
  cd cloned/project/directory
```

4. Make sure you edited the source according to point Prerequisites

5. Compile and run

## Support

For support, email kneiv112@wp.pl or dm me on discord : kneiv#8382


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
