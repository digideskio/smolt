<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/plain; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Error!</title>
</head>
<body>

<table>
    <tr><th>${linkSQL.user_name}</th></tr>
    <tr py:for="host in linkSQL.hosts">
        <td><a href='show?UUID=${host.uuid}'>${host.uuid}</a></td>
    </tr>
</table>
</body>
</html>
