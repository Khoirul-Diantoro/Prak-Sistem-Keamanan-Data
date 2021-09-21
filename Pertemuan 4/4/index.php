<<?php
session_start();
error_reporting(0);
$encrypt = $_SESSION['encrypt'];
$decrypt = $_SESSION['decrypt'];

// inisialisasi variabel
$key = "";
$code = "";
$error = "";
$valid = true;
$color = "#FF0000";

// if form was submit
if ($_SERVER['REQUEST_METHOD'] == "POST")
{
	// declare encrypt and decrypt funtions
	require_once('enkripsi.php');
	
	// set the variables
	
	$code = $_POST['code'];
	
	
	// inputs valid
	if ($valid)
	{
		// jika menekan tombol enkripsi
		if (isset($_POST['encrypt']))
		{
			$code = encrypt($key, $code);
			
		}
			
		// jika menekan tombol dekripsi
		if (isset($_POST['decrypt']))
		{
			$code = decrypt($key, $code);
			
		}
	}
}

?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Enkripsi</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

<div class="con">
	<form action="index.php" method="post" class="from">
		<fieldset style="width: 50%; height: 50%;">
				<ul>
					<li> <input type="text" name="code" id="masukkan" placeholder="Masukan Data..." style="text-align: center" value="<?php echo htmlspecialchars($key); ?>"></li>
					<li ><input type="submit" name="encrypt" value="Enkripsi" /></li>
					<li><input type="submit" name="decrypt" value="Deskripsi"/></li>
					<li><a style="" href="hapus.php">Clear</a></li>
					<li >
						 <h2>Hasil    : <?php echo htmlspecialchars($code); ?></h2>
		 				 
					</li>
				</ul>

		</fieldset>
	</form>
</div>

</body>
</html>

