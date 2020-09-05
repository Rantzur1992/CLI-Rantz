Technical Exam for JFrog by Ran Tzur.<br>
A CLI for Artifactory built in python.<br>

<b>Install using:</b>

```sh
$ pip install CLI-Rantz
```

<b>Or install by using the Artifactory Saas instance</b><br>
```sh
$ pip install CLI-Rantz -i https://rantz.jfrog.io/artifactory/api/pypi/jfrog-exam/simple
```


<b>This uses f literals thus requires python3</b><br>

First navigate to where the package installation is on your local machine(Where pip installs the script)<br>
After that, to see how to use the CLI, do python(or python3 if you are not using pycharm terminal) main.py --help<br>
[![example-1.png](https://i.postimg.cc/9f3VMzPK/example-1.png)](https://postimg.cc/FYxwCrBV)
<br>

You can also use --help on specific commands, for example:

[![example-2.png](https://i.postimg.cc/7P2h5cfc/example-2.png)](https://postimg.cc/NLQBVd87)
<br>

<b>Please note this will work ONLY on the SaaS artifactory</b><br>
<b>You will need to specify your artifactory server name for each command</b><br>
[![example-3.png](https://i.postimg.cc/15MQXcc2/example-3.png)](https://postimg.cc/TpySHbsJ)
<br>

The Artifactory username and password are prompted when entering a command which requires them.<br>
You can also pass them as options to the command.<br>
[![example-4.png](https://i.postimg.cc/1zLgy943/example-4.png)](https://postimg.cc/NykG4v13)

Access tokens are created automatically on each command.<br>
By default, they are set to admin, and expires in one hour.


