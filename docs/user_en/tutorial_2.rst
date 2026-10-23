Tutorial - Part 2
=================

.. only:: html

   .. contents::
      :depth: 2


Reading the SI cards
--------------------

The SI cards are read with the SPORTident readout station using the program ooresults-reader.
It can be started on the same computer as the ooresults-server or on any other computer.

At startup the ooresults-reader reads a key from a configuration file
and sends it to the ooresults-server together with the data read from the SI card.
The ooresults-server assigns the data to the event whose key matches the received key
(or discards the data if this key has not been specified for any event).

.. warning::

   The key does not only serve to assign the data to an event, but also as proof of the access authorization
   of the reading program. Only the reading program that knows the event key can store SI card data in the database.
   The key therefore has to be kept secret like a password and should comply with the usual password policies.

As the key has to be handled like a password, it is displayed as \*\*\* in the Events table. To read the key,
call the Edit function of the event.

.. image:: ../user/images/event_3_edited.png

For security reasons a key should only be specified for the event that is currently being held.
After the end of the event the key should be deleted and a different key should be used for the next event.

If the ooresults-server and the ooresults-reader run on the same computer **and** the computer is not connected to a network,
a simple key such as "local" can also be used.

.. warning::

   The ooresults-reader uses the "extended" protocol to read the SI cards.

   If the SPORTident readout station is disconnected from the computer before the ooresults-reader is closed,
   the readout station is not reset to the originally configured protocol,
   and other software products such as OE2003 cannot access the readout station.
   With the help of the set-legacy-mode program the readout station can be set back
   to the "legacy" protocol.


Displaying the SI card data that has been read
----------------------------------------------

1. Click the "SI Reader" tab

All SI cards read for the selected event since the server was started are displayed.

.. note::

   The "SI Reader" tab can only be opened if an event with a key is selected.

When an SI card is read, it is automatically checked whether the SI card number that has been read can be unambiguously assigned
to a competitor registered for the event in question.

If this is the case, the result is stored for the competitor and
the running time is displayed together with the competitor's name on a
green background for a successful run (status OK) or on a red background for a mispunch (status MP or DNF).

If the SI card that has been read cannot be unambiguously assigned to a competitor, or if another result has already been
assigned to the competitor, no competitor name is displayed, and instead of the running time and the status a reason is shown
why no assignment to a competitor is possible. The entry is shown on a yellow background.

.. image:: ../user/images/sireader_1.png

In the following cases the SI card cannot be assigned to a competitor:

- No competitor with this SI card exists
- Exactly one competitor with this SI card exists, but a (different) result has already been assigned to the competitor
- Several competitors with this SI card exist

If an SI card is read several times but with the same records (i.e. **no** further control was punched
after the first readout), no new entry is created in the "Entries" list.

At the end of the page the status of the readout station is displayed:

.. image:: ../user/images/sireader_2_edited.png

The meanings are:

- Offline

  The web page has no connection to the ooresults-server.

- Card reader status: Offline

  No connection has been established yet to an ooresults-reader
  that uses the key of the event.

- Card reader status: Disconnected

  A connection has been established to an ooresults-reader
  that uses the same event key.
  However, no SPORTident readout station is connected yet,
  or the SPORTident readout station was not detected by the ooresults-reader.

- Card reader status: Connected

  A connection has been established to an ooresults-reader
  that uses the same event key,
  and a SPORTident readout station is connected and ready for operation.

.. note::

   After a restart of the server the table of the "SI Reader" tab is empty.

If the SI card that has been read cannot be assigned to a competitor, the result is displayed as a new entry (without a competitor name)
on the page "Entries":

.. image:: ../user/images/entries_1_edited.png

.. note::

   In contrast to the "SI Reader" list, the "Entries" list is not updated automatically when an SI card is read,
   but only after the "Reload" function is called (or when switching from another tab).



Manually assigning an SI card that has been read to a competitor
----------------------------------------------------------------

If an SI card that has been read cannot be assigned automatically to a competitor,
the result has to be assigned manually to a competitor.

1. Click the "Entries" tab
#. Select the competitor to whom the result is to be assigned.
   The list can be reduced with the help of the filter function.
#. Click the function "Edit entry ..."
#. Open the Result list and select one of the unassignable SI card entries
#. Confirm with "Save"

.. image:: ../user/images/entries_2_edited.png

If no result has been assigned to the competitor yet, the SI card entry is deleted from the "Entries" list.

If a result has already been assigned to the competitor, the existing result is stored as a new unassignable result
in the "Entries" list. This is done in order to be able to handle the scenario "two competitors have swapped their SI cards".

.. warning::

   If the competitor is not yet registered for the run, he or she has to be created first,
   see chapter :ref:`add_entry`.


Manually removing a result assigned to a competitor
---------------------------------------------------

Sometimes it may be necessary to remove a result assigned to a competitor from this competitor again.
The result is then stored as an unassignable result in the "Entries" list.

1. Select the competitor in the "Entries" list.
   The list can be reduced with the help of the filter function.
#. Click the function "Edit entry ..."
#. Open the Result list and select "Remove result"
#. Confirm with "Save"

.. image:: ../user/images/entries_3_edited.png

Unassignable result entries that are no longer needed can be deleted from the "Entries" list
with the function "Delete entry".

.. note::

   The entry "Remove result" is only displayed if a result is assigned to the competitor.


Changing the status of a competitor
-----------------------------------

This is done with the function "Edit entry ...".

1. Select the competitor in the "Entries" list.
   The list can be reduced with the help of the filter function.
#. Click the function "Edit entry ..."
#. Open the Status list and select a status
#. Confirm with "Save"

.. image:: ../user/images/entries_4_edited.png

.. seealso::

   A description of the possible statuses can be found in chapter :ref:`entries`.


Displaying and editing the results of a competitor
--------------------------------------------------

1. Select the competitor in the "Entries" list.
   The list can be reduced with the help of the filter function.
#. Click the function "Edit split times ..."

.. image:: ../user/images/entries_result_1.png

If a control station does not work and is not contained on the competitor's SI card
despite proper punching, proceed as follows:

1. Click the function "Edit" at the end of the row of the control in question
#. Enter the punch time (if it is not known, leave the field empty)
#. Confirm with "Save"

.. image:: ../user/images/entries_result_2.png

The time displayed in the column "Used time" is used for the result calculation.
Rows that have been edited, i.e. in which the time read from the SI card (column "Card time")
differs from the time used (column "Used time"), are displayed with a grey background.

.. image:: ../user/images/entries_result_3_edited.png


Using the self-service readout window
-------------------------------------

The ooresults software is designed for self-service readout of the SI card by a competitor,
i.e. the competitor inserts his or her SI card into the SPORTident readout station and gets
the result displayed on an (additional) screen (a smartphone is also suitable for this).

If the SI card cannot be assigned to a competitor, a message appears asking the competitor to contact the event center.
There the result can then be assigned to a competitor.

If the displayed name does not correspond to the name of the competitor (e.g. because two competitors have swapped their SI cards),
the competitor also contacts the event center for correction.

1. Open a web browser window
#. Open the page https://localhost:8080/si1

.. image:: ../user/images/si1_1_edited.png

.. note::

   If several events have a key,
   the first event with a key in the "Events" list is used.


.. _demo_cardreader:

Demo card reader
----------------

If the ooresults-server is started in a demo mode, the reading of SI cards can be simulated with a
demo card reader.

1. Open a web browser window
#. Open the page https://localhost:8080/demo
#. Enter the event key
#. Enter the controls and punch times
#. Enter the SI card number
#. Send the result to the ooresults-server by pressing "Insert card"

.. image:: ../user/images/demo_1_edited.png

.. note::

   - Only rows with a control number **and** a punch time are used.

   - The demo reader automatically adds the date of the event as the date.

   - As the ooresults-reader reads the key only at program start, the web page should be reloaded
     before the key is changed.
