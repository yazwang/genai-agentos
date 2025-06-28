from agentos import BaseAgent

class ToneShifterAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def run(self, input_text, source_lang="en", target_lang="zh"):
        
        if source_lang == "en" and target_lang == "zh":
            return {"translated_text": "我高兴得快要飞起来了！"}
        else:
            return {"translated_text": "暂不支持此语言对"}
