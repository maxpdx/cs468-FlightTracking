<?php
// http://web.cecs.pdx.edu/~lmaksim/join.php
ini_set('display_errors',1);
ini_set('display_startup_errors',1);
error_reporting(-1);

include "connectPGDB.php";

$query = "SELECT * FROM Reserves R1, Sailors S1 WHERE R1.sid=S1.sid";
$Rquery = "SELECT * FROM Reserves";
$Squery = "SELECT * FROM Sailors";

$result = pg_query($connection, $query) or die("Query error: " . pg_last_error());
$Rresult = pg_query($connection, $Rquery) or die("R Query error: " . pg_last_error());
$Sresult = pg_query($connection, $Squery) or die("S Query error: " . pg_last_error());

$Rrows = array();
$Srows = array();

echo "<table border='1' cellpadding='15'><tr><td>";
echo "Wanted Result: <strong>" . pg_num_rows($result) . " rows</strong><br/>";
while($row = pg_fetch_row($result))
{
        foreach($row as $element)
                echo $element . " | ";
        echo "<br/>";
}

echo "</td><td>";

echo "Reserves: <strong>" . pg_num_rows($Rresult) . " rows</strong><br/>";
while($row = pg_fetch_row($Rresult))
{
        $Rrows[] = $row;
        foreach($row as $element)
                echo $element . " | ";
        echo "<br/>";
}

echo "</td><td>";

echo "Sailors: <strong>" . pg_num_rows($Sresult) . " rows</strong><br/>";
while($row = pg_fetch_row($Sresult))
{
        $Srows[] = $row;
        foreach($row as $element)
                echo $element . " | ";
        echo "<br/>";
}
echo "<br/>";

echo "</td></tr></table>";

foreach($Rrows as $rrow)
{
        foreach($rrow as $i => $r)
        {
                echo $r . " | ";
        }

        foreach($Srows as $srow)
        {
                if($rrow[0] == $srow[0])
                        foreach($srow as $j => $s)
                        {
                                if($j != 0)
                                        echo $s . " | ";
                        }
        }
        echo "<br />";
}

pg_close($connection);