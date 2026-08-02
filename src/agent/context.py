class AgentContext:

    def __init__(self, data, question):

        self.data = data

        self.question = question

        self.metrics = None

        self.abnormal = None

        self.trend = None

        self.ai_answer = None

        self.history = []

        self.insights = None

        self.completed_tools = []
