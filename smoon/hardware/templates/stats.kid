<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title> Stats </title>
</head>
<body>
    <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
        <tr>
            <th valign="top" width="25%">Total Registered Hosts</th>
            <td><strong>${Stat['totalHosts']}</strong></td>
        </tr>
        <tr>
            <th valign="top">Total Registered Devices</th>
            <td><strong>${Device.select('1=1').count()}</strong></td>
        </tr>
        <tr>
            <th valign="top">Total bogomips</th>
            <td><strong>${Stat["bogomipsTot"]}</strong></td>
        </tr>
        <tr>
            <th valign="top">Total processors</th>
            <td><strong>${Stat["cpusTot"]}</strong></td>
        </tr>
        <tr>
            <th valign="top">Total MHz</th>
            <td><strong>${Stat["cpuSpeedTot"]}</strong></td>
        </tr>
    </table>
    <div class="tabber">
        <div class="tabbertab"><h2>Archs</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr><th>Arch</th><th>Count</th><th>% of total</th><th halign="left"> </th></tr>
                <tr py:for='arch in Stat["archs"]'>
                    <th align="right">${arch[0]}</th>
                    <td align="center">${arch[1]}</td>
                    <td><strong>${'%.1f' % (float(arch[1]) / Stat["archstot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(arch[1]) / Stat["archstot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>OS</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='OS in Stat["OS"]'>
                    <th align="right">${OS[0]}</th>
                    <td align="center">${OS[1]}</td>
                    <td><strong>${'%.1f' % (float(OS[1]) / Stat["OStot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(OS[1]) / Stat["OStot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>Runlevel</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='rl in Stat["runlevel"]'>
                    <th align="right">${rl[0]}</th>
                    <td align="center">${rl[1]}</td>
                    <td><strong>${'%.1f' % (float(rl[1]) / Stat["runleveltot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(rl[1]) / Stat["runleveltot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>Language</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='lang in Stat["language"]'>
                    <th align="right">${lang[0]}</th>
                    <td align="center">${lang[1]}</td>
                    <td><strong>${'%.1f' % (float(lang[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(lang[1]) / Stat["languagetot"] * 500 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>Vendor</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='vendor in Stat["vendors"]'>
                    <th align="right">${vendor[0]}</th>
                    <td align="center">${vendor[1]}</td>
                    <td><strong>${'%.1f' % (float(vendor[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(vendor[1]) / Stat["languagetot"] * 500 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>Model</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='system in Stat["systems"]'>
                    <!-- Temporary solution to a silly problem -->
                    <th align="right">${system[0].split(' Not')[0].split(' To be')[0].split('System Version')[0]}</th>
                    <td align="center">${system[1]}</td>
                    <td><strong>${'%.1f' % (float(system[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(system[1]) / Stat["languagetot"] * 1000 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>RAM</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='mem in Stat["sysMem"]'>
                    <th align="right">${mem[0]}</th>
                    <td align="center">${mem[1]}</td>
                    <td><strong>${'%.1f' % (float(mem[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(mem[1]) / Stat["languagetot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>Swap</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='mem in Stat["swapMem"]'>
                    <th align="right">${mem[0]}</th>
                    <td align="center">${mem[1]}</td>
                    <td><strong>${'%.1f' % (float(mem[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(mem[1]) / Stat["languagetot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>MHz</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='cpuSpeed in Stat["cpuSpeed"]'>
                    <th align="right">${cpuSpeed[0]}</th>
                    <td align="center">${cpuSpeed[1]}</td>
                    <td><strong>${'%.1f' % (float(cpuSpeed[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(cpuSpeed[1]) / Stat["languagetot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>CPUs</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='numCPUs in Stat["numCPUs"]'>
                    <th align="right">${numCPUs[0]}</th>
                    <td align="center">${numCPUs[1]}</td>
                    <td><strong>${'%.1f' % (float(numCPUs[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(numCPUs[1]) / Stat["languagetot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>CPUVendor</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='cpuVendor in Stat["cpuVendor"]'>
                    <th align="right">${cpuVendor[0]}</th>
                    <td align="center">${cpuVendor[1]}</td>
                    <td><strong>${'%.1f' % (float(cpuVendor[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(cpuVendor[1]) / Stat["languagetot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>bogomips</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='bogomips in Stat["bogomips"]'>
                    <th align="right">${bogomips[0]}</th>
                    <td align="center">${bogomips[1]}</td>
                    <td><strong>${'%.1f' % (float(bogomips[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(bogomips[1]) / Stat["languagetot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
        <div class="tabbertab"><h2>kernel</h2>
            <table id="stats" width="100%" border="0" cellpadding="3" cellspacing="3">
                <tr py:for='kernelVersion in Stat["kernelVersion"]'>
                    <th align="right">${kernelVersion[0]}</th>
                    <td align="center">${kernelVersion[1]}</td>
                    <td><strong>${'%.1f' % (float(kernelVersion[1]) / Stat["languagetot"] * 100) } %</strong></td>
                    <td><img py:for='i in range(1, int( float(kernelVersion[1]) / Stat["languagetot"] * 100 ))' src='/static/images/tile.png' /></td>
                </tr>
            </table>
        </div>
    </div>

</body>
</html>
