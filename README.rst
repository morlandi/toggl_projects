toggl_client
============

Download a projects summary from Toggl in CSV format.

Installation
------------

::

    pip install git+https://github.com/morlandi/toggl_projects

Sample usage
------------

::

    $ python test_client.py

        id,name,wid,cid,cname,active,budget,actual_hours,billable,created_at,is_private
        ...

Authentication
--------------

A sample config file "~/.toggl_projects.conf" is automatically created on first run.

You should edit it to supply appropriate credentials::

    [general]
     api_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
