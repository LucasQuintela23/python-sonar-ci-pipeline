"""
Test module for credit_engine.

This module contains unit tests for the CreditAnalysis class.
Tests cover both positive and negative scenarios for the main methods.
"""

import pytest
import allure
from src.credit_engine import CreditAnalysis


@allure.feature("Credit Analysis")
@allure.story("Calculate Score")
class TestCreditAnalysisCalculateScore:
    """Tests for the calculate_score method."""
    
    @pytest.fixture
    def credit_analysis(self):
        """Create a CreditAnalysis instance for testing."""
        return CreditAnalysis()
    
    @allure.title("Test calculate_score with positive income and zero debt")
    @allure.description("Should calculate score correctly for income with no debt")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculate_score_positive_case(self, credit_analysis):
        """Test calculate_score with positive income and zero debt."""
        score = credit_analysis.calculate_score(income=400, debt=0)
        assert score == 800
    
    @allure.title("Test calculate_score with both income and debt")
    @allure.description("Should calculate score by subtracting debt from income")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculate_score_with_debt(self, credit_analysis):
        """Test calculate_score with both income and debt."""
        score = credit_analysis.calculate_score(income=500, debt=200)
        assert score == 600
    
    @allure.title("Test calculate_score cap at 1000")
    @allure.description("Score should be capped at maximum value 1000")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculate_score_cap_at_1000(self, credit_analysis):
        """Test that score is capped at 1000."""
        score = credit_analysis.calculate_score(income=1000000, debt=0)
        assert score == 1000
    
    @allure.title("Test calculate_score with zero values")
    @allure.description("Should return 0 when both income and debt are zero")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculate_score_zero_values(self, credit_analysis):
        """Test calculate_score with zero income and zero debt."""
        score = credit_analysis.calculate_score(income=0, debt=0)
        assert score == 0
    
    @allure.title("Test calculate_score when debt exceeds income")
    @allure.description("Score should be bounded at 0 when debt is higher than income")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculate_score_debt_greater_than_income(self, credit_analysis):
        """Test calculate_score when debt exceeds income."""
        score = credit_analysis.calculate_score(income=10000, debt=30000)
        assert score == 0
    
    @allure.title("Test calculate_score with negative income raises error")
    @allure.description("Should raise ValueError for negative income")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculate_score_negative_income_raises_error(self, credit_analysis):
        """Test that negative income raises ValueError."""
        with pytest.raises(ValueError):
            credit_analysis.calculate_score(income=-5000, debt=0)
    
    @allure.title("Test calculate_score with negative debt raises error")
    @allure.description("Should raise ValueError for negative debt")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculate_score_negative_debt_raises_error(self, credit_analysis):
        """Test that negative debt raises ValueError."""
        with pytest.raises(ValueError):
            credit_analysis.calculate_score(income=50000, debt=-1000)


@allure.feature("Credit Analysis")
@allure.story("Approve Loan")
class TestCreditAnalysisApproveLoan:
    """Tests for the approve_loan method."""
    
    @pytest.fixture
    def credit_analysis(self):
        """Create a CreditAnalysis instance for testing."""
        return CreditAnalysis()
    
    @allure.title("Test loan approval with valid score and amount")
    @allure.description("Should approve loan when score > 600 and amount < 50000")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_approve_loan_approved(self, credit_analysis):
        """Test loan approval with valid score and amount."""
        approved = credit_analysis.approve_loan(score=700, amount=30000)
        assert approved is True
    
    @allure.title("Test loan rejection due to low score")
    @allure.description("Should reject loan when score is below threshold")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_approve_loan_score_too_low(self, credit_analysis):
        """Test loan rejection due to low score."""
        approved = credit_analysis.approve_loan(score=500, amount=30000)
        assert approved is False
    
    @allure.title("Test loan rejection at exact score threshold")
    @allure.description("Should reject loan when score equals 600 (not > 600)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_approve_loan_score_exactly_threshold(self, credit_analysis):
        """Test loan approval with score exactly at threshold."""
        approved = credit_analysis.approve_loan(score=600, amount=30000)
        assert approved is False
    
    @allure.title("Test loan approval just above score threshold")
    @allure.description("Should approve loan when score is 601 (> 600)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_approve_loan_score_above_threshold(self, credit_analysis):
        """Test loan approval with score just above threshold."""
        approved = credit_analysis.approve_loan(score=601, amount=30000)
        assert approved is True
    
    @allure.title("Test loan rejection due to high amount")
    @allure.description("Should reject loan when amount >= 50000")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_approve_loan_amount_too_high(self, credit_analysis):
        """Test loan rejection due to high amount."""
        approved = credit_analysis.approve_loan(score=700, amount=50000)
        assert approved is False
    
    @allure.title("Test loan approval with amount just below limit")
    @allure.description("Should approve loan when amount < 50000")
    @allure.severity(allure.severity_level.NORMAL)
    def test_approve_loan_amount_just_below_limit(self, credit_analysis):
        """Test loan approval with amount just below limit."""
        approved = credit_analysis.approve_loan(score=700, amount=49999.99)
        assert approved is True
    
    @allure.title("Test loan rejection when both conditions fail")
    @allure.description("Should reject loan when both score is low and amount is high")
    @allure.severity(allure.severity_level.NORMAL)
    def test_approve_loan_both_conditions_fail(self, credit_analysis):
        """Test loan rejection when both conditions fail."""
        approved = credit_analysis.approve_loan(score=500, amount=60000)
        assert approved is False
    
    @allure.title("Test approve_loan with negative score raises error")
    @allure.description("Should raise ValueError for negative score")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_approve_loan_negative_score_raises_error(self, credit_analysis):
        """Test that negative score raises ValueError."""
        with pytest.raises(ValueError):
            credit_analysis.approve_loan(score=-100, amount=30000)
    
    @allure.title("Test approve_loan with negative amount raises error")
    @allure.description("Should raise ValueError for negative amount")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_approve_loan_negative_amount_raises_error(self, credit_analysis):
        """Test that negative amount raises ValueError."""
        with pytest.raises(ValueError):
            credit_analysis.approve_loan(score=700, amount=-5000)


@allure.feature("Credit Analysis")
@allure.story("Integration Tests")
class TestCreditAnalysisIntegration:
    """Integration tests combining calculate_score and approve_loan."""
    
    @pytest.fixture
    def credit_analysis(self):
        """Create a CreditAnalysis instance for testing."""
        return CreditAnalysis()
    
    @allure.title("Test complete workflow resulting in loan approval")
    @allure.description("End-to-end test: calculate score and approve loan")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_full_workflow_approved(self, credit_analysis):
        """Test complete workflow from score calculation to approval."""
        score = credit_analysis.calculate_score(income=60000, debt=10000)
        approved = credit_analysis.approve_loan(score=score, amount=20000)
        assert approved is True
    
    @allure.title("Test complete workflow resulting in rejection (low income)")
    @allure.description("End-to-end test: score calculation fails approval due to low income")
    @allure.severity(allure.severity_level.NORMAL)
    def test_full_workflow_rejected_low_income(self, credit_analysis):
        """Test complete workflow resulting in rejection due to low income."""
        score = credit_analysis.calculate_score(income=200, debt=50)
        approved = credit_analysis.approve_loan(score=score, amount=20000)
        assert approved is False
    
    @allure.title("Test complete workflow resulting in rejection (high amount)")
    @allure.description("End-to-end test: loan rejected due to high requested amount")
    @allure.severity(allure.severity_level.NORMAL)
    def test_full_workflow_rejected_high_amount(self, credit_analysis):
        """Test complete workflow resulting in rejection due to high amount."""
        score = credit_analysis.calculate_score(income=100000, debt=10000)
        approved = credit_analysis.approve_loan(score=score, amount=60000)
        assert approved is False
