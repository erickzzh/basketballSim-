# basketballSim-

1.  install python wrapper for non-commercial use
```
$ pip install ohmysportsfeedspy

$ pip install matplotlib

$ pip install pandas
```
add 
```
        if "player" in params:
            filename += "-" + params["player"]

        if "team" in params:
            filename += "-" + params["team"]
```
under FILE v1_0.py FUNCTION  __make_output_filename


2. go to https://www.mysportsfeeds.com/login and register a username and password
3. type in the username and password into the username_password.py file
4. cd into the main file 
5. run the sortData.py file and follow the instructions, data should be stored in a local filed called "results"
