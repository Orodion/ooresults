Tutorial - Part 3
=================

.. only:: html

   .. contents::
      :depth: 2


Displaying the results
----------------------

1. Click the "Results" tab

With the functions "Print results ..." and "Print split times ... " PDF files
with the results or split times can be created.

.. image:: ../user/images/results_1_edited.png

.. note::

   The results can be exported in various formats (including IOF XML 3.0 ResultList)
   with the function "Export ..." in the "Entries" tab.


Calculating and displaying the overall result
---------------------------------------------

Events with an entry in the field "Series" are combined into an overall result.
The overall result is displayed in the "Series" tab; the events are sorted by date
and the texts given in the field "Series" are used as headings.

.. image:: ../user/images/series_1_edited.png

.. image:: ../user/images/series_2_edited.png

.. note::

   Currently only one overall result can be calculated per database.

The calculation of the overall result is defined in the "Settings" dialog. The "Settings" dialog is opened with
the function "Settings ...".

.. image:: ../user/images/settings_1.png

.. seealso::

   A description of the fields can be found in chapter :ref:`settings`.


Merging competitors
-------------------

Competitors are identified by their first and last name. If e.g. "Annalena Baerbock"
was added as "Annalena Bärbock" in another event of the series, the results
of "Annalena Baerbock" and "Annalena Bärbock" are not combined in the overall result
but are displayed as the results of two different competitors.

With the function "Merge competitors ..." in the "Competitors" tab
different spellings of a person can be cleaned up. When merging
the competitors "Annalena Bärbock" and "Annalena Baerbock" into "Annalena Baerbock",
the name "Annalena Bärbock" is replaced by "Annalena Baerbock" in all events
and afterwards "Annalena Bärbock" is deleted from the Competitors list.

.. warning::

   If "Annalena Bärbock" and "Annalena Baerbock" have a different gender or year of birth,
   not only the name but also the gender and year of birth are changed in all events.


Organizer bonus
---------------

Competitors who are assigned to the class "Organizer" or "Organizers" in an event
receive an organizer bonus for this event. It amounts to 50% of the points result
if they take part in one run; otherwise it is the average of the two best points results.

.. image:: ../user/images/series_3_edited.png

.. image:: ../user/images/series_4_edited.png

.. warning::

   The classes "Organizer" and "Organizers" do not appear in start lists and result lists
   and can therefore not be used as event classes.
