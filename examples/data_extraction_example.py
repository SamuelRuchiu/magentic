from pydantic import BaseModel, Field
from magentic import prompt

# 1. Define the strict data schema we want the LLM to output
class FinancialData(BaseModel):
    revenue_millions: float = Field(description="Total revenue in millions of dollars")
    profit_millions: float = Field(description="Net profit in millions of dollars")
    sentiment: str = Field(description="Overall sentiment: 'Bullish', 'Bearish', or 'Neutral'")

# 2. Create the LLM pipeline using the decorator
@prompt("Extract the core financial metrics from the following earnings report: {earnings_text}")
def extract_financials(earnings_text: str) -> FinancialData:
    ... # The decorator handles sending the prompt and coercing the output to FinancialData

# 3. Test the extraction
if __name__ == "__main__":
    sample_report = "Q3 was a phenomenal quarter for TechCorp. We generated $450.5 million in top-line revenue, leaving us with a net profit of $120.2 million. Market conditions look incredibly favorable for next year."

    extracted_data = extract_financials(sample_report)

    print("--- Extracted Structured Data ---")
    print(f"Revenue: ${extracted_data.revenue_millions}M")
    print(f"Profit: ${extracted_data.profit_millions}M")
    print(f"Sentiment: {extracted_data.sentiment}")