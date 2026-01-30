while ($true) {
    wevtutil qe System /f:text /c:5 >> data\windows_system.log
    Start-Sleep -Seconds 5
}
