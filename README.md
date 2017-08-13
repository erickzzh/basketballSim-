# basketballSim-

1.  install python wrapper for non-commercial use
```
$ pip install ohmysportsfeedspy
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
4. run the getData.py file and follo the instructions, data should be stored in a local filed called "results"
