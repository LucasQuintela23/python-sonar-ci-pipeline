"""
Credit Engine Module

This module provides credit analysis and loan approval functionality.
It includes methods for calculating credit scores and approving loan requests.
"""


class CreditAnalysis:
    """
    A class to analyze credit worthiness and approve loans.
    
    This class provides methods to calculate credit scores based on income
    and debt, and to approve loan requests based on score and amount criteria.
    """
    
    MIN_SCORE_FOR_APPROVAL: int = 600
    MAX_LOAN_AMOUNT: float = 50000.0
    
    def calculate_score(self, income: float, debt: float) -> int:
        """
        Calculate a credit score based on income and debt.
        
        The score is calculated as: (income - debt) * 2, bounded between 0 and 1000.
        Score represents creditworthiness on a scale of 0 to 1000.
        
        Args:
            income: Annual income in currency units (float).
            debt: Total debt in currency units (float).
        
        Returns:
            int: Credit score between 0 and 1000.
        
        Raises:
            ValueError: If income or debt is negative.
        """
        if income < 0 or debt < 0:
            raise ValueError("Income and debt must be non-negative")
        
        score = (income - debt) * 2
        return max(0, min(int(score), 1000))
    
    def approve_loan(self, score: int, amount: float) -> bool:
        """
        Determine if a loan should be approved.
        
        A loan is approved if the credit score is greater than 600
        and the requested amount is less than 50,000.
        
        Args:
            score: Credit score (int).
            amount: Requested loan amount in currency units (float).
        
        Returns:
            bool: True if loan is approved, False otherwise.
        
        Raises:
            ValueError: If score is negative or amount is negative.
        """
        if score < 0 or amount < 0:
            raise ValueError("Score and amount must be non-negative")
        
        return score > self.MIN_SCORE_FOR_APPROVAL and amount < self.MAX_LOAN_AMOUNT
    
    def legacy_calculation(self, income: float, debt: float, employment_years: int) -> int:
        """
        Legacy method with unnecessary cognitive complexity.
        
        This method demonstrates poor code quality with deeply nested
        conditionals. It is kept for backwards compatibility but should
        not be used in new code.
        
        Args:
            income: Annual income (float).
            debt: Total debt (float).
            employment_years: Years of employment (int).
        
        Returns:
            int: Calculated score using legacy logic.
        """
        base_score = 0
        
        if income > 30000:
            if debt < 10000:
                if employment_years > 2:
                    if income > 50000:
                        base_score = 700
                    else:
                        base_score = 650
                else:
                    if income > 40000:
                        base_score = 600
                    else:
                        base_score = 500
            else:
                if employment_years > 5:
                    if income > 60000:
                        base_score = 650
                    else:
                        base_score = 550
                else:
                    if income > 45000:
                        base_score = 500
                    else:
                        base_score = 400
        else:
            if debt < 5000:
                if employment_years > 1:
                    base_score = 400
                else:
                    base_score = 300
            else:
                base_score = 200
        
        return base_score
