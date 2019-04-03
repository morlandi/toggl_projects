toggl_client
============

Downloads a projects summary from Toggl in CSV format.

Installation
------------

(1) Manually install TogglPy

::

    pip install git+https://github.com/morlandi/TogglPy.git

(2) then,

::

    pip install git+https://github.com/morlandi/toggl_projects


Note (2019-04-03):

I believe step (1) is no more necessary, as my modification required to retrieve
both active and inactive projects as been merged into the main repo, so you could
probably install it instead::

    pip install -U TogglPy


Sample usage
------------

::

    $ toggl_projects > projects.csv
        Using config file "/Users/morlandi/.toggl_projects.conf"

    $ cat projects.csv
        id,name,wid,cid,cname,active,budget,actual_hours,billable,created_at,is_private
        438434879,Project ACME,558467,43697041,Acme,True,,3,False,2019-01-31T08:31:35+00:00,True
        ...


Authentication
--------------

A sample config file "~/.toggl_projects.conf" is automatically created on first run.

You should edit it to supply appropriate credentials::

    [general]
     api_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
