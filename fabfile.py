from fabric.api import local


def play():
    local('python -i play.py')


def test():
    local('tox')
