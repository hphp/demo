<?php
function agent($line)
{
    //1. 函数体前面部分填写所有需要在统计中使用的变量（不管是否能够匹配出变量值）
   $res['_OriginalLogLine'] = $line;
   $res['_Type'] = null;
   $res['_Appid'] = null;
   $res['_Cmdid'] = null;
   $res['_Clientip'] = null;
   $res['_Remoteip'] = null;
   $res['_Versionnum'] = null;
   $res['_Method'] = null;

   $out=split (' ', $line);
   $map = "";    
   return $out;
}
    $line = "a b c d";
foreach (agent($line) as $v){
    echo $v;
}
?>
