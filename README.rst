Corrobo - How do I authentication with micro-services?
======================================================

Require a way to authentcate requests from one server to another.

Require a way for users to make requests to different services while
only logging in once, ie. Single-sign-on.

A few pieces are needed:

An IAM (Identity Access Management) service.
++++++++++++++++++++++++++++++++++++++++++++

Establish and manage user credentials.

Once signed in, respond to the user with an access token.

The access token should be sent with requests to your services.

There is a way for your service to trust the access token and know who
it is responding to and that they have authorization without sharing a
database with your identity service.

Documentation
=============

Read the docs: http://corrobo.readthedocs.org/en/latest/

Expanded Getting Started at http://corrobo.readthedocs.org/en/latest/corrobo.html.


Contribute
==========
Submit any issues or questions here: https://github.com/johnwlockwood/corrobo/issues.

Looking for people who:
 * Would like to learn about this kind of system.
 * Know about how to defend against security attacks.
 * Know about different second factor authentication techniques.
 * Want to make their Internet of Things things communicate securely.
 * Like distributed systems.
 * Like to paint rocks.
 * Like to organize their closets.


Make pull requests to **development** branch of
 https://github.com/johnwlockwood/corrobo.

**Documentation** is written in reStructuredText and currently uses the
 Sphinx style for field
 lists http://sphinx-doc.org/domains.html#info-field-lists

Check out closed pull requests to see the flow of development, as almost
every change to master is done via a pull request on **GitHub**. Code Reviews
are welcome, even on merged Pull Requests. Feel free to ask questions about
the code.


