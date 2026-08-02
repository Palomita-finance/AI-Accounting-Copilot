import unittest
from unittest.mock import patch

import pandas as pd

from src.agent.agent_loop import run_agent
from src.insight import generate_insight
from src.metrics import calculate_metrics


class AgentV1Tests(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame(
            {
                "日期": ["2026-01-01", "2026-02-01"],
                "类别": ["销售", "设备"],
                "收入": [0, 0],
                "支出": [100, 6000]
            }
        )

    def test_zero_income_has_no_profit_margin(self):
        metrics = calculate_metrics(self.data)
        self.assertIsNone(metrics["利润率"])
        self.assertIn(
            "当前没有收入数据，无法计算利润率，需要关注收入来源和经营状态",
            generate_insight(metrics, 1)
        )

    @patch(
        "src.agent.agent_loop.generate_agent_answer",
        return_value="测试分析结果"
    )
    @patch("src.agent.agent_loop.choose_tool_with_llm")
    def test_agent_runs_each_tool_once(self, router, _response):
        router.side_effect = [
            {"action": "tool", "tool": "metrics_tool"},
            {"action": "tool", "tool": "metrics_tool"},
            {"action": "finish", "tool": None},
            {"action": "tool", "tool": "insight_tool"}
        ]

        answer = run_agent(self.data.copy(), "分析财务风险")

        self.assertEqual(answer, "测试分析结果")
        self.assertEqual(router.call_count, 4)


if __name__ == "__main__":
    unittest.main()
