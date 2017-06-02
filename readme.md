# Merit Money

Merit Money is a simple Python application that I'm using to learn the basics of building python applications.  

The idea of 'Merit Money' is a concept by Jurgen Apello that he mentions in his Management 3.0 book.  The basic idea is that bonuses are generally demotivating for people.  Often, people wrong associate bonuses with the thing that they did just before they got the bonus and focus all their energy on doing just that thing in the hope that they will be rewarded with a bonus.  When that bonus is not forthcoming, it is extremely demotivating.

Jurgen argues that a much better way of giving staff bonuses is to allow the entire team to give rewards based on merit.  People should be rewarded for the behaviors they exhibit rather than the work they complete.  Giving people a reward for completing a project, no matter how they did it is a bad thing.  Giving people a reward for demonstrating company values is a good thing.

The best people to spot this good behavior are colleagues.  Rewards should not be given on a schedule, they should be given on a random basis.  

The idea of merit money is to give all staff an allocation of 'merits' that they can give away to other staff if they do something worthy of merit.  There is an exchange rate of 'merits' to cash that fluctuates on company performance.

On a random basis, staff will be given an opportunity to cash in their merits or they can keep them until the exchange rate is more favourable.

## Getting Started with Python

The idea of this project is to give me a chance to practice with Python while building something useful.  I'll be making lots of notes around the basic things I do while getting started.  Don't expect any revelations here!

### Setting up the project

* Atom Editor *
We'll be using 'Atom' as our text editor for the project.  To get it setup, go to https://atom.io/ and download the appropriate version.

* Python *
Of course we'll need Python, so grab it from https://www.python.org/.

* PIP *
We'll need `pip` to help us install other Python packages which makes it easy to use packages created by other people.  When we install python we actually get another tool, `easy_install` that makes it easy to install `pip`.  To get pip installed do:

```
sudo easy_install pip
```

* VirutalEnv *

(See https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/?utm_source=feedly) for more tips)

When developing Python applications we often make use of other frameworks and supporting tools.  We could install these globally so they are available to every project, however, its fairly common for some of these libraries to clash.  We often want to isolate our development environments from project to project.  `VirtualEnv` allows us to do just that.

1.  Install VirtualEnv with `sudo pip install virtualenv`.
2.  Create a folder for our project `mkdir meritmoney`.
3.  Create the virtual env for the project `virtualenv env`.
(The convention is that the virtualenv folder is called `env` and lives inside the project folder).
4.  Activate the environment so that all executables are run from the virtualenv for the project and any installations are added to the virtualenv and not added globally.  `source env/bin/activate`.  This will set the env for the currently open terminal.  If you close the terminal you will need to reactivate.

### Installing Flask

(See https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask for some more info)

We want to start by making a simple API, just to see how it compares to other languages.  A simple REST API is a nice and simple thing without too many complicated concepts.

A useful Python framework for building applications, and specifically API's, is `Flask`.  To install `Flask` into our virtual env (assuming we have activated our environment and still have the terminal open) we use `pip install flask`.






Listing all the add-ons we need for our environment can be done automatically using `pip freeze > requirements.txt`.  Once this is done, anyone that needs to get all the necessary dependencies can use requirements.txt.
