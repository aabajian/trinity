import ConfigParser, os, sys, requests

class RESTDevice:

	def __init__(self, base_url, rest_options):
		self.base_url = base_url
		self.rest_options = rest_options

	def execute_command(self, params):

		endpoint = self.base_url
		options = {}
		if len(self.rest_options) == 1:
			endpoint += self.rest_options[0].endpoint
			options = self.rest_options[0].execute_command(params)

		response = requests.get(endpoint, params=options)
		print(response.content)


class RESTOption:
	
	def __init__(self, endpoint):
		endpoint = endpoint.split()
		if not endpoint:
			print('Missing endpoint for option.')

		self.endpoint = endpoint[0]

		self.params = {}
		for param in endpoint[1:]:
			key, value = param.split(':')
			self.params[key] = value

	def execute_command(self, params):

		options = {}

		if len(params) == len(self.params) == 1:
			options[self.params.keys()[0]] = params[0]
		else:
			print('Missing required parameter: %s' % params)

		return options

		# We verify that all required endpoint
		# parameters have been provided.

class Trinity:

	def __init__(self):
		self.synonyms = {}

	def register(self, device, host):
		synonyms = []

		config_parser = ConfigParser.ConfigParser()

		config_parser.read('gotoanswer.trinity')
		sections = config_parser.sections()

		commands = []
		command_executions = None

		for section in sections:
			options = config_parser.options(section)
			if section == 'Device Information':
				for option in options:
					if option == 'commands':
						commands.append(config_parser.get(section,option))
			if section == 'Command Execution':
				command_executions = section

			if section == 'Synonyms':
				for option in options:
					synonyms.append(option)

		rest_options = []
		if commands and command_executions:
			command_execution_options = config_parser.options(command_executions)
			for command in commands:
				if command not in command_execution_options:
					print('Missing options for command %s' % command)
					sys.exit(1)

			options = config_parser.get(command_executions, command)
			rest_options.append(RESTOption(options))

		rest_device = RESTDevice(host, rest_options)
		for synonym in synonyms:
			self.synonyms[synonym] = rest_device


	def get(self, synonym, value):
		if synonym not in self.synonyms:
			print('Unable to find synonym %s' % synonym)
			sys.exit(1)

		self.synonyms[synonym].execute_command(params=[value])

# Dictionary of synonyms.
trinity = Trinity()
trinity.register('goto: answer', 'http://gotoanswer.com')
trinity.get('gta', 'Batman')