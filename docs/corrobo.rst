Getting Started with Corrobo
================================

How to do server-to-server authentication?

Build an authentication provider service which provides authorization tokens.

Build multiple services that need to talk to each other with verified
authorization.

Build a front end where users need to talk to services in with
verified authorization.


Build an authentication provider
++++++++++++++++++++++++++++++++

Make an Identity Access Management (IAM) web service that manages users.
    * Create user
    * Update user
    * Password reset
    * Takes credentials and verifies them to a user id.
    * Maybe add  a second factor of authentication.
        * Google: implement multi-factor authentication
        * check out these un-vetted and not-endorsed by me services such as:
            * https://www.duosecurity.com/product/services/api.
            * http://www.smspasscode.com/
        * Use Twilio https://www.twilio.com/docs/howto/two-factor-authentication.



With Corrobo add:
    * from a user id make a token to return to the user.
    * take unexpired token and return a new token.


If the client asks for a new token with an unexpired one, they can avoid giving their credentials again.


Encrypted the Data in Transit
+++++++++++++++++++++++++++++

This is done with TLS (Transport Layer Security).
It requires that the server have a certificate signed by
a certificate authority. For non-public facing servers you
may become your own certificate authority so you can sign
your own cryptographic keys. This allows the encrypted
connection to be authenticated and therefore trusted.
