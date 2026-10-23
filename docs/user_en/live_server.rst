.. raw:: latex

    \clearpage


.. _ooresults_live_server:

Publishing results via an ooresults live server
-----------------------------------------------


Concept
^^^^^^^

An ooresults-server can be used as a live server. Its event data
is then updated regularly from an external source (e.g. another ooresults-server).
The external source sends the data as "IOF 3.0 Interface Standard ResultList".


.. warning::

   It is also possible to publish the results of an event directly via the ooresults-server
   that is used to manage the event.
   This can be sufficient for a local WLAN. For publication on the Internet a second ooresults-server
   should be used for reasons of stability and security.


.. _configuration_live_server:

Configuration of the ooresults live server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.  In the configuration the parameter "import_stream" has to be set to "on", see also :ref:`configuration`.

#.  An event has to be created whose results are to be published and updated by the ooresults event server.
    The following parameters have to be set for this event:

    - Publish

      To publish the result data of the event,
      the parameter "Publish" of this event has to be set to true.

    - Key

      Definition of a key. The key has to be specified when the connection to the ooresults-server is established
      in order to define the event for which the received data is intended.


.. _configuration_events_server:

Configuration of the ooresults event server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.  The following parameters have to be set on the ooresults-server from which data of an event is to be sent
    to the ooresults live server:

    - Streaming address

      Address of the ooresults live server including the port but without the protocol,
      e.g. "server.com:8081".


    - Streaming key

      Key of the event on the ooresults live server for which the sent results are intended.


    - Streaming enabled

      Data is only sent to the ooresults live server if the parameters "Streaming address"
      and "Streaming key" are defined and "Streaming enabled" is switched on.
