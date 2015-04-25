Corrobo - How do I authentication with micro-services?
======================================================

Require a way to authentcate requests from one server to another.

Require a way for users to make requests to different services while
only logging in once, ie. Single-sign-on.

A few pieces are needed:

An IAM (Identity Access Management) service.
+++++++++++++++++++++++++++++++++++++++++++++++++++

Establish and manage user credentials.

Once signed in, respond to the user with an access token.

The access token should be sent with requests to your services.

There is a way for your service to trust the access token and know who
it is responding to and that they have authorization without sharing a
database with your identity service.

