import main
ftp = main.FtpClient()
ftp.connect("localhost",9990)
ftp.interactive()