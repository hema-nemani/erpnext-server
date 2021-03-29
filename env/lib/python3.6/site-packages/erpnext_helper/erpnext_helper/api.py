import frappe

# put this in default loc
ssl_script = """
print `hi do you have a domain name`?
if domain_yes: lets set it up

ok now do you have an ssl cert
if domain_yes: if not, our friends at let's encryot can help us out
"""

# put this in bashrc
curr_dir = """
cd {bench_dir}
"""

"""
do test ip: 139.59.2.3
frappe: changethispassword
"""


def setup_ssl_helper():
	script_location = input("Input Script Location: ")
	with open(script_location, 'w') as f:
		f.write(ssl_script)

def setup_current_directory():
	with open('~/.bashrc', 'a') as f:
		f.write(curr_dir)

def setup_helpers():
	"""Sets up `easy setup` for single site self hosted"""
	setup_current_directory()
	setup_ssl_helper()
