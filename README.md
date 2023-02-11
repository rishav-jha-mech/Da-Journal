# Da Journal

#### Python Script to maintain a secure journal.


```
    ________                ____.                                 .__   
    \______ \ _____        |    | ____  __ _________  ____ _____  |  |  
    |    |  \\__  \       |    |/  _ \|  |  \_  __ \/    \\__  \ |  |  
    |    `   \/ __ \_ /\__|    (  <_> )  |  /|  | \/   |  \/ __ \|  |__
    /_______  (____  / \________|\____/|____/ |__|  |___|  (____  /____/
            \/     \/                                    \/     \/      
```

## Installation

1. Clone the repository
   ```
        git clone https://github.com/rishav-jha-mech/Da-Journal.git
   ````
2. Install the requirements
   ```
        pip install -r requirements.txt
   ```
3. Run the script
   ```
        python3 main.py
   ```

## Usage

1. At first create the files for the month using 1st option
2. Then when you are done with writing the journal, use the 2nd option to encrypt the file [Note : that the file will be encrypted and you will be given a key in the root folder `key.key` to decrypt it]
3. Now when you want to access the journal again use the 3rd option to decrypt the file and read it. [Note : that you will need the key in the root folder `key.key` to decrypt the file]

## Future Plans

- Add a web interface to access the journal.
- Better CLI interface.