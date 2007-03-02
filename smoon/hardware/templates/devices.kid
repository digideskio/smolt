<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title> Stats </title>
</head>
<body>
    <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
        <tr>
            <th valign="top" width="25%">Total Registered Devices</th>
            <td><strong>${devices["total"]}</strong></td>
        </tr>
        <tr>
            <th valign="top" width="25%">Unique Devices</th>
            <td><strong>${devices["count"]}</strong></td>
        </tr>
    </table>
    <div class="tabber">
        <div class="tabbertab"><h2>Raw Devices</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='dev in devices["totalList"]'>
                    <th align="right">${dev[0]}</th>
                    <td align="center">${dev[1]}</td>
                    <td nowrap="true"><strong>${'%.1f' % (float(dev[1]) / devices["total"] * 100) } %</strong></td>
                    <td nowrap="true"><img py:for='i in range(1, int( float(dev[1]) / devices["total"] * 1000 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>Machines / Device</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='dev in devices["uniqueList"]'>
                    <th align="right">${dev[0]}</th>
                    <td align="center">${dev[1]}</td>
                    <td nowrap="true"><strong>${'%.1f' % (float(dev[1]) / devices["totalHosts"] * 100) } %</strong></td>
                    <td nowrap="true"><img py:for='i in range(1, int( float(dev[1]) / devices["totalHosts"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
       <div class="tabbertab"><h2>Classes</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='dev in devices["classes"]'>
                    <th align="right"><a href='/byClass?type=${dev[0]}'>${dev[0]}</a></th>
 <!--                   <td align="center">${dev[1]}</td>
                    <td nowrap="true"><strong>${'%.1f' % (float(dev[1]) / devices["count"] * 100) } %</strong></td>
                    <td nowrap="true"><img py:for='i in range(1, int( float(dev[1]) / devices["count"] * 100 ))' src='/static/images/tile.png' /></td>-->
                </tr>
            </table>
        </div>
     </div>

</body>
</html>
