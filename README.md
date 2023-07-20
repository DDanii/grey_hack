# Grey Hack

### libversion.src

Show the version number for specified library.

```
libversion [file path]
```

### wificrack.src

Crack available wifi one by one.

```
wificrack wlan0
```

### netploit.src

Scan the remote target for vulnerabilities.

```
netploit [ip] [port]
```

### netoverflow.src

Apply exploit on the remote target.

```
netoverflow [ip] [port] [memory] [value]
```

### qcrack.src

Constantly waiting for the password hash to be cracked.

```
qcrack
```

### files.src

Search files on computers, filter and process them.

```
files -h -x cmd -l root expression
```

```
files Mail.txt -x cat
```

```
files Mail.txt -l /home
```

### decipher.src

Decrypt all lines from files and print the result.

```
decipher [file|encrypted text]
```