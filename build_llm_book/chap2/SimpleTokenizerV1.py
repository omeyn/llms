class SimpleTokenizerV1:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}
        self.next_id = 0

    def tokenize(self, text):
        tokens = text.split()
        token_ids = []
        for token in tokens:
            if token not in self.vocab:
                self.vocab[token] = self.next_id
                self.inverse_vocab[self.next_id] = token
                self.next_id += 1
            token_ids.append(self.vocab[token])
        return token_ids

    def detokenize(self, token_ids):
        tokens = [self.inverse_vocab[token_id] for token_id in token_ids]
        return ' '.join(tokens)