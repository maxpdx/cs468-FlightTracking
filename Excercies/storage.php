<?php
ini_set('display_errors',1);
ini_set('display_startup_errors',1);
error_reporting(-1);

include "connectPGDB.php";

$table = "cars";
$query = "SELECT * FROM $table";
$result = pg_query($query);

$i = 0;
$columns = array();
while ($row = pg_fetch_row($result)) 
{
	$count = count($row);
	$y = 0;
	while ($y < $count)
	{
		$c = current($row);
		$columns[$y]['null'] = 0;
		$columns[$y]['unique'] = 0;
		if(empty($c))
			$columns[$y]['null'] = $columns[$y]['null'] + 1;
			
		next($row);
		$y = $y + 1;
	}
	$i = $i + 1;
}

echo 'Table: <strong>' . $table . '</strong><br/><br/>';
echo '<html><body><table border="1">';
echo '<tr><th>Field name</th><th>Type</th><th>Null</th><th>Unique</th></tr>';
$i = 0;
while ($i < pg_num_fields($result))
{
	
	$name = pg_field_name($result, $i);
	$type = pg_field_type($result, $i);
	$null = $columns[$i]['null'];
	$unique = $columns[$i]['unique'];
	
	echo '<tr>';
	echo '<td>' . $name . '</td>';
	echo '<td>' . $type . '</td>';
	echo '<td>' . $null . '</td>';
	echo '<td>' . $unique . '</td>';
	echo '</tr>';
	$i = $i + 1;
}

echo '</table></body></html>';
echo '<br/><strong>Rows: ' . pg_num_rows($result) . '</strong>';

pg_free_result($result);
pg_close($connection);