<?php

$data = "sistemkeamanandata";
$method = "DES-EDE3";
$key = "1234567810";
$options = 0;

// transform the key from hex to string
$key = pack("H*", $key);

// encrypt
$enc = openssl_encrypt($data, $method, $key, $options);
// decrypt
$dec = openssl_decrypt($enc, $method, $key, $options);

echo "plain: ".$data." encrypted: ".$enc." decrypted: ".$dec;
?>