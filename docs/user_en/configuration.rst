Configuration and user management
=================================

.. only:: html

   .. contents::
      :depth: 2


.. _configuration:

Configuration
-------------

ooresults is configured via the file config.ini.
It is searched for in the subdirectory .ooresults of the user's home directory.
If no such file exists, it is created with the following content:

.. code-block::

   [Server]
   ssl_cert =
   ssl_key =
   demo_reader = off
   import_stream = off

   [Cardreader]
   host = 127.0.0.1
   ssl_verify = false
   serial_number =
   key = local


The ooresults-server uses the section [Server],
the ooresults-reader the section [Cardreader].

The entries mean:

.. index:: ooresults-server; Configuration

[Server]ssl_cert and [Server]ssl_key

   The entries ssl_cert and ssl_key refer to the certificates required
   for the https server. If the entries are missing or empty,
   the files cert.pem and privkey.pem from the subdirectory
   .ooresults/cert of the user's home directory are used;
   if they do not exist, self-signed files are created.


[Server]demo_reader

   If the entry demo_reader is on, a page can be opened at the address https://localhost:8080/demo
   with which the reading of an SI card can be simulated,
   see section :ref:`demo_cardreader`.

   .. note::

      For security reasons demo_reader should be set to "on" only for getting to know the software
      and otherwise to "off".


[Server]import_stream

   If the entry import_stream is "on", IOF Interface Standard 3.0 ResultList data can be received
   at the address "wss://<server>:8081/import". This is necessary e.g.
   if the ooresults-server is to be used for publishing live results,
   see section :ref:`ooresults_live_server`.

   .. note::

      For security reasons import_stream should only be set to "on"
      if result data is to be received via the streaming interface.


.. index:: ooresults-reader; Configuration

[Cardreader]host

   IP address or name under which the ooresults-server can be reached.

   .. note::

      On Windows computers 127.0.0.1 should always be used instead of localhost,
      because Windows prioritizes the IPv6 protocol and the ooresults-server may then
      not be reachable.


[Cardreader]ssl_verify

   If false, the ooresults-server is not verified.
   Should be set to false for self-created certificates, otherwise to true.


[Cardreader]serial_number

   If several readout stations are connected to one computer, the one to be used can be selected
   by specifying the serial number of the SPORTident readout station.
   The serial number is located on the back of the SPORTident readout station.

   If only one readout station is connected, the entry should remain empty.


[Cardreader]key

   Key to assign the ooresults-reader to an event.

   .. warning::

      The key also serves as proof of authorization. Anyone who knows the key can store data
      in the assigned event on the ooresults-server.


.. _user_management:

User management
---------------

The user management for logging in to ooresults is done via the file users.json.
It is searched for in the subdirectory .ooresults of the user's home directory
and contains the user names and passwords.

If no such file exists, it is created with the following content:

.. code-block::

   [
       {
           "username": "admin",
           "password": "admin"
       }
   ]

.. warning::

   For security reasons it is recommended to change the password.

Changing user names and passwords, creating new users or deleting
users is done by editing the file directly.
For example, the following file contains the three user names Scholz, Habeck and Lindner:

.. code-block::

   [
       {
           "username": "Scholz",
           "password": "Ka_1_lbsbraten"
       },
       {
           "username": "Habeck",
           "password": "Sc_2_hweinebraten"
       },
       {
           "username": "Lindner",
           "password": "Hirsch$Gulasch"
       }
   ]

.. note::

   Changes to users.json only take effect after a restart of the ooresults-server.

.. warning::

   The ooresults-server can only be started with an existing users.json with correct
   content. It is checked against the following JSON schema:

   .. code-block::

      {
          'type': 'array',
          'items': {
              'type': 'object',
              'properties': {
                  'username': {'type': 'string'},
                  'password': {'type': 'string'},
              },
              'required': ['username', 'password'],
              'additionalProperties': False,
          }
      }
