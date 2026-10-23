Getting started
===============

.. only:: html

   .. contents::
      :depth: 2


Overview
--------

ooresults (open orienteering results) is a software for recording and evaluating
the results of smaller orienteering events and is able to read SPORTident cards.

Here, "open" stands for "Open Source" on the one hand and for "Open Architecture" on the other.
ooresults is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, version 3.

ooresults consists of two programs:

1. **ooresults-server**

   ooresults-server is a web server for managing and storing data. It uses the TCP ports 8080 and 8081.

#. **ooresults-reader**

   ooresults-reader reads the data of an SI card with the help of a connected SPORTident readout station
   and sends the data to the ooresults-server.

It is operated with a current web browser (Chrome, Firefox, Edge, ...).

ooresults was successfully used to compute the results of the SILVA O-Night 2023 in Munich.
It has the following features:

- Multi-user capable
- Reading of SPORTident cards
- Installation is only necessary on the server and on computers with a connected SPORTident readout station,
  other computers only need a current web browser
- Supports visiting controls in a prescribed or in any order
- Supports score competitions
- Calculation of an overall result from several events
- Import of the competitor lists of an event from OrienteeringOnline.net via OE2003 CSV export
- Import of the competitor lists of an event in IOF 3.0 XML format
- Import of course data in IOF 3.0 XML format (e.g. PurplePen)
- Export of results in IOF 3.0 XML format
- Creation of result lists as PDF files


.. index:: Installation

Installation
------------

ooresults requires at least Python 3.10.
The following command installs the latest version of ooresults and its dependencies from the Python Package Index:

.. code-block::

   python -m pip install ooresults

It is recommended to install ooresults in a virtual environment (venv).


.. index:: ooresults-server; Start

.. _start_server:

Starting the ooresults-server
-----------------------------

The ooresults-server is started with the following command:

.. code-block::

   python -m ooresults.server

The ooresults-server creates a subdirectory .ooresults in the home directory of the user
if this directory does not yet exist.
It contains an sqlite database and configuration files.

Alternatively, the server can also be started directly with the ooresults-server program
located in the scripts directory of the Python installation.

For easy use, a desktop icon with a shortcut to this program can be created.

.. warning::

   For security reasons it is recommended to change the password of the admin user after the first start
   of the ooresults-server, see chapter :ref:`user_management`.

All data is stored in the sqlite database file ooresults.sqlite in the subdirectory .ooresults
of the user's home directory.

By copying this file the data can be backed up or transferred to another computer.


.. index:: ooresults-reader; Start

Starting the ooresults-reader
-----------------------------

The ooresults-reader is started with the following command:

.. code-block::

   python -m ooresults.reader

Alternatively, the reader can also be started directly with the ooresults-reader program
located in the scripts directory of the Python installation.

For easy use, a desktop icon with a shortcut to this program can be created.

.. warning::

   The ooresults-reader uses the "extended" protocol to read the SI cards.

   If the SPORTident readout station is disconnected from the computer before the ooresults-reader is closed,
   the readout station is not reset to the originally configured protocol,
   and other software products such as OE2003 cannot access the readout station.
   With the help of the set-legacy-mode program the readout station can be set back
   to the "legacy" protocol:

   .. code-block::

      python -m ooresults.set_legacy_mode


Starting the user interface
---------------------------

The program is operated with a current web browser by opening the page "https://localhost:8080".

If self-created certificates are used to start the https server,
the accesses to "https://localhost:8080" **and** "https://localhost:8081"
must be confirmed as exceptions in the web browser:

.. image:: ../user/images/unsave_1_edited.png

.. image:: ../user/images/unsave_2_edited.png
