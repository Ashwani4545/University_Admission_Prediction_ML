"""
AI-Powered Recommendation Engine
Generates personalized recommendations based on predictions
"""
from typing import List, Dict, Any
from app.schemas.predictions import Recommendation, FeatureImportance

class RecommendationEngine:
    """
    Generates personalized, actionable recommendations
    based on ML predictions and feature importance
    """
    
    def generate_admission_recommendations(
        self,
        features: Dict[str, Any],
        probability: float,
        feature_importance: List[FeatureImportance]
    ) -> List[Recommendation]:
        """Generate recommendations for improving admission chances"""
        recommendations = []
        
        # Analyze GRE score
        if features['gre_score'] < 320:
            recommendations.append(Recommendation(
                category="Test Preparation",
                title="Improve GRE Score",
                description=f"Your current GRE score of {features['gre_score']} can be improved. "
                           f"Aim for 320+ to significantly boost admission chances.",
                priority="high",
                actionable_steps=[
                    "Enroll in Manhattan Prep or Magoosh GRE course",
                    "Practice 2 hours daily for 8-12 weeks",
                    "Take 5+ full-length practice tests",
                    "Focus on weak areas identified in practice tests",
                    "Consider retaking the test in 2-3 months"
                ]
            ))
        
        # Analyze TOEFL score
        if features['toefl_score'] < 100:
            recommendations.append(Recommendation(
                category="Language Proficiency",
                title="Enhance English Proficiency",
                description=f"TOEFL score of {features['toefl_score']} is below top-tier requirements. "
                           f"Target 100+ for competitive programs.",
                priority="high" if features['toefl_score'] < 90 else "medium",
                actionable_steps=[
                    "Practice speaking and writing sections daily",
                    "Watch English content without subtitles",
                    "Join TOEFL preparation groups online",
                    "Take TOEFL iBT practice tests",
                    "Consider retaking within 3 months"
                ]
            ))
        
        # Analyze CGPA
        if features['cgpa'] < 8.0:
            recommendations.append(Recommendation(
                category="Academic Performance",
                title="Strengthen Academic Record",
                description=f"CGPA of {features['cgpa']} can be improved. Focus on remaining coursework.",
                priority="medium",
                actionable_steps=[
                    "Prioritize core subject grades",
                    "Seek help from professors during office hours",
                    "Form study groups with high-performing peers",
                    "Take fewer courses per semester to maintain quality",
                    "Consider taking additional courses to boost GPA"
                ]
            ))
        
        # Research experience
        if not features['research_experience']:
            recommendations.append(Recommendation(
                category="Research & Projects",
                title="Gain Research Experience",
                description="Research experience significantly boosts admission chances, especially for PhD programs.",
                priority="high" if probability < 0.6 else "medium",
                actionable_steps=[
                    "Contact professors about research opportunities",
                    "Join ongoing research projects as volunteer",
                    "Attend research seminars and workshops",
                    "Aim to get paper published or presented",
                    "Document all research work for your CV"
                ]
            ))
        
        # SOP and LOR
        if features['sop_strength'] < 4.0:
            recommendations.append(Recommendation(
                category="Application Materials",
                title="Strengthen Statement of Purpose",
                description="A compelling SOP can significantly improve your application.",
                priority="high",
                actionable_steps=[
                    "Clearly articulate your research interests",
                    "Connect past experiences to future goals",
                    "Get feedback from professors and mentors",
                    "Revise at least 5-7 times before submission",
                    "Tailor SOP for each university"
                ]
            ))
        
        if features['lor_strength'] < 4.0:
            recommendations.append(Recommendation(
                category="Application Materials",
                title="Secure Strong Recommendation Letters",
                description="Strong LORs from well-known professors carry significant weight.",
                priority="medium",
                actionable_steps=[
                    "Build relationships with professors early",
                    "Excel in their courses and participate actively",
                    "Assist in research or teaching activities",
                    "Provide recommenders with your CV and goals",
                    "Give recommenders at least 4 weeks notice"
                ]
            ))
        
        # University selection strategy
        if features['university_rating'] > 4 and probability < 0.7:
            recommendations.append(Recommendation(
                category="University Selection",
                title="Balance Your University List",
                description="Consider applying to a mix of reach, target, and safety schools.",
                priority="high",
                actionable_steps=[
                    "Apply to 2-3 reach schools (top tier)",
                    "Apply to 3-4 target schools (good match)",
                    "Apply to 2-3 safety schools (high chances)",
                    "Research professor's work at each university",
                    "Consider programs with funding opportunities"
                ]
            ))
        
        # General timeline and planning
        if len(recommendations) > 0:
            recommendations.append(Recommendation(
                category="Planning & Timeline",
                title="Create Structured Improvement Plan",
                description="Systematic preparation over 6-12 months yields best results.",
                priority="high",
                actionable_steps=[
                    "Create month-by-month preparation timeline",
                    "Set specific, measurable goals for each area",
                    "Track progress weekly using a journal",
                    "Adjust strategy based on practice test results",
                    "Apply early decision/action when possible"
                ]
            ))
        
        # Sort by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        recommendations.sort(key=lambda x: priority_order[x.priority])
        
        return recommendations[:5]  # Return top 5
    
    def generate_dropout_recommendations(
        self,
        features: Dict[str, Any],
        dropout_risk: bool,
        probability: float,
        risk_factors: List[Dict[str, Any]]
    ) -> List[Recommendation]:
        """Generate intervention recommendations for dropout prevention"""
        recommendations = []
        
        # Attendance-based recommendations
        if features['attendance_rate'] < 80:
            severity = "critical" if features['attendance_rate'] < 70 else "high"
            recommendations.append(Recommendation(
                category="Attendance",
                title="Improve Attendance Immediately",
                description=f"Your {features['attendance_rate']}% attendance is concerning. "
                           f"Regular attendance is critical for academic success.",
                priority="high" if severity == "critical" else "medium",
                actionable_steps=[
                    "Set daily alarms for all classes",
                    "Find an accountability partner/study buddy",
                    "Speak with advisor about attendance barriers",
                    "Catch up on missed material immediately",
                    "Aim for 90%+ attendance moving forward"
                ]
            ))
        
        # Academic performance
        if features['academic_grades'] < 70:
            recommendations.append(Recommendation(
                category="Academic Support",
                title="Seek Academic Intervention",
                description=f"Grades of {features['academic_grades']}% indicate need for immediate support.",
                priority="high",
                actionable_steps=[
                    "Schedule meeting with academic advisor",
                    "Enroll in free tutoring services",
                    "Join study groups for difficult subjects",
                    "Meet with professors during office hours",
                    "Consider reducing course load next semester"
                ]
            ))
        
        # Family support
        if not features['family_support']:
            recommendations.append(Recommendation(
                category="Support System",
                title="Build Support Network",
                description="Lack of family support can be supplemented with institutional resources.",
                priority="high",
                actionable_steps=[
                    "Schedule counseling session to discuss challenges",
                    "Join student support groups or clubs",
                    "Connect with peer mentors",
                    "Explore financial aid options if needed",
                    "Build relationship with faculty advisor"
                ]
            ))
        
        # Study habits
        if features['study_hours'] < 3:
            recommendations.append(Recommendation(
                category="Study Habits",
                title="Establish Better Study Routine",
                description=f"{features['study_hours']} hours of daily study is insufficient. "
                           f"Aim for 3-4 hours of focused study.",
                priority="medium",
                actionable_steps=[
                    "Create structured daily study schedule",
                    "Use Pomodoro technique (25 min focused work)",
                    "Find quiet study space (library, study hall)",
                    "Eliminate distractions (phone, social media)",
                    "Study most difficult subjects when most alert"
                ]
            ))
        
        # Socio-economic challenges
        if features['socio_economic_status'] == 'low':
            recommendations.append(Recommendation(
                category="Financial Support",
                title="Explore Financial Assistance",
                description="Financial stress can impact academic performance. Help is available.",
                priority="high" if dropout_risk else "medium",
                actionable_steps=[
                    "Apply for scholarships and grants",
                    "Speak with financial aid office",
                    "Explore campus employment opportunities",
                    "Look into emergency financial assistance",
                    "Connect with resource centers for basic needs"
                ]
            ))
        
        # Distance/commute issues
        if features['distance_from_school'] > 15:
            recommendations.append(Recommendation(
                category="Logistics",
                title="Address Transportation Challenges",
                description=f"{features['distance_from_school']}km commute may be affecting engagement.",
                priority="low",
                actionable_steps=[
                    "Explore on-campus housing options",
                    "Look into carpool arrangements",
                    "Check for student housing near campus",
                    "Adjust schedule to minimize commute trips",
                    "Use commute time productively (audiobooks, review)"
                ]
            ))
        
        # Parent education / first-generation support
        if features['parent_education'] in ['high_school', 'none']:
            recommendations.append(Recommendation(
                category="First-Generation Support",
                title="Access First-Generation Resources",
                description="First-generation students have unique challenges. Special support is available.",
                priority="medium",
                actionable_steps=[
                    "Join first-generation student programs",
                    "Connect with peer mentors",
                    "Attend academic success workshops",
                    "Learn about graduate school pathways early",
                    "Build relationship with career services"
                ]
            ))
        
        # Overall wellness
        if dropout_risk:
            recommendations.append(Recommendation(
                category="Wellness & Mental Health",
                title="Prioritize Overall Wellbeing",
                description="Academic success is closely tied to mental and physical health.",
                priority="high",
                actionable_steps=[
                    "Schedule appointment with wellness center",
                    "Maintain regular sleep schedule (7-8 hours)",
                    "Exercise regularly (even 20 min walks help)",
                    "Practice stress management techniques",
                    "Don't hesitate to use campus mental health services"
                ]
            ))
        
        # Sort by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        recommendations.sort(key=lambda x: priority_order[x.priority])
        
        return recommendations[:6]  # Return top 6
