import json
def load(assets):
 return {'land':json.loads((assets/'land.json').read_text()),'timing':json.loads((assets/'timing.json').read_text())}
