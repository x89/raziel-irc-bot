import unittest
import ircbot
import ircbot.irc as irc
import ircbot.bot as bot

class PluginTestCase(unittest.TestCase):
	cfg = {}

	def setUp(self):
		ircbot.cfg.update(self.cfg)
		self.channel = irc.Channel('#test')
		self.bot = bot.Bot('localhost:6667')

	def _create_msg(self, message, source=None, is_admin=False):
		if not isinstance(message, irc.Message):
			if not source:
				source = 'test!bar@baz.com'
			message = irc.Message(source, '#test', message)
		message.user.is_admin = is_admin
		return message

	def reply(self, message, **kwargs):
		message = self._create_msg(message, **kwargs)
		for reply in self.plugin.replies:
			ret = reply(message)
			if ret:
				return ret

	def cmd(self, message, **kwargs):
		message = self._create_msg(message, **kwargs)
		command = bot.CommandMessage(message)
		func = self.plugin.commands[command.command]
		return func(command)