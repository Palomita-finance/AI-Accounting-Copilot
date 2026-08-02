# AI Accounting Copilot

## Overview

AI Accounting Copilot is an AI-powered financial analysis assistant built with Python and an LLM Agent architecture. It reads structured accounting data, coordinates deterministic financial tools, and converts their results into a management-oriented financial diagnosis.

## Problem

Traditional financial analysis workflows are repetitive and rule-based. Analysts repeatedly calculate the same indicators, review large expense tables, inspect trends, identify unusual transactions, and assemble management reports. A standalone LLM can summarize text, but it cannot replace reliable accounting calculations.

## Solution

This project combines deterministic financial tools with LLM reasoning capabilities. Financial calculations remain in testable Python functions, while the LLM decides which tool should run next. The final response is generated only after the Agent has collected the required metrics, anomaly results, trends, and financial insights.

## Architecture

```text
Router
  ↓
Agent Loop
  ↓
Financial Tools
  ↓
Agent Context
  ↓
AI Response
```

The Router evaluates the user question and current state. The Agent Loop controls execution and prevents repeated or out-of-order calls. Financial Tools perform deterministic analysis. Agent Context stores successful results and execution history. AI Response converts the completed context into a readable financial report.

## Technical Highlights

- Tool orchestration with an LLM Router
- Stateful context management across the Agent workflow
- LLM decision making with deterministic execution safeguards
- Financial analytics pipeline for metrics, anomalies, trends, and insights
- Streamlit dashboard for interactive analysis and report download
- Local `.env` and Streamlit Cloud Secrets support

## Use Cases

- Financial risk analysis
- Expense monitoring and abnormal transaction review
- Monthly cost trend analysis
- Management reporting and decision support
