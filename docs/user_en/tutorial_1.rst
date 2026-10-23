Tutorial - Part 1
=================

.. only:: html

   .. contents::
      :depth: 2


Logging in
----------

.. note::

   In the following it is assumed that the web browser is started on the same computer
   on which the ooresults-server is running (for starting the ooresults-server see chapter :ref:`start_server`).

   If this is not the case (the ooresults-server is running on another computer),
   another address instead of https://localhost:8080 and possibly
   also another user name and password have to be used.

1. Start the ooresults-server
#. Start a current web browser (Firefox, Chrome, ...)
#. Open the page https://localhost:8080
#. Click the link Administration
#. Enter the user name and password

.. image:: ../user/images/login_1_edited.png

.. image:: ../user/images/login_2.png

If the user name and password are entered correctly, the events that have already been created
are displayed in descending chronological order.

.. image:: ../user/images/login_3.png

The event data is displayed and changed via several tabs:

- Events
- Entries (participants)
- Classes
- Courses
- Results
- Competitors
- Clubs
- Series
- SI Reader (SI cards that have been read)

The data of the tabs Events, Competitors, Clubs and Series is independent of the event
and applies to all events.

The data of the tabs Classes, Courses, Results and SI Reader depends on the event.
These tabs can only be accessed if an event has previously been selected in the Events tab.
The displayed data then refers to this event.

.. note::

   Adding, changing or deleting a record of a tab is done by clicking one of the tool buttons.
   Some functions are only available after a record has been selected.
   The currently selected record is displayed with a red background.

   A double click on a record directly opens the window for editing the record.

.. image:: ../user/images/login_4_edited.png


Creating an event
-----------------

1. Click the "Events" tab
#. Click the function "Add event ..."
#. Enter the event data and confirm with "OK". Name and date are mandatory.

.. image:: ../user/images/event_1_edited.png

.. image:: ../user/images/event_2.png

.. note::

   **For most of the further steps an event has to be selected first
   (click the Events tab and click the event in question;
   the selected event is then displayed with a red background).**


Importing entries
-----------------

1. Export the entry data in http://orienteeringonline.net/ in the OE2003 format.

   1. Open http://orienteeringonline.net
   #. Log in
   #. Switch to the event page
   #. Switch to the Control Panel tab
   #. Select Export to OE2003
   #. Click the Export button
   #. Save the file, e.g. as Export_OONet.txt

.. image:: ../user/images/import_entries_1_edited.png

2. Click the "Events" tab
3. Select the event "1. O-Cup 2023 (Westpark)" (by clicking it)

.. image:: ../user/images/import_entries_2_edited.png

4. Click the "Entries" tab
5. Click the function "Import ..."

.. image:: ../user/images/import_entries_3_edited.png

6. Select "OE2003"
7. Select the file exported in step 1
8. Confirm with "Import"

.. image:: ../user/images/import_entries_4_edited.png

The imported entries are now displayed:

.. image:: ../user/images/import_entries_5.png

Clubs and competitors that do not yet exist are created automatically and displayed under "Competitors" and "Clubs".
Classes that do not yet exist are also created automatically.

.. warning::

   The OrienteeringOnline export does not contain the gender of the participants. As it is needed for the handicap calculation,
   it has to be added afterwards by editing the entries.

   If the competitor is already contained in the "Competitors" tab
   (e.g. through participation in an earlier event), the gender is taken over automatically from there during the import.

.. warning::

   For the OE2003 export from OrienteeringOnline special rights are required in OrienteeringOnline.

By selecting a view the entries can be displayed in groups (e.g. separated by class):

.. image:: ../user/images/import_entries_6_edited.png

Creating the courses
--------------------

1. Click the "Courses" tab
#. Click the function "Add course ..."
#. Enter the course data. At least the name and the numbers of the controls have to be filled in.
#. Click "Save"

.. image:: ../user/images/course_1.png

The controls are entered separated by hyphens.
For better readability, spaces can be entered before and after the hyphen.

For the tutorial events a course with the controls "121-124-122-123" is required:

.. image:: ../user/images/course_2.png

.. note::

   Instead of entering the course data manually, the course data can also be imported with the function "Import ...".
   The course data has to be available in the format IOF XML 3.0 CourseData.


Creating the classes
--------------------

The classes created automatically when importing the entry data from orienteeringonline.net
still have to be completed with further data.

1. Click the "Classes" tab
#. Select the class to be edited
#. Click the function "Edit class ..."
#. Enter the missing class data
#. Click "Save"

.. image:: ../user/images/class_1_edited.png

.. image:: ../user/images/class_2.png

.. warning::

   The names Organizer and Organizers cannot be used as event classes.
   Participants assigned to these classes receive an organizer bonus in series.
   These classes are not listed in start lists and result lists.

The following classes are used for the tutorial events:

.. image:: ../user/images/class_3.png

.. seealso::

   A description of the data fields can be found in chapter :ref:`classes`.


.. _add_entry:

Creating entries manually
-------------------------

1. Click the "Entries" tab
#. Click the function "Add entry ..."
#. Enter the entry data. First and last name and class are mandatory.
#. Confirm with "Save"

.. image:: ../user/images/competitor_1_edited.png

.. warning::

   If the club or the class is not contained in the selection list,
   it has to be created **beforehand** via the pages "Clubs" or "Classes".

If the competitor does not yet exist in the "Competitors" list, he or she is added there automatically.

If the competitor already exists in the "Competitors" list
(e.g. because he or she has already taken part in an earlier run),
the button "Competitors ..." (to the right of the field "First name") can be pressed.

A window with the Competitors list opens.
By clicking and pressing "Save" the data can be transferred directly into the "Add entry ..." form.
The Competitors list can be reduced by filtering (input field "Filter ...").


Editing and deleting entries
----------------------------

The edit function is mainly needed to add or change SI card numbers and to change the status
(e.g. to set the status DNS for participants who did not start).

1. Click the "Entries" tab
2. Select the desired entry in the table.
   The row is then displayed with a red background.
   By using the filter (input field "Filter (ALT+F) ...") the list can be reduced.

   .. note::

      Pressing the key combination "ALT+F" sets the input focus to the filter and clears its content.
      The year of birth is particularly suitable as a filter criterion.

.. image:: ../user/images/competitor_2_edited.png

3. Click the function "Edit entry ..." or "Delete entry ...
4. For "Edit entry ...": change the entry data
5. Confirm with "Save" or "Delete"

.. warning::

   First name, last name, gender and year of birth are unchangeable properties of a participant. If they are changed,
   they are changed in **all** events (including those that have already finished). When the handicap factor is used,
   this can lead to a change of the ranking.
