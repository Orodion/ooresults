Reference guide
===============

.. only:: html

   .. contents::
      :depth: 2


.. _events:

Events
------

Name

   Name of the event.


Date

   Date on which the event takes place, e.g. 2022-03-31.


Key

   Definition of a key. The key has to be specified when the connection to the ooresults-server is established
   in order to define the event for which the received data is intended. It is used both by an
   ooresults-reader to transmit the SI card data that has been read and by another ooresults-server
   to transmit live results.

   .. warning::

      The key does not only serve to assign the data to an event, but also as proof of the access authorization
      of the reading program. Only the reading program that knows the event key can store SI card data in the database.
      The key therefore has to be kept secret like a password and should comply with the usual password policies.


Publish

   If "Publish" is switched on, the results of the event
   can be read from the ooresults-server without specifying a password.

   Currently only the result data of one event can be published.
   If "Publish" is activated for several events, the event with the
   most recent date is used.


Streaming address

   Address of an ooresults-server to which result data of the event
   is to be transmitted as IOF Interface Standard 3.0 ResultList
   (with the port but without the protocol, e.g. "server.com:8081").


Streaming key

   Key of the event of an ooresults-server to which the result data is to be sent.


Streaming enabled

   Data is only sent to another ooresults-server if a "Streaming address" and a "Streaming key" are defined
   and "Streaming enabled" is switched on.


.. _entries:

Entries
-------

This collection contains the participants of an event.
A participant is uniquely identified by his or her first and last name.

If a participant is entered in an event and is not yet contained in the list :ref:`competitors`,
he or she is added there automatically with first and last name, gender and year of birth.

If the first or last name of a participant is corrected,
his or her first and last name is also changed accordingly in **all** other events
and in the collection :ref:`competitors`.
The same applies to a correction of gender or year of birth.

.. warning::

   If the gender or year of birth of a participant is corrected, the results of **all** events
   in which the participant took part in a class with handicap scoring are recalculated.


First name

   First name of the participant.


Last name

   Last name of the participant.


Sex

   Gender of the participant (F = female, M = male).


Year

   Year of birth of the participant (four digits), e.g. 1982 or 2008.


Chip

   Number of the SPORTident card that the participant wants to use / has used in the run.

   The number cannot be changed if the result read from a SPORTident card is assigned to the participant.


Club

   Club of the participant. To be able to assign a participant to a club,
   the club has to be entered in advance in the list :ref:`clubs`.


Class

   Class in which the participant starts.


NC (not competing)

   The participant starts out of competition, i.e. he or she is listed in the result lists with his or her running time,
   but the result is not taken into account when calculating the rankings.


Start

   Start time of the participant. If the class is run without punching a start control,
   this time is used as the start time of the participant.

   For a mass start no time should be entered here.
   If a start time is specified both here and for the class,
   the time specified here is used as the start time of the participant.


Status

   There are the following statuses:

   - **Started (started)**

     The runner has started but has not yet read out his or her SPORTident card.

   - **OK (ok)**:

     The runner has punched all controls (in the correct order).

   - **MP (mispunched)**:

     The runner has not punched at least one control correctly.

   - **DNS (did not start)**:

     The runner did not start.

     This status cannot be set if the result read from a SPORTident card is assigned to the participant.

   - **DNF (did not finish)**:

     The runner did not finish the run.
     Possible causes:

     1. The runner abandoned the run without punching "Finish",
     #. The runner punched "Finish", but the status was changed manually to DNF.

   - **OTL (over time limit)**:

     The runner exceeded the time limit of the event.

   - **DSQ (disqualified)**:

     The runner was disqualified.


Functions
~~~~~~~~~


Import ...
""""""""""


With "Import ..." the data of an event can be imported in the following formats:

- **IOF Interface Standard 3.0 Entry List**

  Imports the participant data of an EntryList in the IOF XML 3.0 format, see `IOF Data Standard 3.0 <https://orienteering.sport/iof/it/data-standard-3-0/>`_.

- **IOF Interface Standard 3.0 Result List**

  Imports the result data of a ResultList in the IOF XML 3.0 format, see `IOF Data Standard 3.0 <https://orienteering.sport/iof/it/data-standard-3-0/>`_.

- **OE2003 csv, OE12 csv**

  Imports the participant or result data in the SportSoftware OE2003 or OE12 CSV format.
  Can be used to take over participant data of an event from http://orienteeringonline.net.


.. warning::

   First name, last name and class of a participant are mandatory fields.
   If one of these fields is empty for any of the entries in the data to be imported, the data cannot be imported.

.. warning::

   If the data to be imported contains several entries with the same first and last name, only the first entry is imported,
   and a message is shown that not all data has been imported.


Export ...
""""""""""


With "Export ..." the data of an event can be exported in the following formats:

- **IOF Interface Standard 3.0 Entry List**

  Exports the participant data as EntryList in the IOF XML 3.0 format, see `IOF Data Standard 3.0 <https://orienteering.sport/iof/it/data-standard-3-0/>`_.

- **IOF Interface Standard 3.0 Result List**

  Exports the result data as ResultList in the IOF XML 3.0 format, see `IOF Data Standard 3.0 <https://orienteering.sport/iof/it/data-standard-3-0/>`_.

- **Result List for Splitsbrowser**

  Exports the result data as ResultList in the IOF XML 3.0 format, but uses the pure running times as the result.
  Time credits (e.g. when using a handicap factor) or penalty times are not taken into account.
  Should be used if time credits cause problems when importing into splits browser software
  such as `WinSplits <http://obasen.orientering.se/winsplits>`_.

- **OE2003 csv**

  Exports the participant or result data in the OE2003 CSV format
  so that it can be imported by the OE2003 SportSoftware.
  Does not contain split times.

- **OE12 csv**

  Exports the participant or result data in the OE12 CSV format
  so that it can be imported by the OE12 software.
  Does not contain split times.


.. _classes:

Classes
-------


Name

   Name of the class, e.g. "Damen A" or "Herren A".


Short name

   Currently not used.


Course

   Course used for this class. The course has to be defined beforehand in :ref:`Courses`.
   If no course is assigned to the class, no results are calculated.
   This can be used to import results of an event series.


Type

   Three competition types are available:

   - **Standard**:

     The controls have to be visited in the prescribed order. The runner with the fastest time who has punched all controls in the correct order wins.

   - **Net**:

     The controls may be visited in any order. The runner with the fastest time who has punched all controls wins.

   - **Score**:

     Score competition, i.e. there is one point for each control visited. The runner with the highest number of points wins.


Voided Legs

   Used with "Standard" to disregard the running time of the leg between
   two directly consecutive controls.
   The two control numbers are separated by a hyphen.
   Several legs can be specified separated by commas, e.g. "113-119, 112-114".


Use start control

   "If punched", "No" and "Yes" are available.

   - **If punched**:

     If a start control is used, its time is used as the start time, otherwise the start time of the runner specified in :ref:`entries`. If nothing is specified there, the mass start time specified in :ref:`classes` is used.

   - **No**:

     Even if a start control has been punched, it is not used as the start time. The start time of the runner specified in :ref:`entries` is always used, or, if nothing is specified there, the mass start time specified in :ref:`classes`.

   - **Yes**:

     The punch time of the start control is always used. If the start control was not punched, the run is invalid.


Apply handicap

   If "Yes", the total time (running time plus any penalty times) is multiplied by the handicap factor of the runner.
   The handicap factor of the runner depends on gender and age.


Mass start

   Time of the mass start, e.g. 18:30:00.


Time limit

   Used to define a time limit. The input is in minutes (e.g. "45:00" for 45 minutes).


Penalty controls

   For each missing control the specified penalty time (to be entered in seconds) is added to the running time.


Penalty time limit

   For each started minute by which the running time exceeds the time limit,
   the specified penalty time (to be entered in seconds) is added to the running time.


.. _courses:

Courses
-------


Name

   Name of the course, e.g. "Bahn A".


Length

   Length of the course in meters.


Climb

   Climb of the course in meters along the expected best route choice.


Controls

   Numbers of the controls (without start and finish) that make up the course.

   For the competition type "Standard" the controls have to be visited in the order specified here.
   For the competition types "Net" and "Score" the controls can be specified in any order.

   The controls are entered separated by hyphens.
   For better readability, spaces can be entered before and after the hyphen.
   Valid entries are e.g. "121-141-122-124" or "121 - 141 - 122 - 124".


.. _settings:

Settings
--------


Name

   Defines the heading used when printing.


Nr of best results

   Defines the maximum number of events that are to be used for a participant to calculate the
   overall result. If nothing is specified, all events
   are taken into account.


Mode

   Defines the calculation method. Currently only proportional is possible,
   i.e. the time of the winner is divided by the own time.


Maximum points

   In proportional mode: The winner receives maximum points, all others
   *MaximumPoints* * *(WinnerTime / OwnTime)*. Participants who are not ranked
   (status other than ok) receive 0 points.


Decimal places

   In proportional mode: The calculated number of points
   *MaximumPoints* * *(WinnerTime / OwnTime)* is rounded to the specified number
   of decimal places.


.. _competitors:

Competitors
-----------

This collection serves as an archive of all competitors.

A competitor can only be deleted from this collection if he or she is not entered as a participant
in any event. A competitor is uniquely identified by his or her first and last name,
i.e. there cannot be two competitors with the same first and last name.

If the first or last name of a competitor is corrected,
his or her first and last name is also changed accordingly in **all** events.
The same applies to a correction of gender or year of birth.

.. warning::

   If the gender or year of birth of a competitor is corrected, the results of **all** events
   in which the competitor took part in a class with handicap scoring are recalculated.


First name

   First name of the competitor.


Last name

   Last name of the competitor.


Sex

   Gender of the competitor (F = female, M = male).


Year

   Year of birth of the competitor (four digits), e.g. 1982 or 2008.


Chip

   Number of the SPORTident card that the competitor usually uses.


Club

   Club of the competitor. To be able to assign a competitor to a club,
   the club has to be entered in advance in the list :ref:`clubs`.


.. _clubs:

Clubs
-----


To be able to assign a participant or competitor in :ref:`entries` or :ref:`competitors` to a club,
the club has to be entered in this collection in advance.

If a participant of an event or a competitor is assigned to a club,
this club cannot be deleted.


Name

   Name of the club.
