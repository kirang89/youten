.. youten documentation master file, created by
   sphinx-quickstart on Sat Sep 20 22:19:12 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Youten-API
==================================

**Youten** is a simple app to help manage your code snippets. This documentation covers
the brains(API) behind this app.


API
***

*Note: All request-response communication should be done in JSON.*

Create a snippet
----------------
``/v1/snippets POST``

params:
    - code snippet
    - programming language

returns:
    - 201 CREATED

Get all snippets
----------------
``/v1/snippets GET``

returns:
    - JSON array of all snippets sorted by the updated time

Get all snippets by programming language
----------------------------------------
``/v1/snippets/language/<language> GET``

returns:
    - JSON array of all snippets created in the specified language

Get a particular snippet
------------------------
``/v1/snippets/<snippet_id> GET``

returns:
    - Snippet details as JSON

Update a snippet
----------------
``/v1/snippets/<snippet_id> PUT``

params: updated snippet

returns:
    - 200 OK

Delete a snippet
----------------
``/v1/snippets/<snippet_id> DELETE``

returns:
    - 200 OK

Search for a snippet
--------------------
``/v1/snippets/search POST``

params:
    - query (Could be language or even a portion of code snippet)

returns:
    - JSON array of snippets matching the query

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

