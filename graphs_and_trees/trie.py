"""
taken from interviewcake solution, thanks!
"""


class Trie:

    def __init__(self):
	self.root_node = {}

    def check_present_and_add(self, word):

	current_node = self.root_node
	is_new_word = False

	# Work downwards through the trie, adding nodes
	# as needed, and keeping track of whether we add
	# any nodes.
	for char in word:
            if char not in current_node:
		is_new_word = True
		current_node[char] = {}
            current_node = current_node[char]

	# Explicitly mark the end of a word.
	# Otherwise, we might say a word is
	# present if it is a prefix of a different,
	# longer word that was added earlier.
	if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

	return is_new_word
