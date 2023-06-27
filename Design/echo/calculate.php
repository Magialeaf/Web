<?php 
if(isset($_POST['content'])){
    $content = $_POST['content'];
    echo json_encode(array("content" => $content));
}else{
    echo json_encode(array());
}
?>