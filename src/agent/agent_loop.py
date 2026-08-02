from src.agent.context import AgentContext

from src.agent.llm_router import choose_tool_with_llm

from src.agent.agent_executor import execute_tool

from src.agent.agent_response import generate_agent_answer


def run_agent(data, question):

    # 初始化Agent状态
    context = AgentContext(
        data,
        question
    )

    # 最大执行次数保护
    max_steps = 10

    for step in range(max_steps):

        print(f"\n--- Agent第 {step + 1} 步 ---")

        # =========================
        # 1. 检查是否已经完成
        # =========================

        if check_task_complete(context):

            print("Agent任务已经完成")

            break

        # =========================
        # 2. 让LLM决定下一步
        # =========================

        expected_tool = get_next_required_tool(context)

        try:
            decision = choose_tool_with_llm(
                question,
                context
            )
        except Exception as exc:
            print(f"路由失败，使用流程兜底: {exc}")
            decision = {
                "action": "tool",
                "tool": expected_tool
            }

        # 保证依赖顺序稳定，防止提前结束、越级或重复调用。
        if (
            decision.get("action") != "tool"
            or decision.get("tool") != expected_tool
        ):
            decision = {
                "action": "tool",
                "tool": expected_tool
            }

        print("Agent决定:")
        print(decision)

        # =========================
        # 3. 执行动作
        # =========================

        action = decision.get("action")

        # ---- 调用工具 ----

        if action == "tool":

            tool_name = decision.get("tool")

            # 防止重复工具调用
            if tool_name in context.completed_tools:

                print(
                    f"{tool_name} 已经执行过，跳过"
                )

                continue

            print("执行工具:")
            print(tool_name)

            try:
                result = execute_tool(
                    tool_name,
                    context
                )
            except Exception as exc:
                result = {
                    "tool": tool_name,
                    "success": False,
                    "error": str(exc)
                }

            print("工具结果:")
            print(result)

            # 保存执行记录

            context.history.append(result)

            if result.get("success") is True:
                context.completed_tools.append(
                    tool_name
                )

        # ---- AI认为可以结束 ----

        elif action == "answer":

            print(
                "Agent认为可以直接回答"
            )

            break

        # ---- Agent主动结束 ----

        elif action == "finish":

            print(
                "Agent完成任务"
            )

            break

        else:

            print(
                "未知action，停止"
            )

            break

    # =========================
    # 最终回答
    # =========================

    answer = generate_agent_answer(
        question,
        context
    )

    context.ai_answer = answer

    return answer


def check_task_complete(context):
    """
    判断任务是否完成

    """

    required_tools = [

        "metrics_tool",

        "abnormal_tool",

        "trend_tool",

        "insight_tool"

    ]

    # 如果所有分析工具完成

    if all(
        tool in context.completed_tools
        for tool in required_tools
    ):

        return True

    return False


def get_next_required_tool(context):
    required_tools = [
        "metrics_tool",
        "abnormal_tool",
        "trend_tool",
        "insight_tool"
    ]

    return next(
        (
            tool
            for tool in required_tools
            if tool not in context.completed_tools
        ),
        None
    )
