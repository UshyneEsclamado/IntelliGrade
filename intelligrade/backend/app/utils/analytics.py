"""
Analytics utilities for IntelliGrade
Provides performance analytics and reporting functionality
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import statistics

logger = logging.getLogger(__name__)

class GradingAnalytics:
    def __init__(self):
        pass
    
    def calculate_assessment_statistics(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate comprehensive statistics for an assessment"""
        
        if not results:
            return {
                "total_submissions": 0,
                "average_score": 0,
                "median_score": 0,
                "score_distribution": {},
                "grade_distribution": {},
                "difficulty_analysis": "No data available"
            }
        
        scores = [r.get('percentage', 0) for r in results]
        grades = [r.get('letter_grade', 'F') for r in results]
        
        # Basic statistics
        stats = {
            "total_submissions": len(results),
            "average_score": round(statistics.mean(scores), 2),
            "median_score": round(statistics.median(scores), 2),
            "min_score": min(scores),
            "max_score": max(scores),
            "standard_deviation": round(statistics.stdev(scores) if len(scores) > 1 else 0, 2)
        }
        
        # Score distribution (by ranges)
        score_ranges = {
            "90-100": 0,
            "80-89": 0,
            "70-79": 0,
            "60-69": 0,
            "Below 60": 0
        }
        
        for score in scores:
            if score >= 90:
                score_ranges["90-100"] += 1
            elif score >= 80:
                score_ranges["80-89"] += 1
            elif score >= 70:
                score_ranges["70-79"] += 1
            elif score >= 60:
                score_ranges["60-69"] += 1
            else:
                score_ranges["Below 60"] += 1
        
        stats["score_distribution"] = score_ranges
        
        # Grade distribution
        grade_distribution = {}
        for grade in grades:
            grade_distribution[grade] = grade_distribution.get(grade, 0) + 1
        
        stats["grade_distribution"] = grade_distribution
        
        # Difficulty analysis
        stats["difficulty_analysis"] = self._analyze_difficulty(stats["average_score"])
        
        # Performance insights
        stats["insights"] = self._generate_performance_insights(stats, results)
        
        return stats
    
    def calculate_student_progress(self, student_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate progress analytics for a specific student"""
        
        if not student_results:
            return {
                "total_assessments": 0,
                "average_performance": 0,
                "progress_trend": "No data",
                "strengths": [],
                "areas_for_improvement": []
            }
        
        # Sort by date
        sorted_results = sorted(student_results, key=lambda x: x.get('graded_at', ''))
        
        scores = [r.get('percentage', 0) for r in sorted_results]
        
        progress = {
            "total_assessments": len(sorted_results),
            "average_performance": round(statistics.mean(scores), 2),
            "latest_score": scores[-1] if scores else 0,
            "best_score": max(scores) if scores else 0,
            "progress_trend": self._calculate_trend(scores),
            "consistency": self._calculate_consistency(scores)
        }
        
        # Analyze question type performance
        question_type_performance = self._analyze_question_type_performance(sorted_results)
        progress["question_type_analysis"] = question_type_performance
        
        # Identify strengths and weaknesses
        strengths, weaknesses = self._identify_strengths_weaknesses(question_type_performance)
        progress["strengths"] = strengths
        progress["areas_for_improvement"] = weaknesses
        
        # Recent performance (last 5 assessments)
        recent_results = sorted_results[-5:] if len(sorted_results) >= 5 else sorted_results
        recent_scores = [r.get('percentage', 0) for r in recent_results]
        progress["recent_average"] = round(statistics.mean(recent_scores), 2) if recent_scores else 0
        
        return progress
    
    def generate_class_report(self, all_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive class performance report"""
        
        if not all_results:
            return {"error": "No data available for class report"}
        
        # Group results by student
        student_results = {}
        for result in all_results:
            student_id = result.get('student_id')
            if student_id not in student_results:
                student_results[student_id] = []
            student_results[student_id].append(result)
        
        # Calculate class-wide statistics
        all_scores = [r.get('percentage', 0) for r in all_results]
        
        class_report = {
            "overview": {
                "total_students": len(student_results),
                "total_assessments": len(all_results),
                "class_average": round(statistics.mean(all_scores), 2),
                "median_score": round(statistics.median(all_scores), 2),
                "score_range": {
                    "min": min(all_scores),
                    "max": max(all_scores)
                }
            },
            "performance_distribution": self._calculate_performance_distribution(all_scores),
            "student_rankings": self._calculate_student_rankings(student_results),
            "improvement_trends": self._analyze_class_improvement_trends(student_results),
            "common_challenges": self._identify_common_challenges(all_results)
        }
        
        return class_report
    
    def _analyze_difficulty(self, average_score: float) -> str:
        """Analyze assessment difficulty based on average score"""
        
        if average_score >= 85:
            return "Easy - Most students performed well"
        elif average_score >= 75:
            return "Moderate - Good overall performance"
        elif average_score >= 65:
            return "Challenging - Mixed performance"
        elif average_score >= 55:
            return "Difficult - Students struggled"
        else:
            return "Very Difficult - Significant challenges for most students"
    
    def _generate_performance_insights(self, stats: Dict[str, Any], results: List[Dict[str, Any]]) -> List[str]:
        """Generate insights from performance statistics"""
        
        insights = []
        
        avg_score = stats["average_score"]
        std_dev = stats["standard_deviation"]
        
        # Average performance insights
        if avg_score >= 85:
            insights.append("Excellent overall class performance")
        elif avg_score >= 75:
            insights.append("Good overall class performance")
        elif avg_score < 65:
            insights.append("Class may need additional review of this material")
        
        # Score distribution insights
        high_performers = stats["score_distribution"]["90-100"]
        low_performers = stats["score_distribution"]["Below 60"]
        total = stats["total_submissions"]
        
        if high_performers / total > 0.5:
            insights.append("Over half the class achieved excellent scores")
        
        if low_performers / total > 0.3:
            insights.append("Significant portion of class needs additional support")
        
        # Consistency insights
        if std_dev < 10:
            insights.append("Consistent performance across students")
        elif std_dev > 20:
            insights.append("Wide variation in student performance")
        
        return insights
    
    def _calculate_trend(self, scores: List[float]) -> str:
        """Calculate performance trend from scores"""
        
        if len(scores) < 2:
            return "Insufficient data"
        
        # Simple linear trend calculation
        recent_avg = statistics.mean(scores[-3:]) if len(scores) >= 3 else scores[-1]
        early_avg = statistics.mean(scores[:3]) if len(scores) >= 3 else scores[0]
        
        difference = recent_avg - early_avg
        
        if difference > 5:
            return "Improving"
        elif difference < -5:
            return "Declining"
        else:
            return "Stable"
    
    def _calculate_consistency(self, scores: List[float]) -> Dict[str, Any]:
        """Calculate consistency metrics for student performance"""
        
        if len(scores) < 2:
            return {"level": "Unknown", "variation": 0}
        
        std_dev = statistics.stdev(scores)
        mean_score = statistics.mean(scores)
        
        # Coefficient of variation
        cv = (std_dev / mean_score) * 100 if mean_score > 0 else 0
        
        if cv < 10:
            level = "Very Consistent"
        elif cv < 20:
            level = "Consistent"
        elif cv < 30:
            level = "Moderately Consistent"
        else:
            level = "Inconsistent"
        
        return {
            "level": level,
            "variation": round(cv, 2),
            "standard_deviation": round(std_dev, 2)
        }
    
    def _analyze_question_type_performance(self, results: List[Dict[str, Any]]) -> Dict[str, Dict[str, float]]:
        """Analyze performance by question type across multiple assessments"""
        
        question_type_data = {}
        
        for result in results:
            question_results = result.get('question_results', [])
            
            for q_result in question_results:
                q_type = q_result.get('question_type', 'unknown')
                points_earned = q_result.get('points_earned', 0)
                points_possible = q_result.get('points_possible', 1)
                
                if q_type not in question_type_data:
                    question_type_data[q_type] = {
                        'total_points_earned': 0,
                        'total_points_possible': 0,
                        'question_count': 0
                    }
                
                question_type_data[q_type]['total_points_earned'] += points_earned
                question_type_data[q_type]['total_points_possible'] += points_possible
                question_type_data[q_type]['question_count'] += 1
        
        # Calculate percentages
        performance_by_type = {}
        for q_type, data in question_type_data.items():
            if data['total_points_possible'] > 0:
                percentage = (data['total_points_earned'] / data['total_points_possible']) * 100
                performance_by_type[q_type] = {
                    'percentage': round(percentage, 2),
                    'questions_answered': data['question_count'],
                    'total_points_earned': data['total_points_earned'],
                    'total_points_possible': data['total_points_possible']
                }
        
        return performance_by_type
    
    def _identify_strengths_weaknesses(self, question_type_performance: Dict[str, Dict[str, float]]) -> tuple:
        """Identify strengths and weaknesses from question type performance"""
        
        strengths = []
        weaknesses = []
        
        for q_type, performance in question_type_performance.items():
            percentage = performance['percentage']
            questions_count = performance['questions_answered']
            
            # Only consider if student has answered multiple questions of this type
            if questions_count >= 2:
                if percentage >= 80:
                    strengths.append({
                        'area': q_type.replace('_', ' ').title(),
                        'performance': f"{percentage:.0f}%",
                        'question_count': questions_count
                    })
                elif percentage <= 60:
                    weaknesses.append({
                        'area': q_type.replace('_', ' ').title(),
                        'performance': f"{percentage:.0f}%",
                        'question_count': questions_count
                    })
        
        # Sort by performance
        strengths.sort(key=lambda x: float(x['performance'].rstrip('%')), reverse=True)
        weaknesses.sort(key=lambda x: float(x['performance'].rstrip('%')))
        
        return strengths[:3], weaknesses[:3]  # Return top 3 of each
    
    def _calculate_performance_distribution(self, scores: List[float]) -> Dict[str, Dict[str, Any]]:
        """Calculate detailed performance distribution"""
        
        total_students = len(scores)
        
        # Grade ranges
        ranges = {
            "A (90-100)": {"count": 0, "percentage": 0},
            "B (80-89)": {"count": 0, "percentage": 0},
            "C (70-79)": {"count": 0, "percentage": 0},
            "D (60-69)": {"count": 0, "percentage": 0},
            "F (Below 60)": {"count": 0, "percentage": 0}
        }
        
        for score in scores:
            if score >= 90:
                ranges["A (90-100)"]["count"] += 1
            elif score >= 80:
                ranges["B (80-89)"]["count"] += 1
            elif score >= 70:
                ranges["C (70-79)"]["count"] += 1
            elif score >= 60:
                ranges["D (60-69)"]["count"] += 1
            else:
                ranges["F (Below 60)"]["count"] += 1
        
        # Calculate percentages
        for range_data in ranges.values():
            range_data["percentage"] = round((range_data["count"] / total_students) * 100, 1) if total_students > 0 else 0
        
        return ranges
    
    def _calculate_student_rankings(self, student_results: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """Calculate student rankings based on average performance"""
        
        student_averages = []
        
        for student_id, results in student_results.items():
            scores = [r.get('percentage', 0) for r in results]
            avg_score = statistics.mean(scores) if scores else 0
            
            student_averages.append({
                'student_id': student_id,
                'average_score': round(avg_score, 2),
                'total_assessments': len(results),
                'best_score': max(scores) if scores else 0,
                'recent_trend': self._calculate_trend(scores[-5:] if len(scores) >= 5 else scores)
            })
        
        # Sort by average score (descending)
        student_averages.sort(key=lambda x: x['average_score'], reverse=True)
        
        # Add rank
        for i, student in enumerate(student_averages):
            student['rank'] = i + 1
        
        return student_averages
    
    def _analyze_class_improvement_trends(self, student_results: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Analyze improvement trends across the class"""
        
        improvement_data = {
            "improving_students": 0,
            "stable_students": 0,
            "declining_students": 0,
            "overall_trend": "Stable"
        }
        
        trends = []
        
        for student_id, results in student_results.items():
            if len(results) >= 2:
                scores = [r.get('percentage', 0) for r in sorted(results, key=lambda x: x.get('graded_at', ''))]
                trend = self._calculate_trend(scores)
                trends.append(trend)
                
                if trend == "Improving":
                    improvement_data["improving_students"] += 1
                elif trend == "Declining":
                    improvement_data["declining_students"] += 1
                else:
                    improvement_data["stable_students"] += 1
        
        # Determine overall class trend
        if improvement_data["improving_students"] > improvement_data["declining_students"]:
            improvement_data["overall_trend"] = "Improving"
        elif improvement_data["declining_students"] > improvement_data["improving_students"]:
            improvement_data["overall_trend"] = "Declining"
        
        # Add percentages
        total_students = len([s for s in student_results.values() if len(s) >= 2])
        if total_students > 0:
            improvement_data["improvement_percentage"] = round((improvement_data["improving_students"] / total_students) * 100, 1)
            improvement_data["decline_percentage"] = round((improvement_data["declining_students"] / total_students) * 100, 1)
        
        return improvement_data
    
    def _identify_common_challenges(self, all_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify common challenges across all students"""
        
        question_type_errors = {}
        total_questions_by_type = {}
        
        for result in all_results:
            question_results = result.get('question_results', [])
            
            for q_result in question_results:
                q_type = q_result.get('question_type', 'unknown')
                is_correct = q_result.get('is_correct', False)
                
                if q_type not in question_type_errors:
                    question_type_errors[q_type] = 0
                    total_questions_by_type[q_type] = 0
                
                total_questions_by_type[q_type] += 1
                if not is_correct:
                    question_type_errors[q_type] += 1
        
        # Calculate error rates
        challenges = []
        for q_type in question_type_errors:
            if total_questions_by_type[q_type] >= 5:  # Only consider types with enough data
                error_rate = (question_type_errors[q_type] / total_questions_by_type[q_type]) * 100
                
                if error_rate >= 40:  # High error rate
                    challenges.append({
                        'area': q_type.replace('_', ' ').title(),
                        'error_rate': round(error_rate, 1),
                        'total_questions': total_questions_by_type[q_type],
                        'incorrect_answers': question_type_errors[q_type]
                    })
        
        # Sort by error rate
        challenges.sort(key=lambda x: x['error_rate'], reverse=True)
        
        return challenges[:5]  # Return top 5 challenges