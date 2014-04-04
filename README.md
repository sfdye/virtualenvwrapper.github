virtualenvwrapper.github
===========

virtualenvwrapper.github is a template for [`virtualenvwrapper`][virtualenvwrapper] to extend its project-management features. It automatically clones a Github repository when creating a new project directory.

Installation
============
```
  $ pip install virtualenvwrapper.github
```

Usage
=====
```
  # make sure git@github.com:your_github_username/my_repo.git exists    

  $ export VIRTUALENVWRAPPER_GITHUB_USER=your_github_username
  $ mkproject -t github my_repo
  
```


[virtualenvwrapper]: https://bitbucket.org/dhellmann/virtualenvwrapper