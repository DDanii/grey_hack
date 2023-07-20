//rshell_interface
metaxploit = include_lib("/lib/metaxploit.so")
if not metaxploit then
	metaxploit = include_lib(current_path + "/metaxploit.so")
end if
if not metaxploit then exit("Error: Can't find metaxploit library in the /lib path or the current folder")
print("Listening for upcoming connections...")

shells = []
while shells.len == 0	
	shells = metaxploit.rshell_server
	if(typeof(shells) == "string") then exit(shells)	
	if(shells.len == 0) then wait(2)
end while

option = 0
while typeof(option) != "number" or (option < 1 or option > shells.len)
	print(shells.len + " shell(s) connected!\n<b>Select a shell to start a terminal:</b>")
	for i in range(0, shells.len - 1)
		print("\n<b>Shell (" + (i + 1) + ")</b>\nPublic IP: " + shells[i].host_computer.public_ip + "\nLocal IP: " + shells[i].host_computer.local_ip)
	end for
	print("-----------")
	option = user_input("Select shell>").to_int
end while
print("Starting shell #" + option)
shells[option - 1].start_terminal