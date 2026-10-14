import json
def load(assets):
 return {'timing':json.loads((assets/'timing.json').read_text())}
