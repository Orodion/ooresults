Häufige Fragen
--------------

**Bei zwei Wettkämpfen einer Wettkampfserie wurde der Name einer Läuferin unterschiedlich**
**geschrieben. Im Gesamtergebnis erscheint die Läuferin mehrfach und die Einzelergebnisse sind**
**nicht zu einem Gesamtergebnis zusammengefasst. Was ist zu tun?**

   Wurde eine Läuferin in einem Wettkampf A z.B. als Annalena Baerbock und in einem Wettkampf B
   als Anna-Lena Baerbock eingetragen, so sind dies für ooresults zwei verschiedene Läuferinnen,
   und es werden im Gesamtergebnis zwei Läuferinnen gelistet.
   
   Ist Annalena Baerbock der korrekte Name der Läuferin, können die beiden Läuferinnen im Registerblatt
   "Competitors" mit "Merge competitors ..." zusammengeführt werden, siehe :ref:`merge_competitors`.
   Dabei wird Anna-Lena Baerbock gelöscht und bei allen Wettkämpfen durch Annalena Baerbock ersetzt.
   Im Gesamtergebnis gibt es jetzt nur noch die Läuferin Annalena Baerbock.

   Alternativ kann die Läuferin Annalena Baerbock im Wettkampf B hinzugefügt werden. Anschliessend
   ist im Wettkampf B das Ergebnis von der Läuferin Anna-Lena Baerbock zu entfernen und zur
   Läuferin Annalena Baerbock hinzuzufügen. Danach kann im Wettkampf B (und in der Competitors-Liste)
   die Läuferin Anna-Lena Baerbock gelöscht werden.

|

**Wie kann ein Backup der Daten durchgeführt werden?**

   Sämtliche Daten werden in der sqlite Datenbank-Datei ooresults.sqlite
   im Unterverzeichnis .ooresults des Heimverzeichnis des Benutzers gespeichert.
   
   Nach Beenden des ooresults-server kann die Datei kopiert und z.B. auf einem USB-Stick gespeichert
   werden. Ebenso kann sie als Datenbankdatei auf anderen Rechnern mit einer
   ooresults Installation verwendet werden.


