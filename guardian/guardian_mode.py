class GuardianMode:

def __init__(self):
self.active = False

def activate(self, behavior_score):

if behavior_score >= 0.8:
self.active = True

return {
"guardian_mode": "ACTIVE",
"message": "⚠️ Emotional escalation detected.",
"suggestion": "Pause trading briefly and review risk exposure."
}

elif behavior_score >= 0.5:

return {
"guardian_mode": "WATCH",
"message": "⚡ Risky behavior pattern detected.",
"suggestion": "Consider reviewing position sizing and leverage."
}

else:

return {
"guardian_mode": "OFF",
"message": "Normal trading behavior detected.",
"suggestion": None
}
class GuardianMode:

def __init__(self):
self.active = False

def activate(self, behavior_score):

if behavior_score >= 0.8:
self.active = True

return {
"guardian_mode": "ACTIVE",
"message": "⚠️ Emotional escalation detected.",
"suggestion": "Pause trading briefly and review risk exposure."
}

elif behavior_score >= 0.5:

return {
"guardian_mode": "WATCH",
"message": "⚡ Risky behavior pattern detected.",
"suggestion": "Consider reviewing position sizing and leverage."
}

else:

return {
"guardian_mode": "OFF",
"message": "Normal trading behavior detected.",
"suggestion": None
}
