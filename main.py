import npc

test = npc.base_ideolog("Testism",["To debug", "To fix", "To analyze"])
guy = npc.npc("Joe", test)

npc.introduce(guy)
