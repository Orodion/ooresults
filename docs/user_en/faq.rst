Frequently asked questions
--------------------------

**At two events of an event series the name of a female competitor was spelled differently.**
**In the overall result she appears several times and the individual results are**
**not combined into one overall result. What can be done?**

   If a female competitor was entered in event A as e.g. Annalena Baerbock and in event B
   as Anna-Lena Baerbock, these are two different competitors for ooresults,
   and two competitors are listed in the overall result.

   If Annalena Baerbock is the correct name of the competitor, the two competitors can be merged
   in the "Competitors" tab with "Merge competitors ...", see :ref:`merge_competitors`.
   Anna-Lena Baerbock is then deleted and replaced by Annalena Baerbock in all events.
   The overall result now contains only the competitor Annalena Baerbock.

   Alternatively, the competitor Annalena Baerbock can be added in event B. Then,
   in event B the result has to be removed from the competitor Anna-Lena Baerbock and added to the
   competitor Annalena Baerbock. After that the competitor Anna-Lena Baerbock can be deleted
   in event B (and in the Competitors list).

|

**How can the data be backed up?**

   All data is stored in the sqlite database file ooresults.sqlite
   in the subdirectory .ooresults of the user's home directory.

   After the ooresults-server has been stopped, the file can be copied and stored e.g. on a USB stick.
   It can also be used as a database file on other computers with an
   ooresults installation.
