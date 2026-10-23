.. raw:: latex

    \clearpage


.. _rental_cards:

Rental SPORTident cards
-----------------------

To make it easier to manage rented SPORTident cards,
rental cards can be recorded in a file rental_cards.txt.
The file is searched for in the subdirectory .ooresults of the user's home directory
and contains one SPORTident card number per line.

.. code-block::

   219402
   219403
   219412


If the number of a SPORTident card used by a participant is contained in this file,
it is displayed as "RC (...)" in the corresponding columns of the tables of the "Entries" and "SI Reader" tabs
(RC = rental card).

.. image:: ../user/images/rental_card_1_edited.png

.. warning::

   The file rental_cards.txt is read only once while the ooresults-server is starting.
   If the changed data is to be used after a change of the file,
   the ooresults-server has to be stopped and restarted.

